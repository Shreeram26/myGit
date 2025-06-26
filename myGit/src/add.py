import os
import hashlib

def execute(args):
    for file in args.files:
        if not os.path.exists(file):
            print(f"Error: {file} does not exist.")
            continue

        print(f"Adding {file} to the staging area...")
        with open(file, "rb") as f:
            content = f.read()
        
        hash = hashlib.sha1(content).hexdigest()
        os.makedirs(".mygit/objects", exist_ok=True)
        with open(f".mygit/objects/{hash}", "wb") as f:
            f.write(content)
        
        with open(".mygit/index", "a") as f:
            f.write(f"{hash} {file}\n")

