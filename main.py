import stats


def get_book_text(filepath: str):
    with open(filepath, "r") as file:
        content = file.read()
    return content


def main():
    frank_path = "books/frankenstein.txt"
    frankenstein_text = get_book_text(frank_path)
    num_words = stats.get_num_words(frankenstein_text)  # Print the first 500 characters
    print(f"Found {num_words} total words")
    print(stats.count_unique_chars(frankenstein_text))


if __name__ == "__main__":
    main()
