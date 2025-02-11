"""
Project Name: Final_CSI1320Jeopardy.py
Authors: Dani Romaya & Joshua Mabanglo
Date: 12/3/2023
Purpose of Program: This program is a 16-question, Jeopardy-style simulation for CSI 1320: Intro to Python & Unix.
"""

def main():
    """The main method"""

    # - global variables:
    global nextRound  # counter to keep track of round number
    nextRound = 1

    global score  # dictionary of player scores 
    score={"player 1":"0","player 2":"0"}

    global diction  # dictionary to store/ call subjects
    diction = {1:"Functions",
               2:"Data Structures",
               3:"Number Types",
               4:"Strings, Loops, and TextFiles"}

    global dictionTwo  # dictionary to store/ call available point values for each subject
    dictionTwo = {diction[1]:"1 2 3 4",
                  diction[2]:"1 2 3 4",
                  diction[3]:"1 2 3 4",
                  diction[4]:"1 2 3 4"}   

    # - Write questions to files
    function=open("Functions", "w")  # "Functions" questions
    function.write("What command is used to define a function?"+"\n"
                   +"What are some examples of higher order functions?"+"\n"
                   +"Could there be more than one parameter when defining a function?"+"\n"
                   +"To stop an infinite recursion with a recursive function, what must a programmer add to prevent the outcome?"+"\n")
    function.close()
    
    numbertypes=open("Number Types", "w")  # "Number Types" questions
    numbertypes.write("What is the base amount for a binary number?" +"\n"
                      +"What is the binary number equivalent to the hexa number 16A?" +"\n"
                      +"What is the decimal number equivalent to 110110?" +"\n"
                      +"What is the hexa number equivalent to the decimal number 32?"+"\n")
    numbertypes.close()
    
    datastructures=open("Data Structures", "w")  # "Data Structures" questions
    datastructures.write("Is a list mutuable?" + "\n"
                         + "What type of brackets do you use if you want to make a dictionary?" + "\n"
                         + "What is the method that adds an element to the end of a list?" + "\n"
                         + "What is the method used to remove an element from a list or dictionary?"+"\n")
    datastructures.close()
    
    stringsandloops=open("Strings, Loops, and Textfiles", "w")  # "Strings, Loops, and Textfiles" questions
    stringsandloops.write("What method splits the element into words?" + "\n" + "What is the one type of loop?" + "\n" + "What type of loop uses definite iteration?" + "\n" "To read a line from a text file, what is the method that is used?"+"\n")
    stringsandloops.close()

    # Entrance banner
    print("-" * 25)
    print("-" * 35)
    print("Jeopardy: CSI 1320 Edition")
    print("-" * 35)
    print("-" * 25)


# - - - - - While loop cycles through game unless players end it or there are no more questions - - - - -
    keepPlaying = True  # boolean that user can change to end game
    while nextRound != 17 and keepPlaying:
        
        # Round number banner
        print("\n\n" + "-" * 25 + " ROUND " + str(nextRound) + " " + "-" * 25)

        # Decide if it is player 1 or 2's turn
        if nextRound % 2 == 1:  # player 1 plays on odd rounds and player 2 on even rounds
            print("\nPlayer 1's turn:")
        else:
            print("\nPlayer 2's turn:")

        # Print/ select subject number
        subject = selectSubjectNum()

        # - Store name of chosen subject in global variable
        global result
        result = callSubject(subject)  
        
        # Print point values
        pointList = pointsList()  # turns a string of point values in dictionTwo into a printable list
        for point in pointList:
            print(point + " points", end = "  ")
        print("\n" + "-" * 25)


    # - - - While loop continues until a proper number is entered
        while2 = True
        while while2:
            
            # - Global variable to store requested point value
            global pointNum
            pointNum = input("How many points are you aiming for?\n(input point number): ")

            # If requested number is not valid, assign the number 5 to a tester variable
            check2 = 0
            for point in pointList:
                if pointNum == point:
                    check2 = int(pointNum)
                    break
                else:
                    check2 = 5
                    
            # Try and except statement finds error when tester variable = 5
            try:
                5 / (5 - check2)
            except ZeroDivisionError:
                print("Not a point value. Try again.\n")
            else:
                while2 = False

         
        # Remove chosen point value 
        update = updatePoints(pointList, pointNum)   # Remove chosen point value from relevant subject name in dictionTwo

        # Turn printable list of point values back into string to be stored in dictionTwo
        newPointsList = ""
        for point in update:
            newPointsList = newPointsList + point + " "
        dictionTwo[result] = newPointsList

        question(result, int(pointNum))  # Use subject name and point value to print question

        response()  # Ask user for response to question and determine if response is correct

        scores()  # Add point numbers to player total if answer was correct


    # - - - Remove subject entirely if all point values have been selected
        noPoints = ""   # Variable to store subject name if it has no more point values available
        
        # Traverse dictionTwo for subjects with no point values
        for key in dictionTwo:
            if dictionTwo[key] == "":
                noPoints = key
                
        # If noPoints is found, find key in diction with subject name in noPoints
        if noPoints != "":   
            deleteKey = "" # Variable to store the subject number in diction to be deleted

            # Traverse diction for subject number containing noPoints variable
            for key in diction:
                if diction[key] == noPoints:
                    deleteKey = key

            # Remove subject from both dictionaries
            diction.pop(deleteKey)
            dictionTwo.pop(result)

            
    # - - - Decide whether to keep playing
        yes_No = moveForward()  # ask if players want to continue playing
        
        keepPlaying = yes_No  # assign boolean from moveForward() to keepPlaying
        
        nextRound += 1  # increase round number up by 1


  # - - - Detirmine winner and end program
    winner()  # Detirmine winner

    print("\n\n" + "-" * 25 + " Thanks for playing! " + "-" * 25)  # Exit banner


# - - - - - - - Methods - - - - - - -
def selectSubjectNum():
    """print available subjects, return chosen subject"""
    # Print subjects
    print("-" * 20)
    for key in diction:
        print(str(key) + ": " + diction[key])
    print("-" * 20)

  # - - - While loop cycles until proper number is entered
    while1 = True
    while while1:
        # Enter subject number
        subjectNum = int(input("What subject would you like to choose?\n(input subject number): "))
        check1 = 0
        remaining = [] # create list of available subjects
        if 1 in diction:
            remaining.append(1)
        if 2 in diction:
            remaining.append(2)
        if 3 in diction:
            remaining.append(3)
        if 4 in diction:
            remaining.append(4)     
        # if requested subject number is invalid, tester variable = 5
        for subNum in diction:
            if subjectNum == subNum:
                check1 = int(subjectNum)
                break
            else:
                check1 = 5
        # Try and except statement finds error when subject number is invalid
        try:
            5 / (5 - check1)
        except ZeroDivisionError:
            print("Not a subject value. Try again.\n")
        else:
            while1 = False  # End while loop upon finding a valid number
            
    # return chosen subject    
    return subjectNum

        
def callSubject(subNum):
    """Returns the appropiate subject name for chosen subject number"""
    # Traverses diction for subject number user chose 
    for key in diction:
        if key == subNum:
            return diction[key]
        
    
def pointsList():
    """Creates list to print point values for a subject"""
    print("\n\n" + result)
    print("-" * 25)
    subjectPoints = dictionTwo[result]   # call dictionary value containing available point values
    pointsList = subjectPoints.split()   # turn dictionary value into traversable list
    return pointsList


def updatePoints(pointList, point):
    """Remove point value that was chosen"""
    # Find index of point value chosen and pop it from list
    remove = pointList.index(point)
    result = pointList.pop(remove)
    return pointList

def question(sub, num):
    """Use subject name and point value to read proper question from textfile"""
    x = ""  # Question string
    y = open(result, "r")  # Open file with subject name
    # For loop keeps replacing variable x with a new sentence until proper question is read
    for i in range(int(pointNum)):
        x = y.readline()
    # Print question    
    print("\n\nQuestion:\n" + "-" * 30)
    print(x, end = "")
    print("-" * 30)
    y.close()


def response():
    """User enters response to question. Use methods to decide if response is correct, and print result"""
    ans=input("Your answer: What is ")  # User enters response
    decide = ""  # variable to store whether answer is correct or not
    # call list of answers corresponding to subject name
    if result == "Functions":
        # recieve decision and print it to terminal
        decide = answer_Functions(ans)
        print("\n" + decide)
    elif result == "Data Structures":
        decide = answer_DataStructures(ans)
        print("\n" + decide)
    elif result == "Number Types":
        decide = answer_NumberTypes(ans)
        print("\n" + decide)
    elif result == "Strings, Loops, and TextFiles":
        decide = answer_StringsLoopsTextfiles(ans)
        print("\n" + decide)
    # Add 0 points to score if answer is incorrect
    if decide != "correct":
        global pointNum
        pointNum = 0


# - - - Following methods are the answer keys to the questions. If response is an answer in dictionary, correct is returned.
def answer_Functions(n):
    answers={
        "def":"correct",
        "filter":"correct",
        "reduce":"correct",
        "map":"correct",
        "yes":"correct",
        "Yes":"correct",
        "base case":"correct"
        }
    return answers.get(n, "incorrect")

def answer_DataStructures(n):
    answers={
        "yes":"correct",
        "Yes":"correct",
        "{}":"correct",
        "curly brackets":"correct",
        "append":"correct",
        "pop":"correct"
        }
    return answers.get(n, "incorrect")

def answer_NumberTypes(n):
    answers={
        "2":"correct",
        "000101101010":"correct",
        "54":"correct",
        "20":"correct"
        }
    return answers.get(n, "incorrect")

def answer_StringsLoopsTextfiles(n):
    answers={
        "split":"correct",
        "for loop":"correct",
        "while loop":"correct",
        "readline":"correct",
        "read line": "correct",
        }
    return answers.get(n, "incorrect")


# - - - More Methods
def scores():
    """Assign score to proper player and print that player's score"""
    # decide if player 1 or 2 is playing
    if nextRound % 2 == 1:  # player 1 plays on odd rounds and player 2 on even rounds
        player = "player 1"
        value=score.get("player 1", None)  # Retrieve current score from global dictionary
    else:
        player = "player 2"
        value=score.get("player 2", None)
    integer=int(value)  # convert score to integer    
    sum1=integer + int(pointNum)  # add pointNum to current score
    score[player]=sum1  # assign new score to proper player
    print(player + " score: " + str(sum1))  # print score


def moveForward():
    """Decide whether to keep playing"""
  # - - - While loop continues until proper input is recieved
    while2 = True
    while while2:
        decision = input("\nContinue Playing? (Y or N): ")  # Ask if user would like to continue playing
        # if no, end loop and end program
        if decision == "N" or decision == "n":
            while2 = False
            return False
        # if yes, end loop but continue program
        elif decision == "Y" or decision == "y":
            while2 = False
            return True
        
        # error statement
        else:
            print("Invalid input. Please try again.")


def winner():
    """Decide and print the winning player"""

    # variable for player scores
    firstPlayer = int(score["player 1"])
    secondPlayer = int(score["player 2"])

    print("\n")
    print("Final Scores:")
    print(score)

    # print player 1 if they have higher score
    if firstPlayer > secondPlayer:
        print("\n" + "-" * 30)
        print("Player 1 wins!")
        print("-" * 30)

    # print player 2 if they have higher score
    elif firstPlayer < secondPlayer:
        print("\n" + "-" * 30)
        print("Player 2 wins!")
        print("-" * 30)

    # print if player 1 and 2 tied
    else:
        print("\n" + "-" * 30)
        print("Player 1 and Player 2 tied!")
        print("-" * 30)
        

# - - - - -Entry point for program - - - - -
main()
