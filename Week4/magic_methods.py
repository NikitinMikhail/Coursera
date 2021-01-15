import tempfile
import os


class File:
    def __init__(self, path_to_file=None):
        self.path_to_file = path_to_file
        if not os.path.exists(self.path_to_file):
            with open(self.path_to_file, 'w'):
                pass
        self.abspath = os.path.abspath(self.path_to_file)


    def __add__(self, other):
        new_path = str(hash(self.path_to_file + other.path_to_file))
        new_file = File(os.path.join(tempfile.gettempdir(), new_path))
        new_file.write(self.read() + other.read())
        return new_file

    def read(self):
        with open(self.path_to_file, 'r') as f:
            return f.read()

    def write(self, some_text: str):
        with open(self.path_to_file, 'w') as f:
            return f.write(some_text)

    def __iter__(self):
        with open(self.path_to_file, 'r') as f:
            self.lines = f.readlines()
        self.current = 0
        self.end = len(self.lines)
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        return_line = self.lines[self.current]
        self.current += 1
        return return_line

    def __str__(self):
        return self.abspath
