from abc import ABC, abstractmethod


class File(ABC):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.file = None

    @abstractmethod
    def __open__(self):
        pass

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def __read__(self):
        pass


class TxtFile(File):
    def __init__(self, path, mode='r'):
        super(TxtFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass


class Json:
    def __init__(self):
        pass


class XmlFile(File):
    def __init__(self, path, mode='r'):
        super(XmlFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass


class ZipFile(File):
    def __init__(self, path, mode='r'):
        super(ZipFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass

    def open_excel(self):
        pass


class DataFile(File):
    def __init__(self, path, mode='r'):
        super(DataFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass


class ConfigFile(File):
    def __init__(self, path, mode):
        super(ConfigFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass


class CoilConfigFile(File):
    def __init__(self, path, mode):
        super(CoilConfigFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass


class ExcelFile(File):
    def __init__(self, path, mode='r'):
        super(ExcelFile, self).__init__(path, mode)

    def __open__(self):
        pass

    def __read__(self):
        pass

    def open(self):
        pass

    def open_sheet(self):
        pass

    def save(self):
        pass
