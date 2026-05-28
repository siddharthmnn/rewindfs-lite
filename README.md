# rewindfs-lite

rewindfs-lite is a lightweight snapshot-based file versioning tool inspired by Git, Time Machine, and snapshot-oriented filesystems such as ZFS.

The project explores how rollback systems and file history tracking work internally through a simplified command-line implementation.

Unlike the main rewindfs project, rewindfs-lite focuses only on the core concepts:

* snapshot creation
* file version tracking
* rollback and recovery
* metadata storage
* content hashing

## Features

* Create snapshots of files
* Track file version history
* Restore older file versions
* Store metadata using JSON
* Detect file state changes using SHA-256 hashing

## Project Goals

This project was built to better understand:

* filesystem concepts
* version control ideas
* rollback systems
* snapshot architecture
* metadata indexing
* hashing and file integrity

while keeping the implementation lightweight and easy to experiment with.

## Tech Stack

* Python
* JSON
* File I/O
* hashlib
* shutil

## Example Commands

```bash
python main.py init
python main.py snapshot test.txt
python main.py history test.txt
python main.py rollback test.txt 1
```

## Status

Currently under development.
