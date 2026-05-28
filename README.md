# rewindfs-lite

rewindfs-lite is a small snapshot-based file versioning tool for exploring rollback, file history tracking, and basic filesystem-style metadata handling.

It is a stripped-down prototype of a larger rewindfs idea, focused on the core pieces:
- snapshots
- version history
- rollback
- file hashing
- JSON metadata

## Features

- Snapshot creation for files
- File version history tracking
- Rollback to older versions
- SHA-256 hashing for integrity checks
- JSON-based metadata storage
- Simple command-line interface

## Why I built it

I wanted a small project that shows how versioned file recovery works without turning into a huge codebase.

This project is mainly about understanding:
- snapshot architecture
- rollback systems
- file versioning
- metadata indexing
- hashing and integrity checks
- filesystem-inspired design

## Tech Stack

- Python
- JSON
- File I/O
- hashlib
- shutil

## Repository Structure

```text
rewindfs-lite/
├── main.py
├── README.md
├── metadata.json
└── snapshots/
```

## Commands

Initialize the project:

```bash
python3 main.py init
```

Create a snapshot:

```bash
python3 main.py snapshot test.txt
```

View snapshot history:

```bash
python3 main.py history test.txt
```

Rollback to an older version:

```bash
python3 main.py rollback test.txt 1
```

## Example Workflow

```bash
echo "hello world" > test.txt

python3 main.py snapshot test.txt

echo "second version" > test.txt

python3 main.py snapshot test.txt

python3 main.py history test.txt

python3 main.py rollback test.txt 1
```

## How It Works

Each snapshot is stored as a versioned copy inside the `snapshots/` directory.

For every file, `metadata.json` stores:
- version number
- timestamp
- SHA-256 hash
- snapshot filename

Rollback restores a selected snapshot back into the working file.

## Demo

![rewindfs-lite demo](screenshots/demo.png)

## Future Improvements

- directory snapshots
- diff viewer
- automatic snapshots
- deduplication
- compressed snapshot storage
- ignore rules similar to `.gitignore`

## Status

Still experimenting with rollback and snapshot ideas.

## Author

Siddharth S Menon
