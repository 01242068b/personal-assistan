import random

# Function to collect user information


def collect_user_info():
    # Ask the important questions first
    answers = {}

    # Ask name and age
    name = input("What is your name? ")
    age = input("How old are you? ")

    answers["name"] = name
    answers["age"] = age

    # Extra questions to choose from
    extra_questions = [
        "What is your favorite color? ",
        "Where do you live? ",
        "Which Senior High School did you attend? ",
        "Which soccer team do you support? "
    ]

    extra_keys = ["color", "city", "school", "team"]

    # Randomly choose how many extra questions to ask (between 2 and 4)
    num_extra = random.randint(2, 4)

    # Make a list of random positions
    positions = random.sample([0, 1, 2, 3], num_extra)

    for i in positions:
        answer = input(extra_questions[i])
        key = extra_keys[i]
        answers[key] = answer

    return answers


# Show the summary of answers
def show_summary(answers):
    print("\n--- Summary of Your Information ---")
    print("Hello " + answers["name"] + "!")

    print("You are " + answers["age"] + " years old.")

    # Check and print optional answers
    if "color" in answers:
        print("Your favorite color is " + answers["color"] + ".")
    if "city" in answers:
        print("You live in " + answers["city"] + ".")
    if "school" in answers:
        print("You went to " + answers["school"] + " SHS.")
    if "team" in answers:
        print("You support " + answers["team"] + ".")


# Save the answers to a file
def save_to_file(answers, rating):
    filename = answers["name"] + ".txt"

    file = open(filename, "w")
    file.write("User Info Summary\n")
    file.write("------------------\n")

    for key in answers:
        file.write(key + ": " + answers[key] + "\n")

    file.write("Rating: " + str(rating) + "/5\n")
    file.close()

    print("Saved your summary to " + filename)


# Main function
def run_assistant():
    while True:
        info = collect_user_info()
        show_summary(info)

        save = input("\nDo you want to save your summary? (yes/no): ")
        if save.lower() == "yes":
            while True:
                rate = input("Rate this assistant from 1 to 5: ")
                if rate.isdigit():
                    rate_num = int(rate)
                    if rate_num >= 1 and rate_num <= 5:
                        break
                    else:
                        print("Enter a number from 1 to 5.")
                else:
                    print("Please enter a number.")

            save_to_file(info, rate_num)

        again = input("\nDo you want to try again? (yes/no): ")
        if again.lower() != "yes":
            print("Thanks for using the assistant!")
            break


# Run the program
run_assistant()
