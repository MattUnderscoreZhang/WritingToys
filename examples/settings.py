import sys

from writing_toys.settings import generate_setting


if __name__ == "__main__":
    starting_prompt = (
        None
        if len(sys.argv) < 2
        else " ".join(sys.argv[1:])
    )
    setting = generate_setting(starting_prompt)
    print(setting)
