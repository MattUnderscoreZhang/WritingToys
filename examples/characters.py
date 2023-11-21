from ai_emotion.simple_emotion import PlutchikEmotion
import argparse

from writing_toys.characters import generate_character


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--prompt", help="Specify a starting prompt")
    parser.add_argument("-e", "--emotion_random", help="Add a random emotion during generation", action=argparse.BooleanOptionalAction)
    args = parser.parse_args()

    emotion = (
        PlutchikEmotion.random()
        if args.emotion_random
        else None
    )
    character = generate_character(
        starting_prompt=args.prompt,
        emotion=emotion,
    )
    print(character)
