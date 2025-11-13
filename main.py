import stats
import sys


def get_book_text(filepath: str):
    with open(filepath, "r") as file:
        content = file.read()
    return content


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    text = get_book_text(path_to_book)
    num_words = stats.get_num_words(text)  # Print the first 500 characters
    unique = stats.count_unique_chars(text)
    unique = stats.sort_dict(unique)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, num in unique:
        if not char.isalpha():
            continue
        print(f"{char}: {num}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
