import argparse
import piexif

def main() -> None:
    parser = argparse.ArgumentParser(description="EXIF CLI tool")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # --- Read subcommand ---
    read_parser = subparsers.add_parser("read", help="Read EXIF data from files")
    read_parser.add_argument("files", nargs="+", help="Files to read EXIF from")

    # --- Delete subcommand ---
    delete_parser = subparsers.add_parser("delete", help="Delete EXIF data from files")
    delete_parser.add_argument("files", nargs="+", help="Files to delete EXIF from")

    # --- Modify subcommand ---
    modify_parser = subparsers.add_parser("modify", help="Modify EXIF data in files")
    modify_parser.add_argument("files", nargs="+", help="Files to modify")
    modify_parser.add_argument("--tag", required=True, help="EXIF tag to modify")
    modify_parser.add_argument("--value", required=True, help="New value for the tag")
    
    args = parser.parse_args()

    match args.command:
        case "read":
            print("Reading EXIF from:", args.files)
        case "delete":
            print("Deleting EXIF from:", args.files)
        case "modify":
            print(f"Modifying {args.tag} in {args.files} to {args.value}")



if __name__ == "__main__":
    main()