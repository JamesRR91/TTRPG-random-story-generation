import random

def ttrpg_story_gen():
    story_template = "In a world of [setting], a group of [adjective] [noun] embark on a quest to [goal]. Along the way, they face [obstacle] and encounter [enemy]. The party is guided by a mysterious [guide] who reveals [plot twist]."

    parts_of_speech = ['setting', 'adjective', 'noun', 'goal', 'obstacle', 'enemy', 'guide', 'plot twist']

    user_inputs = {}

    for part in parts_of_speech:
        user_inputs[part] = input(f"Enter a {part}: ")

    filled_story = story_template
    for part, word in user_inputs.items():
        filled_story = filled_story.replace(f'[{part}]', word)

    print("\nYour TTRPG Story:\n")
    print(filled_story)

if __name__ == "__main__":
    ttrpg_story_gen()
