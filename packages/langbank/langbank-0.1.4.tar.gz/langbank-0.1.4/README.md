# LangBank

LangBank is a Python package for managing a word bank for language learning. It provides functionality for storing and retrieving words along with additional information such as timestamps and tags.

## Installation

```bash
pip install langbank
```

## Usage

```python
from langbank import LangBank

# Initialize LangBank with optional file path
word_bank = LangBank(file_path="path/to/your/bank.json")

# Add a word to the word bank
word_bank.add_word("hello", tags=["english", "greeting"])

# Retrieve words added today
todays_words = word_bank.get_todays_words()
print("Today's words:", todays_words)
```
