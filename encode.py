offset = 0

# remove any current addictions beyond the EOF
with open('stegosaurus.jpeg', 'r+b') as fi:
    content = fi.read()
    offset = content.index(bytes.fromhex('FFD9'))+2
    fi.seek(offset)
    fi.truncate()

with open("payload/payload.py","rb") as p, open("stegosaurus.jpeg","ab") as src:
    src.write(p.read())