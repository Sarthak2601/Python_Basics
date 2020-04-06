from pathlib import Path

path = Path("ecommerce")
if path.exists():
    path.rmdir()  # Removes a directory
else:
    path.mkdir()  # Generates a directory

print(path.exists())  # Prints if the file exists or not

# Path can be defined in 2 ways -
# 1. Relative - In relation to the current file
# 2. Absolute - In relation with the root of the system

currentPath = Path()
for file in currentPath.glob('*.py'):    # Lists all the files with .py extension in the current directory
    print(file)

for file in currentPath.glob('*'):    # Lists all the files with all the extensions in the current path
    print(file)