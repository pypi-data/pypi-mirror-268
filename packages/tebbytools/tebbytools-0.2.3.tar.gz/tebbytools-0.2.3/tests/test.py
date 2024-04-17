import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.tebbytools import ReviewList, WordBank

TEST_BANK_JSON = "tests/data/bank.json"
TEST_REVIEW_LIST_TXT = "tests/data/review_list.txt"

if __name__ == "__main__":
    with open(TEST_BANK_JSON, "w") as f:
        f.write("[]")

    bank = WordBank(file_path=TEST_BANK_JSON)
    bank.add_word("hello", tags=["greeting", "english"])
    bank.add_word("hola", tags=["greeting", "spanish"])

    print("all words: ", bank.get_all_words())
    print("today's words", bank.get_todays_words())

    review_list = ReviewList(file_path=TEST_REVIEW_LIST_TXT, size=3)
    review_list.add_word("hello")
    review_list.add_word("hola")
    review_list.add_word("bonjour")

    print("review list: ", review_list.get_list())

    review_list.add_word("ciao")

    print("review list: ", review_list.get_list())
