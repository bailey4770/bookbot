from collections import defaultdict
from collections.abc import MutableMapping


def get_num_words(text: str) -> int:
    text_list = text.split()
    return len(text_list)


def count_unique_chars(text: str):
    unique_chars: MutableMapping[str, int] = defaultdict(int)

    for char in text:
        unique_chars[char.lower()] += 1

    return unique_chars


def sort_dict(d: MutableMapping[str, int]):
    return sorted(d.items(), reverse=True, key=lambda item: item[1])
