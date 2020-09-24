class FileReader:
    """Class for reading file content"""

    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):

        """Read file content as one line, return empty string otherwise"""
        try:
            with open(self.filepath, 'r+') as file_content:
                content_line = file_content.read()
        except FileNotFoundError:
            content_line = ''

        return content_line
