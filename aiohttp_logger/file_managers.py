import os
from collections import defaultdict
from datetime import datetime
from utils import cleanup


class DailyFileManager:
    """Manages files daily
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.open_files = defaultdict()
        self.current_date = datetime.now().date()

    def is_opened(self, file_name, day):
        if datetime.now().date() != self.current_date:
            old_current_date = self.current_date
            self.current_date = datetime.now().date()
            for key in self.open_files:
                name, ext = os.path.splitext(key)
                archive_file_name = '%s.%s%s' % (name, old_current_date, ext)

                opened_file = self.open_files.get(key, None)
                if opened_file:
                    opened_file.close()
                if os.path.exists(archive_file_name):
                    with open(archive_file_name, 'a') as fp:
                        temp = open(key, 'r')
                        fp.write(temp.read())
                        temp.close()
                else:
                    os.rename(key, archive_file_name)

                self.open_files[key] = open('%s' % key, 'a')

            if day is not None:
                cleanup(day, file_name)
        if file_name in self.open_files:
            return True
        return False

    def open(self, file_name):
        self.open_files[file_name] = open('%s' % file_name, 'a')

    def write(self, file_name, data):
        self.open_files[file_name].write(data + '\n')
        self.open_files[file_name].flush()


DAILY_FILE_MANAGER = DailyFileManager()
