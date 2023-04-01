class SortFiles:
    def __init__(self, files: list):
        self.files = files

    # если не указан конкретный файл, то возвращаем словарь файл:кол-во строк, иначе кол-во строк в 1 файле
    def get_count_lines(self, file=None):

        if file == None:
            files_dict = {}

            for file in self.files:
                files_dict[file] = sum(1 for line in open(file, 'rt'))
        
            return files_dict
        else:
            return sum(1 for line in open(file, 'rt'))
    
    
    def sort_files(self):
        sort_files = []
        valuses = []
        for val in self.get_count_lines().values():
            valuses.append(int(val))

        for n in range(max(valuses) + 1):
            for key, val in self.get_count_lines().items():
                if val not in sort_files:
                    if val == n:
                        sort_files.append(key)
        return sort_files


    def write_file(self):
        with open('4.txt', 'w') as file_for_write:
            pass
        for file in self.sort_files():
            with open('4.txt', 'at') as file_for_write:
                file_for_write.write(f'{file}\n')
                file_for_write.write(str(f'{self.get_count_lines(file)}\n'))
            with open(file, 'rt') as file_for_read:
                for i in range(self.get_count_lines(file)):
                    line = file_for_read.readline()
                    with open('4.txt', 'at') as file_for_write:
                        file_for_write.write(f'Строка номер {i+1} файла номер {str(file)[0]}\t {line}')


sorting = SortFiles(['1.txt', '2.txt', '3.txt'])

# Файл с именем 4.txt создается в каталоге запуска main.py
sorting.write_file()