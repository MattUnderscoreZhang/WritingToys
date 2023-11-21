from ai_emotion.simple_emotion import PlutchikEmotion

from writing_toys.characters import generate_character
from writing_toys.settings import generate_setting


if __name__ == "__main__":
    starting_prompt = "Refugees in the bowels of a massive ship"
    emotion = PlutchikEmotion(
        joy=0.0,
        sadness=1.0,
        trust=0.0,
        disgust=0.5,
        fear=1.0,
        anger=0.0,
        surprise=0.0,
        anticipation=0.8,
    )
    setting = generate_setting(
        starting_prompt=starting_prompt,
        emotion=emotion,
    )
    print(setting)
    print()
    character = generate_character(
        starting_prompt=setting,
        emotion=emotion,
    )
    print(character)
