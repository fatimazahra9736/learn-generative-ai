from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()
lines = contents.splitlines()
pi_string = ""
for line in lines:
    pi_string += line

birthday = input("Enter your birthday in the form")
if birthday in pi_string:
    print("Your birthday appeare in the first million digits of pi")
else:
    print("Your birthday does not appeare in the first million digits of pi")
