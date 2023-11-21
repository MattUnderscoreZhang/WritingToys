from rich import print
import sys

from writing_toys.critic import criticize_writing
from writing_toys.edit import edit
from writing_toys.settings import generate_setting


if __name__ == "__main__":
    starting_prompt = (
        None
        if len(sys.argv) < 2
        else " ".join(sys.argv[1:])
    )
    setting = generate_setting(starting_prompt)
    print(setting)

    print("\nCriticizing...\n")
    criticism = criticize_writing(setting)
    print(criticism)

    print("\nEditing...\n")
    rewritten_setting = edit(setting, criticism)
    print(rewritten_setting)
