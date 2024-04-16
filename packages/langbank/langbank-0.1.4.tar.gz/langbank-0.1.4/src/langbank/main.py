import json
import os
from datetime import datetime

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"


class LangBank:
    """
    A class for managing a word bank for language learning.
    """

    def __init__(self, file_path=None):
        """
        Initialize LangBank with an optional file path.
        If no file path is provided, a default one will be used.
        """
        if file_path is None:
            # Default file path: ~/langbank/bank.json
            self.file_path = os.path.expanduser("~/langbank/bank.json")
        else:
            self.file_path = file_path

        self.setup_bank()

    def set_file_path(self, file_path):
        """
        Set the file path for the word bank.
        """
        self.file_path = file_path

    def setup_bank(self):
        """
        Create the word bank file and parent directories if they do not exist.
        """
        # Create parent directories if they do not exist
        parent_dir = os.path.dirname(self.file_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)

        # Create the word bank file if it does not exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                f.write("[]")

    def get_bank(self):
        """
        Get the contents of the word bank from the JSON file.
        Returns:
            The word bank (list).
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(self.file_path, "r") as f:
                bank = json.load(f)
                # Parse datetime strings into datetime objects
                for item in bank:
                    if "datetime" in item:
                        item["datetime"] = datetime.strptime(
                            item["datetime"], DATETIME_FORMAT
                        )
                return bank
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.file_path}' not found.")

    def write_bank(self, bank):
        """
        Write the contents of the word bank to the JSON file.
        Args:
            bank: The word bank (list) to write.
        """
        # Convert datetime objects to strings
        for item in bank:
            if "datetime" in item:
                item["datetime"] = item["datetime"].strftime(DATETIME_FORMAT)

        # Write bank to JSON file
        with open(self.file_path, "w") as f:
            json.dump(bank, f, indent=4)

    def add_word(self, word, tags=None):
        """
        Add a new word to the wordbank
        Args:
            word: the word to add
            tags: a list of string tags
        """
        if tags is None:
            tags = []

        dt = datetime.now()
        entry = {"word": word, "datetime": dt.strftime(DATETIME_FORMAT), "tags": tags}
        bank = self.get_bank()
        bank.append(entry)
        self.write_bank(bank)

    def get_words_from_past_n_days(self, n=0):
        """
        Get a list of all the words added in the past n days, where n=0 will return the words added today
        """
        bank = self.get_bank()
        today = datetime.now().date()
        words = []
        for entry in bank:
            if (today - entry["datetime"].date()).days <= n:
                words.append(entry["word"])

        return words

    def get_todays_words(self):
        """
        Get the list of words added today
        """
        return self.get_words_from_past_n_days(0)

    def get_words_by_tag(self, tag):
        """
        Get a list of all the words with a specific tag
        """
        bank = self.get_bank()
        words = []
        for entry in bank:
            if tag in entry["tags"]:
                words.append(entry["word"])

        return words

    def get_words_by_date(self, date):
        """
        Get a list of all the words added on a specific date
        """
        bank = self.get_bank()
        words = []
        for entry in bank:
            if entry["datetime"].date() == date:
                words.append(entry["word"])

        return words

    def occurences(self, word):
        """
        Get the number of times a word has been added to the bank
        """
        bank = self.get_bank()
        count = 0
        for entry in bank:
            if entry["word"] == word:
                count += 1

        return count
