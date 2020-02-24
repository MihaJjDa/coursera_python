class FileReader:
    def __init__(self, name):
        self.file = name

    def read(self):
        try:
            with open(self.file, 'r') as f:
                return f.read()
        except:
            return ''

