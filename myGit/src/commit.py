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

    head_path = ".mygit/HEAD"
    parent_hash=None

    if os.path.exists(head_path):
        with open(head_path, "r") as f:
            parent_hash = f.read().strip()
    
    if parent_hash:
        commit_content = f"Parent: {parent_hash}\n{commit_content}"

    with open(f".mygit/objects/{commit_hash}","w") as f:
        f.write(commit_content)

    with open(".mygit/HEAD","w") as f:
        f.write(commit_hash)    
    
    with open(index_path, "w") as f:
        pass