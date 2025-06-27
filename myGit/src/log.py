import os

def execute(args):
    print()
    if not os.path.exists(".mygit/HEAD"):
        print("Error: No repository initialized. Please run 'mygit init' first.")
        return
    
    with open(".mygit/HEAD", "r") as f:
        commit_hash = f.read().strip()
    
    if not commit_hash:
        print("No commits found.")
        return

    while commit_hash:
        commit_path = f".mygit/objects/{commit_hash}"

        if not os.path.exists(commit_path):
            print(f"Error: Commit object {commit_hash} not found.")
            break

        with open(commit_path, "r") as f:
            content = f.readlines()

        print(f"Commit: {commit_hash}")
        parent = None
        message = None

        for line in content:
            if line.startswith("Parent:"):
                parent = line.split(":", 1)[1].strip()
            elif line.startswith("Commit Message:"):
                message = line.strip()

        if message:
            print(message)
        print()

        commit_hash = parent
