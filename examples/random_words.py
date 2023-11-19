from writing_toys.random_words import generate_random_words


if __name__ == "__main__":
    words = generate_random_words(3)
    print(words)

    words = generate_random_words(
        n_words=5,
        part_of_speech="verb",
    )
    print(words)

    words = generate_random_words(
        n_words=2,
        part_of_speech="adjective",
    )
    print(words)

    words = generate_random_words(
        n_words=2,
        part_of_speech="noun",
    )
    print(words)
