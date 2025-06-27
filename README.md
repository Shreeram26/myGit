# myGit
# 🌀 myGit – A Custom Version Control System

Welcome to **myGit**, a mini version control system built from scratch using Python, inspired by Git!


## ✅ Implemented Commands

### `init`
Initializes a new myGit repository in the current directory.

- Creates a `.mygit/` folder with subfolders:
  - `.mygit/objects` → stores blobs (content of files, commits)
  - `.mygit/refs` → for future branch pointers
  - `.mygit/index` → the staging area
  - `.mygit/HEAD` → stores the latest commit hash

### `add <file1> <file2> ...`
Stages files by:
- Reading each file
- Generating a SHA-1 hash of its content
- Saving the file content as an object in `.mygit/objects/`
- Writing the hash and filename to `.mygit/index`

### `commit -m "message"`
Commits all staged files.
- Reads all staged file hashes from `.mygit/index`
- Stores commit metadata (message and parent commit) as a new object
- Updates `.mygit/HEAD` with new commit hash
- Clears the `.mygit/index`

### `status`
Displays currently staged files.
- Reads `.mygit/index`
- Lists all files that have been added but not yet committed

### `checkout <commit_hash>`
Restores the project directory to the state of a specific commit.
- Reads the commit object
- Overwrites working directory files using the hashes recorded in that commit
- Updates `.mygit/HEAD`

### `log`
Displays the commit history starting from the latest.
- Reads `.mygit/HEAD`
- Follows the chain of `Parent:` hashes to print each commit’s message and ID

---

## 🔧 Tech Stack
- Python 3.11+
- Modules used: `os`, `hashlib`, `argparse`

---

