import os
import hashlib

def execute(args):
    index_path = ".mygit/index"
    if not os.path.exists(index_path):
        print("Error: No Repository initialized. Please run 'mygit init' first.")
        return
    
    if os.path.getsize(index_path) == 0:
        print("Error: No files staged for commit.")
        return
    
    with open(index_path,"r") as f:
        staged_files=f.read()

    commit_message =args.message
    commit_content = f"Commit Message: {commit_message}\n\n{staged_files}"
    commit_hash = hashlib.sha1(commit_content.encode()).hexdigest()

    with open(f".mygit/objects/{commit_hash}","w") as f:
        f.write(commit_content)

    with open(".mygit/HEAD","w") as f:
        f.write(commit_hash)    
    
    with open(index_path, "w") as f:
        pass