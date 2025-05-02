import os
import shutil

src_dir = "source_dir"
dest_dir = "destination_dir"
os.makedirs(dest_dir, exist_ok=True)

src_file = os.path.join(src_dir, "example.txt")
dest_file = os.path.join(dest_dir, "example.txt")

shutil.copy(src_file, dest_file)
print(f"File copied from {src_file} to {dest_file}.")

