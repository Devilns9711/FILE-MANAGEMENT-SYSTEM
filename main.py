# ============================================================
#              FILE MANAGEMENT SYSTEM
# ============================================================

import os
import shutil
from datetime import datetime

# ------------------------------------------------------------
# PROJECT FOLDER SETUP
# ------------------------------------------------------------

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")

if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)


# ------------------------------------------------------------
# UTILITY FUNCTIONS
# ------------------------------------------------------------

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\nPress Enter to continue...")


def get_full_path(filename):
    return os.path.join(BASE_DIR, filename)


# ------------------------------------------------------------
# FILE LISTING
# ------------------------------------------------------------

def list_files():
    try:
        files = [f for f in os.listdir(BASE_DIR) if f.endswith(".txt")]
        return sorted(files)
    except Exception as e:
        print("Error reading directory:", e)
        return []


def show_files():
    files = list_files()

    if not files:
        print("\nNo files found.")
        return []

    print("\nAvailable Files:\n")

    for i, f in enumerate(files, 1):
        print(f"{i}. {f}")

    return files


# ------------------------------------------------------------
# FILE SELECTION
# ------------------------------------------------------------

def select_file():
    files = show_files()

    if not files:
        pause()
        return None

    print("\n0. Cancel")

    choice = input("\nSelect file (number or name): ").strip()

    if choice == "0":
        return None

    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(files):
            return get_full_path(files[idx])
        else:
            print("Invalid selection.")
            pause()
            return None

    if not choice.endswith(".txt"):
        choice += ".txt"

    full_path = get_full_path(choice)

    if os.path.exists(full_path):
        return full_path

    print("File not found.")
    pause()
    return None


# ------------------------------------------------------------
# HEADER UI
# ------------------------------------------------------------

def header(title):
    clear_screen()
    print("=" * 60)
    print("           FILE MANAGEMENT SYSTEM".center(60))
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


# ------------------------------------------------------------
# MAIN MENU
# ------------------------------------------------------------

def menu():
    header("MAIN MENU")

    print("  1.  Create File")
    print("  2.  Show Files")
    print("  3.  Read File")
    print("  4.  Write File")
    print("  5.  Append File")
    print("  6.  Search Text")
    print("  7.  Replace Text")
    print("  8.  Delete Text")
    print("  9.  Clear File")
    print("  10. Rename File")
    print("  11. Copy File")
    print("  12. Delete File")
    print("  13. File Info")
    print("  14. Statistics")
    print("  15. Exit")

    return input("\nEnter choice: ").strip()


# ------------------------------------------------------------
# CREATE FILE
# ------------------------------------------------------------

def create_file():
    header("CREATE FILE")

    name = input("Enter file name (without .txt): ").strip()

    if name == "":
        print("Filename cannot be empty.")
        pause()
        return

    filename = name + ".txt"
    path = get_full_path(filename)

    try:
        if os.path.exists(path):
            print("File already exists.")
        else:
            with open(path, "w") as f:
                f.write("")
            print(f"File '{filename}' created successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# READ FILE
# ------------------------------------------------------------

def read_file():
    header("READ FILE")

    path = select_file()
    if path is None:
        return

    try:
        with open(path, "r") as f:
            content = f.read()

        print("\n--- FILE CONTENT ---\n")

        if content.strip() == "":
            print("File is empty.")
        else:
            print(content)

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# WRITE FILE (OVERWRITE)
# ------------------------------------------------------------

def write_file():
    header("WRITE FILE (OVERWRITE)")

    path = select_file()
    if path is None:
        return

    print("\nType your content (type END on a new line to save)\n")

    lines = []

    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    try:
        with open(path, "w") as f:
            f.write("\n".join(lines))

        print("\nFile written successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# APPEND FILE
# ------------------------------------------------------------

def append_file():
    header("APPEND FILE")

    path = select_file()
    if path is None:
        return

    print("\nType content to append (type END to finish)\n")

    lines = []

    while True:
        line = input()
        if line.upper() == "END":
            break
        lines.append(line)

    try:
        with open(path, "a") as f:
            if os.path.getsize(path) > 0:
                f.write("\n")
            f.write("\n".join(lines))

        print("\nData appended successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# SEARCH TEXT
# ------------------------------------------------------------

def search_text():
    header("SEARCH TEXT")

    path = select_file()
    if path is None:
        return

    word = input("Enter text to search: ").strip()

    try:
        with open(path, "r") as f:
            content = f.read()

        count = content.lower().count(word.lower())

        if count > 0:
            print(f"\n'{word}' found {count} time(s).")
        else:
            print("\nText not found.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# REPLACE TEXT
# ------------------------------------------------------------

def replace_text():
    header("REPLACE TEXT")

    path = select_file()
    if path is None:
        return

    old = input("Enter text to replace: ")
    new = input("Enter new text: ")

    try:
        with open(path, "r") as f:
            content = f.read()

        count = content.count(old)

        if count == 0:
            print("\nText not found.")
            pause()
            return

        content = content.replace(old, new)

        with open(path, "w") as f:
            f.write(content)

        print(f"\nReplaced {count} occurrence(s).")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# DELETE TEXT
# ------------------------------------------------------------

def delete_text():
    header("DELETE TEXT")

    path = select_file()
    if path is None:
        return

    text = input("Enter text to delete: ")

    try:
        with open(path, "r") as f:
            content = f.read()

        count = content.count(text)

        if count == 0:
            print("\nText not found.")
            pause()
            return

        content = content.replace(text, "")

        with open(path, "w") as f:
            f.write(content)

        print(f"\nDeleted {count} occurrence(s).")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# CLEAR FILE
# ------------------------------------------------------------

def clear_file():
    header("CLEAR FILE")

    path = select_file()
    if path is None:
        return

    confirm = input("Are you sure? (y/n): ")

    if confirm.lower() != "y":
        print("\nCancelled.")
        pause()
        return

    try:
        with open(path, "w") as f:
            pass

        print("\nFile cleared successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# RENAME FILE
# ------------------------------------------------------------

def rename_file():
    header("RENAME FILE")

    path = select_file()
    if path is None:
        return

    new_name = input("Enter new file name (without .txt): ").strip()

    if new_name == "":
        print("Invalid name.")
        pause()
        return

    new_path = get_full_path(new_name + ".txt")

    try:
        os.rename(path, new_path)
        print("\nFile renamed successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# COPY FILE
# ------------------------------------------------------------

def copy_file():
    header("COPY FILE")

    path = select_file()
    if path is None:
        return

    new_name = input("Enter copy file name (without .txt): ").strip()

    if new_name == "":
        print("Invalid name.")
        pause()
        return

    new_path = get_full_path(new_name + ".txt")

    try:
        shutil.copy(path, new_path)
        print("\nFile copied successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# DELETE FILE
# ------------------------------------------------------------

def delete_file():
    header("DELETE FILE")

    path = select_file()
    if path is None:
        return

    confirm = input("Are you sure? (y/n): ")

    if confirm.lower() != "y":
        print("\nCancelled.")
        pause()
        return

    try:
        os.remove(path)
        print("\nFile deleted successfully.")

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# FILE INFORMATION
# ------------------------------------------------------------

def file_info():
    header("FILE INFORMATION")

    path = select_file()
    if path is None:
        return

    try:
        size = os.path.getsize(path)
        created = datetime.fromtimestamp(os.path.getctime(path))
        modified = datetime.fromtimestamp(os.path.getmtime(path))

        with open(path, "r") as f:
            content = f.read()

        lines = content.splitlines()
        words = len(content.split())
        chars = len(content)

        print("\n--- FILE DETAILS ---")
        print("Size      :", size, "bytes")
        print("Created   :", created)
        print("Modified  :", modified)
        print("Lines     :", len(lines))
        print("Words     :", words)
        print("Characters:", chars)

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# STATISTICS
# ------------------------------------------------------------

def statistics():
    header("FILE STATISTICS")

    path = select_file()
    if path is None:
        return

    try:
        with open(path, "r") as f:
            content = f.read()

        print("\n--- QUICK STATS ---")
        print("Lines     :", len(content.splitlines()))
        print("Words     :", len(content.split()))
        print("Characters:", len(content))

    except Exception as e:
        print("Error:", e)

    pause()


# ------------------------------------------------------------
# MENU HANDLER
# ------------------------------------------------------------

def handle_choice(choice):

    if choice == "1":
        create_file()
    elif choice == "2":
        header("SHOW FILES")
        show_files()
        pause()
    elif choice == "3":
        read_file()
    elif choice == "4":
        write_file()
    elif choice == "5":
        append_file()
    elif choice == "6":
        search_text()
    elif choice == "7":
        replace_text()
    elif choice == "8":
        delete_text()
    elif choice == "9":
        clear_file()
    elif choice == "10":
        rename_file()
    elif choice == "11":
        copy_file()
    elif choice == "12":
        delete_file()
    elif choice == "13":
        file_info()
    elif choice == "14":
        statistics()
    else:
        print("\nInvalid choice! Please enter a number between 1 and 15.")
        pause()


# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------

def main():
    while True:
        choice = menu()

        if choice == "15":
            header("GOODBYE")
            print("\nThank you for using File Management System\n")
            break
        else:
            handle_choice(choice)


# ------------------------------------------------------------

if __name__ == "__main__":
    main()
