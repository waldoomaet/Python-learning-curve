import os


class newOpen:
    def __init__(self, path, accessType):
        self.path = path
        self.accessType = accessType

    @staticmethod
    def splitlines(path, separator):
        sepFinderStart = 0
        sepFinderEnd = path.find(separator)
        output = []
        while sepFinderEnd != -1:
            output.append(path[sepFinderStart:sepFinderEnd])
            sepFinderStart = sepFinderEnd + 1
            sepFinderEnd = path.find(separator, sepFinderStart)
        output.append(path[sepFinderStart:])
        return output

    @staticmethod
    def __checkExists(path):
        if os.path.exists(path):
            return True
        return False

    def read(self):
        file = open(self.path, self.accessType)
        output = file.read()
        file.close()
        return output

    def write(self, content):
        folders = newOpen.splitlines(self.path, "\\")
        file = folders.pop(-1)
        firstTime = True
        fullPath = ''
        for folder in folders:
            if firstTime:
                firstTime = False
                fullPath += folder
            else:
                fullPath += f"\\{folder}"
            if not newOpen.__checkExists(fullPath):
                os.mkdir(fullPath)
        fullPath += f"\\{file}"
        file = open(self.path, self.accessType)
        file.write(content)
        file.close()
