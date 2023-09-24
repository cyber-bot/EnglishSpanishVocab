import random

def read_vocabulary_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
    return [line.strip().lower().split(',') for line in lines]

def quiz_user(words, num_questions):
    random.shuffle(words)
    words = words[:num_questions]
    correct = 0
    total = len(words)
    missed_words = []

    for english, spanish in words:
        user_input = input(f"What is the Spanish translation of '{english}'? ").lower()
        if user_input == spanish:
            correct += 1
        else:
            missed_words.append((english, spanish))

    print(f"\nYou got {correct} out of {total} correct!")

    return missed_words

def write_missed_words(missed_words, output_file):
    with open(output_file, 'w') as file:
        for english, spanish in missed_words:
            file.write(f"{english},{spanish}\n")

def main():
    file_name = input("Enter the name of the vocabulary file (including extension): ")
    vocabulary = read_vocabulary_file(file_name)

    if vocabulary:
        num_questions = int(input("How many words would you like to be quizzed on? "))
        missed_words = quiz_user(vocabulary, num_questions)

        if missed_words:
            output_file = input("Enter the name of the file to write wrong answers (including extension): ")
            write_missed_words(missed_words, output_file)
            print(f"Missed words written to '{output_file}'")
        else:
            print("Congratulations! You got all words correct.")
    else:
        print(f"Could not read the file '{file_name}'")

if __name__ == "__main__":
    main()
