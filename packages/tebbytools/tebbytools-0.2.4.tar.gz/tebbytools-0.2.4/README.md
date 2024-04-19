# tebbytools

tebbytools is a simple Python package that provides tools for language learning.

## Installation

```bash
pip install tebbytools
```

## Usage

### Word bank

A `WordBank` manages a json file that contains a list of words you've encountered.
You can add words to the bank and query them in various ways.

```python
from tebbytools import WordBank

# Initialize a WordBank instance
wb = WordBank(file_path="path/to/your/word_bank.json")

# Set a new file path
wb.set_file_path("~/new_path/word_bank.json")

# Add a word to the bank with optional tags
wb.add_word("hello", tags=["greeting", "basic"])

# Get all words in the bank
words = wb.get_all_words()

# Get all unique words in the bank
unique_words = wb.get_all_unique_words()

# Get words added in the past n days
recent_words = wb.get_words_from_past_n_days(7)

# Get words added today
todays_words = wb.get_todays_words()

# Get words by a specific tag
greeting_words = wb.get_words_by_tag("greeting")

# Get words added on a specific date
from datetime import date
words_on_date = wb.get_words_by_date(date(2021, 12, 31))

# Get the number of times a word has been added
occurrences = wb.occurences("hello")
```

### Review list

A `ReviewList` manages a txt file that contains a list of words that you want to review.
You can add words to the list. When the list if full, you can get the words and review them.
If you try add a word past the list's capacity, the list will be cleared, and the new word will be added to the empty list.

```python
from tebbytools import ReviewList

# Initialize a ReviewList instance
rl = ReviewList(file_path="path/to/your/review_list.txt", size=5)

# Set a new file path
rl.set_file_path("~/new_path/review_list.txt")

# Add a new word
rl.add_word("hello")

# Check if the review list is full
is_full = rl.is_full()

# Get the review list
review_list = rl.get_list()

# Clear the review list
rl.clear_list()
```
