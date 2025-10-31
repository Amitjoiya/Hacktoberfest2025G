# favicon-generator.py
from PIL import Image
import sys
if len(sys.argv)<2: print("Usage: python favicon-generator.py source.png"); sys.exit(1)
img = Image.open(sys.argv[1]).convert("RGBA")
img = img.resize((64,64), Image.LANCZOS)
img.save("favicon.ico", format='ICO', sizes=[(64,64)])
print("favicon.ico created")
