import os

folder = "."

for name in os.listdir(folder):
    if name.endswith(".tmp"):
        print("temporary file:", name)
