import os

DEFAULT_FILE_PATH = os.path.expanduser("~/langbank/review_list.txt")


class ReviewList:
    """A class for managing a list of review items."""

    def __init__(self, file_path=None, size=10):
        """
        Initialize ReviewList with an optional file path and size.
        If no file path is provided, a default one will be used.
        """
        if file_path is None:
            # Default file path: ~/reviewlist/reviews.json
            self.file_path = DEFAULT_FILE_PATH
        else:
            self.file_path = file_path
        self.size = size
        self.setup_list()

    def set_file_path(self, file_path):
        """
        Set the file path for the review list.
        """
        self.file_path = file_path

    def setup_list(self):
        """
        Create the review list file and parent directories if they do not exist.
        """
        # Create parent directories if they do not exist
        parent_dir = os.path.dirname(self.file_path)
        if not os.path.exists(parent_dir):
            os.makedirs(parent_dir)
        # Create the review list file if it does not exist
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                f.write("")

    def get_list(self):
        """
        Get the contents of the review list from the text file.
        Returns:
            The review list (list).
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        try:
            with open(self.file_path, "r") as f:
                return f.read().splitlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{self.file_path}' not found.")

    def write_list(self, review_list):
        """
        Write the review list to the text file.
        Args:
            review_list: The review list to write to the file.
        """
        with open(self.file_path, "w") as f:
            for item in review_list:
                f.write(f"{item}\n")

    def clear_list(self):
        """
        Clear the review list.
        """
        with open(self.file_path, "w") as f:
            f.write("")

    def is_full(self):
        """
        Check if the review list is full.
        Returns:
            True if the review list is full, False otherwise.
        """
        review_list = self.get_list()
        return len(review_list) >= self.size

    def add_word(self, word):
        """
        Add a word to the review list.
        Args:
            word: The word to add to the review list.
        """
        if self.is_full():
            self.clear_list()
        review_list = self.get_list()
        review_list.append(word)
        self.write_list(review_list)
