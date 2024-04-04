import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(json_file):
    with open(json_file) as f:
        data = json.load(f)
    return data

# Function to get definition of a word
def get_definition(word, dictionary):
    word = word.lower()  # Normalize input to lower case
    if word in dictionary:
        return dictionary[word]
    else:
        # If word not found, try to suggest a similar word
        similar_words = difflib.get_close_matches(word, dictionary.keys())
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found."

# Main function
def main():
    dictionary = load_dictionary("dictionary.json")

    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        else:
            definition = get_definition(user_input, dictionary)
            print(definition)

if __name__ == "__main__":
    main()

 