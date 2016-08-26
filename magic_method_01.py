class File():
    def __init__(self, name, mode='w'):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print(self)
        self.file_handle = open(self.name, self.mode)
        return self.file_handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file_handle.close()

with File('Context.txt', 'a') as f:
    f.write ('Guaranteered records!')
