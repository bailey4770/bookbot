from stats import get_num_words


def get_book_text(filepath: str):
    with open(filepath, "r") as file:
        content = file.read()
    return content


def main():
    frank_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frank_path)
    num_words = get_num_words(frankenstein_text)  # Print the first 500 characters
    print(f"Found {num_words} total words")


if __name__ == "__main__":
    main()
