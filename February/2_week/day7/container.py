class Folder:
    def __init__(self, files):
        self.files = files
    def __getitem__(self, index):
        return self.files[index]
    def __len__(self):
        return len(self.files)

file_list = ["text_{}.txt".format(i) for i in range(10) ]
print(file_list,'\n')

folder = Folder(file_list)
print(folder,'\n')

print(folder[-3])

print(len(folder))