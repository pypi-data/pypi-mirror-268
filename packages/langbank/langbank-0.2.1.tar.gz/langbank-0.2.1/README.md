# LangBank

LangBank is a Python package for managing a word bank for language learning. It provides functionality for storing and retrieving words along with additional information such as timestamps and tags.

## Installation

```bash
pip install langbank
```

## Usage

### LangBank class

```python
from langbank import LangBank

# Initialize a LangBank instance
lb = LangBank()

# Add a word to the bank with optional tags
lb.add_word("hello", tags=["greeting", "basic"])

# Get all words in the bank
words = lb.get_all_words()

# Get all unique words in the bank
unique_words = lb.get_all_unique_words()

# Get words added in the past n days
recent_words = lb.get_words_from_past_n_days(7)

# Get words added today
todays_words = lb.get_todays_words()

# Get words by a specific tag
greeting_words = lb.get_words_by_tag("greeting")

# Get words added on a specific date
from datetime import date
words_on_date = lb.get_words_by_date(date(2021, 12, 31))

# Get the number of times a word has been added
occurrences = lb.occurences("hello")
```

### ReviewList class

```python
from langbank import ReviewList

# Initialize a ReviewList instance
rl = ReviewList()

# Set a new file path
rl.set_file_path("~/new_path/review_list.txt")

# Add a new word
rl.add_word("hello")

# Check if the review list is full
is_full = rl.is_full()

# Get the review list
review_list = rl.get_list()
```
