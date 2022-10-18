from pathlib import Path


CUR_DIR = Path.cwd().resolve()   
DATA_DIR = CUR_DIR / "data"


if __name__ == "__main__":
    print(CUR_DIR)
    print(DATA_DIR)