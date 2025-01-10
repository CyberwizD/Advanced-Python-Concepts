# Context Managers

from contextlib import contextmanager


@contextmanager
def open_managed_file(filename):
    with open(filename, 'a') as file:
        try:
            yield file
        finally:
            file.close()


with open_managed_file('notes.txt') as file:
    print("Managing file...")
    file.write("\nUsage - contextlib module")
    print("File Managed.")


class ManageFile:
    def __init__(self, filename):
        print('FILE MANAGER')
        self.filename = filename

    def __enter__(self):
        print('Opening file..')
        self.file = open(self.filename, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        print('File closed.')


with ManageFile('notes.txt') as filename:
    print('Writing to file...')
    filename.write('\nManaging File Context.')

# Trial
with open('notes.txt', 'a') as file:
    try:
        file.write('\nContext Managers.')
    finally:
        file.close()
