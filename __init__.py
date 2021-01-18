import os

folders = [
    "docs", 
    "bin", 
    "tests"
]

def init_project_structure():
    for folder in folders:
        if not os.path.exists(folder):
            os.mkdir(folder)


if __name__ == "__main__": # magic method
    init_project_structure()