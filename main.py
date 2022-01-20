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
        print("Invalid input.")
    if again.lower() == 'yes':
        continue
    else:
        print("Goodbye!")
        quit()


## Commentary
"""
Line 1:
    Line 1 is a while loop that runs the program as long as the out put is true. For the output
    to be True however, the block of while loop between line 46 and 55 must equate to two. This 
    is one way of restarting a program after it has finished executing. Learnt it on StackOverflow.

Line 2:
    This is a basic print command that welcomes users to the game.
    
Line 3: 
    This line of code accepts an input (yes/no) from the user. The input determines whether the
    user wants to begin/continue play or quit the program.

Line 5-6:
    This block of code evaluates the response from the user from line 3 and performs the required
    action. The .lower() function appended to the variable converts the input type to lowercase
    to effectively match the code.

Line 8:
    A score global variable is created to hold the total score (correct answers) from the game.

Line 9-14 et al.:
    The variable answer is assigned the input from the question asked. If the input evaluates to
    the right answer in Line 10, the program prints 'Correct!' as indicated on line 11, and proceeds
    to add one to the score (Line 12). If the answer (user input) to the question evaluates to false,
    the program prints 'Incorrect!' as indicated on line 14. 

Line 44:
    Through the print statement and basic concatenation, the total score and percentage from the 
    game is printed out to the user. Note that all integers and float variable types are converted
    tp strings before concatenated in the print statement.
    
Line 46-55:
    This block of code collects user input (yes/no) to tell whether to close the game or run it
    once more. In line 48, the code evaluates the user input to either yes or no, and prints out 
    'Invalid input.' (Line 50) to anything apart from the two. The program proceeds to run if the
    user answers 'yes' but quits and prints out 'Goodbye!' if the user answers no. 
"""