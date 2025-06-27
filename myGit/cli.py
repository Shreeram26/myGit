import argparse
from src import init,add,branch,checkout,status,commit,log 

def build_parser():
    parser=argparse.ArgumentParser(prog="myGit",description="Custon Git Implementation")

    subparsers=parser.add_subparsers(dest="command",required=True)

    init_parser=subparsers.add_parser("init",help="Initialize a new repository")
    init_parser.set_defaults(func=init.execute)

    add_parser=subparsers.add_parser("add",help="Add files to the staging area")
    add_parser.add_argument("files",nargs="+",help="Files to add")
    add_parser.set_defaults(func=add.execute)

    commit_parser=subparsers.add_parser("commit",help="Commit changes to the repository")
    commit_parser.add_argument("-m","--message",required=True,help="Commit message")
    commit_parser.set_defaults(func=commit.execute)

    status_parser=subparsers.add_parser("status",help="Show the status of the repository")
    status_parser.set_defaults(func=status.execute)

    checkout_parser = subparsers.add_parser("checkout", help="Switch branches or restore files")
    checkout_parser.add_argument("branch", help="Branch name")
    checkout_parser.set_defaults(func=checkout.execute)

    branch_parser = subparsers.add_parser("branch", help="List or create branches")
    branch_parser.add_argument("name", nargs="?", help="New branch name (optional)")
    branch_parser.set_defaults(func=branch.execute)

    log_parser = subparsers.add_parser("log", help="Show commit history")
    log_parser.set_defaults(func=log.execute)

    return parser

