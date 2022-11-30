import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:\Users\sales\Downloads"

class FileEventHandler(FileSystemHandler):
    def on_created(self, event):
        print(f"hey {event.src_path} has been created!")
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src_path}!")
    def on_modified(slef, event):
        print(f"Hey there!, {event.src_path} has been modified")
    def on_moved(self, event):
        print(f"someone moved {event.src_path} to {event.dest_path}")

event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()