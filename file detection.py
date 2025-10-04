# Python file detection

import os

file_path = "test.txt"

if os.path.exists(file_path):
    print(f"The file {file_path} exists")
else:
    print(f"The file {file_path} does not exist") 

