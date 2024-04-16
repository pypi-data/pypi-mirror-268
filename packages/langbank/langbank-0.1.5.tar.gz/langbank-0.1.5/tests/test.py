import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.langbank import LangBank

TEST_BANK_JSON = "tests/data/bank.json"


if __name__ == "__main__":
    with open(TEST_BANK_JSON, "w") as f:
        f.write("[]")

    bank = LangBank(file_path=TEST_BANK_JSON)
    bank.add_word("hello", tags=["greeting", "english"])
    bank.add_word("hola", tags=["greeting", "spanish"])
