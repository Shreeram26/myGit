import os

def execute(args):
    index_path = ".mygit/index"

    if not os.path.exists(index_path):
        print("Error: No Repository initialized. Please run 'mygit init' first.")
        return
    
    if os.path.getsize(index_path) == 0:
        print("No files staged for commit.")
        return
    
    with open(index_path, "r") as f:
        staged_files = f.read() 
    
    print("Staged files:")
    for line in staged_files.splitlines():
        print(" -", line)