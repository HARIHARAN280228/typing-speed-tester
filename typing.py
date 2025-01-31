import time
import random
SENTENCES = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a great programming language for beginners and experts alike.",
    "Typing speed tests can help improve your typing accuracy and speed.",
    "This is an intermediate level project in Python programming.",
    "Practice makes perfect, especially when it comes to coding and typing."
]

def get_random_sentence():
    return random.choice(SENTENCES)

def calculate_speed_and_accuracy(start_time, end_time, user_input, original_sentence):
    time_taken = end_time - start_time  # in sec
    words_count = len(original_sentence.split())
    typing_speed = (words_count / time_taken) * 60  
    
    original_words = original_sentence.split()
    user_words = user_input.split()
    matches = sum(1 for ow, uw in zip(original_words, user_words) if ow == uw)
    accuracy = (matches / len(original_words)) * 100

    return typing_speed, accuracy, time_taken

def main():
    print("Welcome to the Typing Speed Test!")
    print("You will be given a random sentence to type.")
    print("Type it as quickly and accurately as you can.")
    print()

    # Get a random sentence
    sentence = get_random_sentence()
    print(f"Your sentence is:\n{sentence}")
    print()

    # Start the timer
    input("Press Enter when you are ready to start...")
    start_time = time.time()

    # Get user input
    user_input = input("\nStart typing: ")
    end_time = time.time()

    # Calculate results
    typing_speed, accuracy, time_taken = calculate_speed_and_accuracy(
        start_time, end_time, user_input, sentence
    )

    # Display results
    print("\nTest Results:")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Typing Speed: {typing_speed:.2f} words per minute")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()

