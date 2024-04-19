import os
import sys
import json
import argparse
import time
import signal
from tqdm import tqdm
from dotenv import load_dotenv

from .scripts.pl_art import *
# from .scripts.pl_art import print_eagle
from .scripts.document_reader import DocumentAIProcessor
load_dotenv()

# progress_bar = None
LOG_FILE = "log.json"
log_dict = {}
# project_id = os.getenv("PROJECT_ID")
project_id='splendid-howl-419519'
# location = os.getenv("LOCATION")
location = 'us'
# processor_display_name = os.getenv("PROCESSOR_DISPLAY_NAME")
processor_display_name = 'pdf_processor_37877f60-bfc1-4923-8271-96e83dd09627'

document_reader = DocumentAIProcessor(project_id, location, processor_display_name)


import os
import sys
import json
import time
import signal
from tqdm import tqdm
from dotenv import load_dotenv

# from scripts.pl_art import *
# from scripts.pl_art import print_eagle
# from scripts.document_reader import DocumentAIProcessor

load_dotenv()

LOG_FILE = "log.json"
log_dict = {}
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
processor_display_name = os.getenv("PROCESSOR_DISPLAY_NAME")

document_reader = DocumentAIProcessor(project_id, location, processor_display_name)


def handler(signum, frame):
    res = input("\nCtrl-C was pressed. Do you really want to exit? y/n ")
    if res == "y":
        if progress_bar is not None:
            progress_bar.close()
        sys.exit(1)


signal.signal(signal.SIGINT, handler)

load_dotenv()

if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as log_file:
        json.dump({}, log_file)
else:
    with open(LOG_FILE, "r") as log_file:
        try:
            log_dict = json.load(log_file)
        except json.decoder.JSONDecodeError:
            log_dict = {}


def count_pdf_files(directory):
    return sum(
        [
            len([f for f in files if f.endswith(".pdf")])
            for r, d, files in os.walk(directory)
        ]
    )

def is_log_file_empty():
    with open(LOG_FILE, 'r') as log_file:
        content = log_file.read()
        return content.strip() == '{}'

def traverse_folder(folder_path, continue_scan, doc_obj, progress_bar=None):

    for entry in os.listdir(folder_path):
        path = os.path.join(folder_path, entry)
        if os.path.isdir(path):
            traverse_folder(path, continue_scan, doc_obj, progress_bar=progress_bar)
        elif path.endswith(".pdf"):
            doc_obj.read_document(path)
            doc_obj.cluster_file()
            if continue_scan and log_dict.get(path) is not None:
                continue
            time.sleep(0.5)
            if progress_bar is not None:
                progress_bar.set_postfix(file=path, refresh=True)
                progress_bar.update(1)
            log_dict[path] = True
            with open(LOG_FILE, "w") as log_file:
                json.dump(log_dict, log_file)


def main():

    print_eagle()
    if len(sys.argv) != 2:
        print("Usage: python script.py <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        sys.exit(1)

    if is_log_file_empty():
        continue_scan = False
    else:
        continue_scan = input("Do you want to continue from where you left off? (yes/no): ")
        continue_scan = continue_scan.lower() == "yes"
        
    if not continue_scan:
        with open(LOG_FILE, "w") as log_file:
            json.dump({}, log_file)
            
    try:
        with open(LOG_FILE, "r") as log_file:
            log_dict = json.load(log_file)
    except FileNotFoundError:
        log_dict = {}

    total_files = count_pdf_files(folder_path)
    processed_files = len(log_dict)
    progress_bar = tqdm(total=total_files, initial=processed_files)
    traverse_folder(folder_path, continue_scan, document_reader, progress_bar=progress_bar)
    with open(LOG_FILE, "w") as log_file:
            json.dump({}, log_file)
    progress_bar.close()



if __name__ == "__main__":
    main()
