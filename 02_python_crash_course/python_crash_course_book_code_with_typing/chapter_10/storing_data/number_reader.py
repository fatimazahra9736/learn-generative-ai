from pathlib import Path
import json

path = Path("numbers.json")
contents = path.read_text()
number = json.loads(contents)

print(number)