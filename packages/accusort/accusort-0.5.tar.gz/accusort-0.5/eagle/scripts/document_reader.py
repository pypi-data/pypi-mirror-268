import os
import re
import shutil
from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import AlreadyExists
from google.cloud import documentai


class DocumentAIProcessor:

    def __init__(self, project_id, location, processor_display_name):
        self.project_id = project_id
        self.location = location
        self.processor_display_name = processor_display_name
        self.document_client = self.create_document_client()
        self.processor = self.create_document_process()

    def create_document_client(self) -> documentai.DocumentProcessorServiceClient:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        return documentai.DocumentProcessorServiceClient(client_options=opts)

    def create_document_process(self) -> documentai.Processor:
        # The full resource name of the location, e.g.:
        # `projects/{project_id}/locations/{location}`
        parent = self.document_client.common_location_path(
            self.project_id, self.location
        )

        # Create a processor with the input config.
        # if a processor with the same name exists, the existing processor will be used.
        try:
            processor = self.document_client.create_processor(
                parent=parent,
                processor=documentai.Processor(
                    type_="OCR_PROCESSOR",
                    display_name=self.processor_display_name,
                ),
            )
        except AlreadyExists:
            processors = self.document_client.list_processors(parent=parent)
            for proc in processors:
                if proc.display_name == self.processor_display_name:
                    processor = proc
                    break
        return processor

    def read_document(self, file_path):
        self.file_path = file_path
        with open(file_path, "rb") as file:
            file_content = file.read()

        raw_document = documentai.RawDocument(
            content=file_content,
            mime_type="application/pdf",
        )

        # Configure the process request
        # `processor.name` is the full resource name of the processor, e.g.:
        # `projects/{project_id}/locations/{location}/processors/{processor_id}`
        request = documentai.ProcessRequest(
            name=self.processor.name, raw_document=raw_document
        )

        result = self.document_client.process_document(request=request)
        self.document = result.document

    def cluster_file(self):
        clustered = False
        pattern = "[-\/\n ]"
        document_pages = self.document.pages
        document_text = self.document.text
        folder_name = os.path.dirname(self.file_path)
        file_name = os.path.basename(self.file_path)
        pl_id = re.sub(pattern, "", re.split("[_ ]", file_name.split(".")[0])[0])

        for page in document_pages:
            for lines in page.lines:
                confidence = round(lines.layout.confidence, 4)
                segment = lines.layout.text_anchor.text_segments[0]
                content = document_text[segment.start_index : segment.end_index].split(
                    " "
                )
                try:
                    content = re.sub(pattern, "", content[1])
                except IndexError:
                    content = content[0]

                if content != pl_id:
                    continue
                if confidence >= 0.9:
                    os.makedirs(os.path.join(folder_name, "accurate"), exist_ok=True)
                    shutil.copy(
                        self.file_path, os.path.join(folder_name, "accurate", file_name)
                    )
                elif 0.8 <= confidence < 0.9:
                    os.makedirs(
                        os.path.join(folder_name, "almost_accurate"), exist_ok=True
                    )
                    shutil.copy(
                        self.file_path,
                        os.path.join(folder_name, "almost_accurate", file_name),
                    )
                elif confidence < 0.8:
                    os.makedirs(os.path.join(folder_name, "ambiguous"), exist_ok=True)
                    shutil.copy(
                        self.file_path,
                        os.path.join(folder_name, "ambiguous", file_name),
                    )
                clustered = True
                break

        if not clustered:
            os.makedirs(os.path.join(folder_name, "unclustered"), exist_ok=True)
            shutil.copy(
                self.file_path, os.path.join(folder_name, "unclustered", file_name)
            )
