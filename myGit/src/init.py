import os

def execute():
    if os.path.exists(".mygit"):
        print("Repository already initialized.")
        return

    os.makedirs(".mygit/objects",exist_ok=True)
    os.makedirs(".mygit/refs",exist_ok=True)

    with open(".mygit/HEAD", "w") as f:
        pass

    print("Initialized empty MyGit repository in .mygit/")

