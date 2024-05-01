print("    let's play a quiz!     ")

questions = [
    "What is the capital of Canada?: ",
    "What is the capital of Japan?: ",
    "What is the capital of Argentina?: "
]

# print(questions)

answers = ["Ottawa", "tokio", "Buenos Aires"]

answer = input(questions[0]).strip()
if answer.lower() == answers[0].lower():
    print("That's correct!")

    answer = input(questions[1]).strip()
    if answer.lower() == answers[1].lower():
        print("That's correct!")

        answer = input(questions[2]).strip()
        if answer.lower() == answers[2].lower():
            print("Correct! You passed the test.")

        else:
            print("That's false, you've failed the test.")

    else:
        print("That's false, you've failed the test.")

else:
    print("That's false, you've failed the test.")


