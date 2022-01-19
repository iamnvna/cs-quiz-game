while True:
    print("Welcome to the Computer Science Quiz!")
    ready = input("Okay, Ready? (Yes/No): ")

    if ready.lower() != "yes":
        quit()

    score = 0
    answer = input("What does CPU stand for?: ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does RAM stand for?: ")
    if answer.lower() == "random access memory":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does CLI stand for?: ")
    if answer.lower() == "command line interface":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does GUI stand for?: ")
    if answer.lower() == "graphical user interface":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    answer = input("What does ARP stand for?: ")
    if answer.lower() == "address resolution protocol":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")

    print("You got " + str(score) + " (" + str((score/5 * 100)) + "%) question(s) correct!")

    while True:
        again = str(input('Want to play again? (Yes/No): '))
        if again.lower() in ('yes', 'no'):
            break
        print("invalid input.")
    if again.lower() == 'yes':
        continue
    else:
        print("Goodbye!")
        quit()