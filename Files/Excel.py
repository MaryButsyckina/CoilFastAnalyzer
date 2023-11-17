from openpyxl.styles import PatternFill, Alignment


class MeasurementTemplate:
    def __init__(self, file_path, book_name, sheet_name, data, mode):
        self.file_path = file_path
        self.book_name = book_name
        self.sheet_name = sheet_name
        self.data = data

    def get_file(self):
        pass

    def create_sheet(self):
        pass

    def write_data(self):
        pass

    def save_book(self):
        pass

    def style_sheet(self):
        pass

    def run(self):
        pass
