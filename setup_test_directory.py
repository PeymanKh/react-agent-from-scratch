"""
Setup Test Directory

This script creates a messy test directory that you can inspect before running the agent.
Use this to see the "before" state, then run demo.py to see how the agent organizes it.

Usage:
    python setup_test_directory.py --scenario personal
    python setup_test_directory.py --scenario developer
"""
import argparse
from pathlib import Path

from src.config.logging_config import get_logger
from src.utils import initialize_personal_directory, initialize_developer_directory

logger = get_logger(__name__)


def list_directory_contents(directory: str = "working_directory") -> None:
    """
    List all files in the working directory in a tree-like format.

    Args:
        directory: The directory to list (default: "working_directory")
    """
    dir_path = Path(directory)

    if not dir_path.exists():
        print(f"Directory '{directory}' does not exist.")
        return

    print(f"\nContents of '{directory}':")
    print("=" * 60)

    files = sorted(dir_path.rglob("*"))

    if not files:
        print("  (empty directory)")
        return

    for file_path in files:
        if file_path.is_file():
            relative = file_path.relative_to(dir_path)
            indent = "  " * (len(relative.parts) - 1)
            print(f"{indent} {relative}")
        elif file_path.is_dir() and file_path != dir_path:
            relative = file_path.relative_to(dir_path)
            indent = "  " * (len(relative.parts) - 1)
            print(f"{indent} {relative}/")

    file_count = sum(1 for f in files if f.is_file())
    dir_count = sum(1 for f in files if f.is_dir())
    print("=" * 60)
    print(f"Total: {file_count} files, {dir_count} directories\n")


def main():
    """Main function to setup test directories."""
    parser = argparse.ArgumentParser(
        description="Setup a messy test directory for the ReAct agent to organize",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python setup_test_directory.py --scenario personal
  python setup_test_directory.py --scenario developer
        """
    )

    parser.add_argument(
        "--scenario",
        type=str,
        choices=["personal", "developer"],
        required=True,
        help="Choose which test scenario to setup"
    )

    args = parser.parse_args()

    # Initialize the appropriate test directory
    print(f"\nSetting up '{args.scenario}' test directory...\n")

    try:
        if args.scenario == "personal":
            initialize_personal_directory()
            print("\nThis directory contains:")
            print("   - invoice_2024.pdf")
            print("   - vacation_photo.jpg")
            print("   - project_proposal.docx")
            print("   - setup.exe")
            print("   - budget_spreadsheet.xlsx")
            print("   - family_video.mp4")
            print("   - tax_return_2023.pdf")
            print("   - recipes.pdf")
            print("   - screenshot_12345.png")
            print("   - thesis_final_FINAL_v2.docx")
            print("   - presentation.pptx")
            print("   - random_notes.txt")
            print("   - contract_signed.pdf")
            print("   - game_installer.zip")
            print("   - backup_code.py")


        else:  # developer
            initialize_developer_directory()
            print("\nThis directory contains:")
            print("   - main.py")
            print("   - test.py")
            print("   - requirements.txt")
            print("   - README.md")
            print("   - config.json")
            print("   - old_version.py")
            print("   - todo.txt")
            print("   - architecture_diagram.png")
            print("   - api_documentation.pdf")
            print("   - database_schema.sql")
            print("   - test_results.csv")
            print("   - logo.svg")
            print("   - screenshot_bug.png")
            print("   - credentials.env")


        print(f"\nLocation: /working_directory")

        print("\nNext steps:")
        print("   1. Explore the directory: cd working_directory && ls")
        print(f"   2. Run the agent: python demo.py")
        print("   3. Compare the organized result!\n")

    except Exception as e:
        logger.error(f"Failed to setup test directory: {e}")
        print(f"Error: {e}")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())