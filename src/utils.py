import pandas as pd

def load_data(file_path):
    """
    Charge les données du fichier .txt et retourne un DataFrame.
    """
    data = {"text": [], "label": []}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith("__label__1"):
                data["label"].append(0)
                data["text"].append(line.replace("__label__1", "").strip())
            elif line.startswith("__label__2"):
                data["label"].append(1)
                data["text"].append(line.replace("__label__2", "").strip())
    return pd.DataFrame(data)

