import datetime
import time
from pathlib import Path

from dateutil import parser

from komodo.core.utils.rag_context import RagContext
from komodo.shared.utils.filestats import file_details
from komodo.shared.utils.globber import Globber


class Indexer:
    def __init__(self, rag_context: RagContext):
        self.rag_context = rag_context
        self.globber = Globber(rag_context.path, self.__on_created, self.__on_deleted)

    def __on_created(self, filepath):
        print("Reviewing status of file: " + filepath)
        if not self.needs_indexing(filepath):
            return

        # index the file
        self.rag_context.index(filepath)

        # update the file details
        file = file_details(filepath)
        file.indexed_at = datetime.datetime.utcnow().isoformat() + 'Z'
        self.rag_context.update_file(filepath, file)

    def __on_deleted(self, filepath):
        print("Removing deleted file: " + filepath)
        self.rag_context.remove(filepath)

    def add_intelligence(self, filepath):
        print("Adding intelligence to: " + filepath)

    def needs_indexing(self, filepath):
        print("Checking if file needs indexing: " + filepath)
        file = self.rag_context.find_file(filepath)
        if not file or not file.indexed_at:
            return True

        datetime_indexed_at = parser.parse(file.indexed_at)
        datetime_modified = datetime.datetime.fromtimestamp(Path(filepath).stat().st_mtime, datetime.timezone.utc)

        print(f"Indexed at: {datetime_indexed_at}")
        print(f"Modified at: {datetime_modified}")

        if datetime_indexed_at >= datetime_modified:
            print(f"Already indexed: {filepath} in collection: {self.rag_context.shortcode} at {file.indexed_at}")
            return False
        else:
            print(f"File has been updated since last index: {filepath} in collection. Re-indexing...")
            return True

    def run(self, max_updates=1, update_interval=5, reindex=False):
        if reindex:
            print("Reindexing...")
            self.rag_context.reset_all()

        # ensure that there have not been any files deleted since the last run
        files = self.globber.get_files_recursively_pathlib()
        print("Files: " + str(files))
        ragged_files = self.rag_context.get_all_indexed_files()
        print("Ragged Files: " + str(ragged_files))

        for file in ragged_files:
            if file not in files:
                print("File has been deleted: " + file)
                self.rag_context.remove(file)

        self.globber.start()
        update_count = 1  # start runs the initial update
        while update_count < max_updates or max_updates == 0:
            time.sleep(update_interval)
            self.globber.updates()
            update_count += 1

        print("Indexed. Looped " + str(update_count) + " times. Stopping...")


if __name__ == "__main__":
    from komodo.config import PlatformConfig

    data_path = PlatformConfig().komodo_hello_path
    cache_path = PlatformConfig().cache()
    rag_context = RagContext(path=data_path, cache_path=cache_path)
    indexer = Indexer(rag_context)
    indexer.run(update_interval=5)
