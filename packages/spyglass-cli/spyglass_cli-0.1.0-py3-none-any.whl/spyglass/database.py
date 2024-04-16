import os
from pathlib import Path
import platform

import shelve as shelf

from utils import die, Project



class Shelf:
    def __init__(self, filename: str):
        self.file: Path = None
        self.db = None

        os_type: str = platform.system()

        if os_type == 'Linux':
            self.file = os.environ.get('HOME') + '/.local/share/' + filename
        elif os_type == 'Windows':
            self.file = os.environ.get('APPDATA') + filename
        else:
            die('OS not supported', 2)


    def __enter__(self):
        # Open the shelf and load data into self.db
        self.db = shelf.open(self.file, writeback=True)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Save any updates to the shelf
        if self.db is not None:
            self.db.sync()
            self.db.close()


    def update(self, entries: set) -> None:

        for entry in entries:
            if self.db.get(entry.name, None) != entry:
                self.db[entry.name] = entry


    def list(self) -> None:

        for _, proj in self.db.items():
            project: Project = proj
            print(str(project))


    def remove(self, entries: set) -> None:

        for entry in entries:
            if self.db.get(entry.name, None):
                del self.db[entry.name]

    def fetch(self) -> list:

        return self.db.values()
