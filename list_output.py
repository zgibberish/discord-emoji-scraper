import os
import sys

# You can change the output directory here for it to scan for downloaded servers
output_path = "./output"

if not os.path.exists(output_path):
    exit(sys.exit("output directory not found"))

servers = [f.path for f in os.scandir(output_path) if f.is_dir()]
servers.sort()
for x in servers:
    print(x, end=": ")
    with open(f"{x}/name.txt") as f:
        print(f.read())
