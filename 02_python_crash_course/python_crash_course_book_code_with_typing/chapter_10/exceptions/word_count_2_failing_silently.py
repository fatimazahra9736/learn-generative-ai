from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"the file {path} has about {num_words}")
file_names:list[str] = ["alice.txt","siddhartha.txt","moby_dick.txt"]
for file_name in file_names:
    path = Path(file_name)
    count_words(path)