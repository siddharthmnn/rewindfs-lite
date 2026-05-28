import os
import sys
import json
import shutil
import hashlib
from datetime import datetime

SNAPSHOT_DIR = "snapshots"
METADATA_FILE = "metadata.json"


def load_metadata():

    if not os.path.exists(METADATA_FILE):
        return {}

    try:
        with open(METADATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except:
        return {}


def save_metadata(data):

    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


def ensure_initialized():

    os.makedirs(SNAPSHOT_DIR, exist_ok=True)

    if not os.path.exists(METADATA_FILE):
        save_metadata({})


def get_file_hash(filepath):

    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:

        while chunk := f.read(8192):
            sha256.update(chunk)

    return sha256.hexdigest()


def init():

    ensure_initialized()

    print("[+] rewindfs-lite initialized")


def snapshot(filepath):

    if not os.path.exists(filepath):
        print("[-] File not found")
        return

    ensure_initialized()

    metadata = load_metadata()

    filename = os.path.basename(filepath)

    if filename not in metadata:
        metadata[filename] = []

    version = len(metadata[filename]) + 1

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_hash = get_file_hash(filepath)

    snapshot_name = f"{filename}_v{version}"

    snapshot_path = os.path.join(
        SNAPSHOT_DIR,
        snapshot_name
    )

    shutil.copy2(filepath, snapshot_path)

    metadata[filename].append({
        "version": version,
        "timestamp": timestamp,
        "hash": file_hash,
        "snapshot": snapshot_name
    })

    save_metadata(metadata)

    print(f"[+] Snapshot saved: version {version}")


def history(filepath):

    metadata = load_metadata()

    filename = os.path.basename(filepath)

    if filename not in metadata:
        print("[-] No snapshot history found")
        return

    for entry in metadata[filename]:

        print(f"Version   : {entry.get('version', 'N/A')}")
        print(f"Timestamp : {entry.get('timestamp', 'N/A')}")
        print(f"Hash      : {entry.get('hash', 'N/A')}")
        print(f"Snapshot  : {entry.get('snapshot', 'N/A')}")
        print()


def rollback(filepath, version):

    metadata = load_metadata()

    filename = os.path.basename(filepath)

    if filename not in metadata:
        print("[-] No snapshot history found")
        return

    for entry in metadata[filename]:

        if entry["version"] == version:

            snapshot_path = os.path.join(
                SNAPSHOT_DIR,
                entry["snapshot"]
            )

            if not os.path.exists(snapshot_path):
                print("[-] Snapshot file missing")
                return

            shutil.copy2(snapshot_path, filepath)

            print(f"[+] Restored {filename} to version {version}")
            return

    print("[-] Version not found")


def help_menu():

    print("""
rewindfs-lite commands:

python3 main.py init
python3 main.py snapshot <file>
python3 main.py history <file>
python3 main.py rollback <file> <version>
""")


def main():

    if len(sys.argv) < 2:
        help_menu()
        return

    command = sys.argv[1]

    if command == "init":

        init()

    elif command == "snapshot":

        if len(sys.argv) != 3:
            help_menu()
            return

        snapshot(sys.argv[2])

    elif command == "history":

        if len(sys.argv) != 3:
            help_menu()
            return

        history(sys.argv[2])

    elif command == "rollback":

        if len(sys.argv) != 4:
            help_menu()
            return

        try:
            version = int(sys.argv[3])

        except ValueError:
            print("[-] Version must be a number")
            return

        rollback(sys.argv[2], version)

    else:
        help_menu()


if __name__ == "__main__":
    main()
