"""
high_score.py for Python 3
Demo of how to save a list of high scores in a JSON file.
"""

import json

JSON_FILE_NAME = 'scores.json'
MAX_SAVED_RECORDS = 5


def main():
    """Program entry point"""

    # Read the saved score record list from a file.
    try:
        with open(JSON_FILE_NAME, 'r') as json_file:
            score_record_list = json.load(json_file)
    except FileNotFoundError:
        score_record_list = []

    # Ask the user for their name and score
    name = input('Enter your name: ')
    score = int(input('Enter your score: '))

    # Save the user's response in a dictionary (score_record)
    # Using a dictionary rather than a custom class allows for easier JSON serialization.
    score_record = {'name': name, 'score': score}

    # Add score_record to the previous retrieved score record list
    score_record_list.append(score_record)

    # Sort the list by score.
    score_record_list.sort(key=lambda sr: sr['score'], reverse=True)

    # Only save the top scores (up to MAX_SAVED_RECORDS)
    score_record_list = score_record_list[:MAX_SAVED_RECORDS]

    # Show the top scores.
    print('\nThe top scores are:')
    for sr in score_record_list:
        print(f"{sr['name']} {sr['score']}")

    # Write the score list to the file.
    with open(JSON_FILE_NAME, 'w') as json_file:
        json.dump(score_record_list, json_file)


# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
