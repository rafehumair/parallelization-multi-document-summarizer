import os

def load_documents(folder_path):
    """Reads all .txt files from a folder and returns list of strings."""
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                docs.append(f.read())
    return docs
