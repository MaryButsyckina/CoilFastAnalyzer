from abc import ABC, abstractmethod
import json


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
    # def __init__(self, path, mode):
    #     self.path = path
    #     self.mode = mode
    @staticmethod
    def open(path, mode):
        with open(path, mode) as file:
            return json.loads(str(file.read()))


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
    def __init__(self, path="config.cfg", mode='r'):
        super(ConfigFile, self).__init__(path, mode)
        self.result = {}

    def __open__(self):
        obj = Json.open(self.path, self.mode)
        for key in obj.keys():
            self.result[key] = {}
            for element in obj[key].keys():
                if obj[key][element]["Active"]:
                    self.result[key] = obj[key][element]
        return self.result

    def __read__(self):
        pass

    def open(self):
        return self.__open__()


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
