from typing import Literal
from wonderwords import RandomWord


PartOfSpeech = Literal["noun", "verb", "adjective", "adverb"]


def generate_random_words(
    n_words: int,
    part_of_speech: PartOfSpeech | None = None,
) -> list[str]:
    rand_words = RandomWord()
    if part_of_speech:
        return rand_words.random_words(n_words, include_parts_of_speech=[part_of_speech])
    else:
        return rand_words.random_words(n_words)
