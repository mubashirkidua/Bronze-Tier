from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
import time
import shutil
from datetime import datetime

class DropHandler(FileSystemEventHandler):
    def __init__(self, vault_path):
        self.vault = Path(vault_path)
        self.needs_action = self.vault / "Needs_Action"
        self.inbox = self.vault / "Inbox"
        self.logs = self.vault / "Logs"

    def on_created(self, event):
        if event.is_directory:
            return
        source = Path(event.src_path)
        if source.parent.name != "Inbox":
            return

        dest = self.needs_action / f"FILE_{source.name}"
        shutil.copy2(source, dest)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date_only = datetime.now().strftime("%Y-%m-%d")
        
        # Create log entry
        log_file = self.logs / f"activity_{date_only}.md"
        
        # Create log file if it doesn't exist
        if not log_file.exists():
            log_file.write_text(f"# Activity Log - {date_only}\n\n| Time | Action | Status |\n|------|--------|--------|\n")
        
        # Append log entry
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"| {timestamp} | File detected: {source.name} → FILE_{source.name} | ✅ |\n")
        
        print(f"[{timestamp}] ✅ New file detected and moved to Needs_Action: {source.name}")

if __name__ == "__main__":
    vault = Path(__file__).parent.parent  # AI_Employee_Vault root
    event_handler = DropHandler(vault)
    observer = Observer()
    observer.schedule(event_handler, path=str(vault / "Inbox"), recursive=False)
    observer.start()
    print("🚀 File System Watcher started... (Drop files in /Inbox)")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
