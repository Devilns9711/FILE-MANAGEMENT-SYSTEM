# File Management System

A command-line based File Management System built with Python. Lets you create, read, write, search, and manage `.txt` files through a simple interactive menu — no external libraries required.

---

## Features

- Create, read, write, and append to files
- Search, replace, and delete specific text inside files
- Rename, copy, and delete files
- View detailed file info (size, created date, modified date, line/word/character count)
- Quick statistics view for any file
- Clear file contents without deleting the file
- All files stored in a `files/` folder placed next to `main.py`

---

## Project Structure

```
file-management-system/
│
├── main.py         ← Entry point, runs the app
├── files/          ← Auto-created folder where all .txt files are stored
└── README.md       ← This file
```

> The `files/` folder is created automatically on first run. You don't need to make it manually.

---

## Requirements

- Python 3.6 or higher
- No external packages needed (uses only built-in modules: `os`, `shutil`, `datetime`)

---

## How to Run

1. Download or clone the project
2. Open a terminal and navigate to the folder containing `main.py`

```bash
cd path/to/file-management-system
```

3. Run the program

```bash
python main.py
```

> On some systems you may need to use `python3` instead of `python`

---

## Menu Options

When you run the program, you'll see this menu:

```
============================================================
              FILE MANAGEMENT SYSTEM
============================================================
                      MAIN MENU
============================================================
  1.  Create File
  2.  Show Files
  3.  Read File
  4.  Write File
  5.  Append File
  6.  Search Text
  7.  Replace Text
  8.  Delete Text
  9.  Clear File
  10. Rename File
  11. Copy File
  12. Delete File
  13. File Info
  14. Statistics
  15. Exit
```

### Option Details

| Option | Name | What it does |
|--------|------|--------------|
| 1 | Create File | Creates a new empty `.txt` file |
| 2 | Show Files | Lists all `.txt` files in the `files/` folder |
| 3 | Read File | Displays the full content of a file |
| 4 | Write File | Overwrites a file with new content |
| 5 | Append File | Adds new content at the end of a file |
| 6 | Search Text | Counts how many times a word/phrase appears |
| 7 | Replace Text | Replaces all occurrences of a word/phrase |
| 8 | Delete Text | Removes all occurrences of a word/phrase |
| 9 | Clear File | Empties the file (keeps the file, deletes content) |
| 10 | Rename File | Renames an existing file |
| 11 | Copy File | Makes a copy of a file with a new name |
| 12 | Delete File | Permanently deletes a file |
| 13 | File Info | Shows size, dates, line count, word count, character count |
| 14 | Statistics | Quick view of line, word, and character count |
| 15 | Exit | Closes the program |

---

## How to Select a File

Whenever a menu option asks you to select a file, you can either:

- **Type the number** shown next to the file name (e.g. `1`)
- **Type the file name** directly (e.g. `notes` or `notes.txt`)
- **Type `0`** to cancel and go back to the main menu

---

## Usage Examples

### Creating a file
```
Enter choice: 1
Enter file name (without .txt): notes
File 'notes.txt' created successfully.
```

### Writing content to a file
```
Enter choice: 4
[Select your file]
Type your content (type END on a new line to save)

Hello, this is my first line.
This is the second line.
END

File written successfully.
```

### Searching for text
```
Enter choice: 6
[Select your file]
Enter text to search: hello
'hello' found 3 time(s).
```

### Replacing text
```
Enter choice: 7
[Select your file]
Enter text to replace: hello
Enter new text: hi
Replaced 3 occurrence(s).
```

---

## Notes

- All files are saved as `.txt` format only
- The `files/` folder is always created next to `main.py`, regardless of where you run the script from
- Write mode (option 4) **overwrites** the entire file — use Append (option 5) to add content without losing existing data
- Delete File (option 12) asks for confirmation before permanently removing a file
- Clear File (option 9) also asks for confirmation before wiping content

---

## Modules Used

| Module | Purpose |
|--------|---------|
| `os` | File and directory operations |
| `shutil` | Copying files |
| `datetime` | Reading file creation and modification timestamps |

---

## Author

Made by Nirmal — BCA 2nd Semester Project
