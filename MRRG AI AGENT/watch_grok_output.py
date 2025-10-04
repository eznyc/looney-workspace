import os
import time
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class GrokOutputHandler(FileSystemEventHandler):
    def __init__(self):
        self.target_dir = "/Users/3treeforest/Desktop/DEV/MRRG AI AGENT/scripts"
        self.downloads_dir = os.path.expanduser("~/Downloads")

    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith(".json") and "grok_output" in os.path.basename(event.src_path):
            time.sleep(1)  # Wait for file to finish writing
            file_name = os.path.basename(event.src_path)
            new_name = file_name.replace("grok_output", "claude_ready")
            target_path = os.path.join(self.target_dir, new_name)
            shutil.move(event.src_path, target_path)
            print(f"Moved {file_name} to {target_path} for Claude processing")

if __name__ == "__main__":
    downloads_path = os.path.expanduser("~/Downloads")
    event_handler = GrokOutputHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_path, recursive=False)
    observer.start()
    print("Watching Downloads for Grok output files...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
