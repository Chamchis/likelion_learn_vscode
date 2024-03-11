import os, shutil
current_directory = os.getcwd()
print(current_directory)

# os.mkdir('new_dir')

# os.makedirs('shopping/computer')

# os.rmdir('new_dir')

# shutil.rmtree('shopping')

os.chdir('chdir_test')

current_directory = os.getcwd()
print(current_directory)

os.chdir('../')

current_directory = os.getcwd()
print(current_directory)

print(os.listdir('chdir_test'))

home_directory = os.getenv('PATH')
print("Home Directory:", home_directory)