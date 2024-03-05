#1
import os

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll directories and files:")
    for item in os.listdir(path):
        print(item)

path = str(input())

list_directories_files(path)

#2
import os

def check_access(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    if os.access(path, os.R_OK):
        print(f"Path '{path}' is readable.")
    else:
        print(f"Path '{path}' is not readable.")
    if os.access(path, os.W_OK):
        print(f"Path '{path}' is writable.")
    else:
        print(f"Path '{path}' is not writable.")
    if os.access(path, os.X_OK):
        print(f"Path '{path}' is executable.")
    else:
        print(f"Path '{path}' is not executable.")

path = str(input())
check_access(path)

#3
import os

def check_path(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    filename = os.path.basename(path)
    directory = os.path.dirname(path)
    print(f"Path '{path}' exists.")
    print(f"Filename: {filename}")
    print(f"Directory: {directory}")
path = "path_to_your_file_or_directory"
check_path(path)

#4
def count_lines(filename):
    with open(filename, 'r') as file:
        num_lines = sum(1 for line in file)
    return num_lines
filename = str(input())
num_lines = count_lines(filename)
print(f"Number of lines in '{filename}': {num_lines}")

#5
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')
filename = str(input())
data = input().split()
write_list_to_file(filename, data)

#6
import string

def generate_files():
    for letter in string.ascii_uppercase:
        filename = letter + ".txt"
        with open(filename, 'w') as file:
            file.write("This is file " + filename)
generate_files()

#7
def copy_file(source, destination):
    with open(source, 'r') as src_file:
        with open(destination, 'w') as dest_file:
            dest_file.write(src_file.read())
source_file = str(input())
destination_file = str(input())
copy_file(source_file, destination_file)

#8
import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"Path '{path}' does not exist.")
        return
    if not os.path.isfile(path):
        print(f"Path '{path}' is not a file.")
        return
    if not os.access(path, os.R_OK):
        print(f"Path '{path}' is not readable.")
        return
    if not os.access(path, os.W_OK):
        print(f"Path '{path}' is not writable.")
        return
    if not os.access(path, os.X_OK):
        print(f"Path '{path}' is not executable.")
        return
    os.remove(path)
    print(f"File '{path}' deleted successfully.")
file_path = str(input())
delete_file(file_path)


