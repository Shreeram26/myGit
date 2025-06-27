import os

def execute(args):
    commit_hash = args.branch

    commit_path = f".mygit/objects/{commit_hash}"
    if not os.path.exists(commit_path):
        print(f"Error: Commit {commit_hash} does not exist.")
        return
    
    with open(commit_path, "r") as f:
        lines = f.readlines()
    
    i = 0
    while i < len(lines) and lines[i].strip() != "":
        i += 1
    i += 1  


    for line in lines[i:]:
        line = line.strip()
        if line == "":
            continue

        object_hash, file_name = line.split(" ", 1)
        object_path = f".mygit/objects/{object_hash}"
        
        if not os.path.exists(object_path):
            print(f"Error: Object {object_hash} for file {file_name} does not exist.")
            continue

        with open(object_path, "rb") as f:
            content = f.read()

        with open(file_name, "wb") as f:
            f.write(content)

        print(f"Restored {file_name} from commit {commit_hash}")

    with open(".mygit/HEAD", "w") as f:
        f.write(commit_hash)
    
    print(f"Checkout completed successfully!")
