# main.py
from cli import build_parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    args.func(args) if hasattr(args, "func") else parser.print_help()

if __name__ == "__main__":
    main()
