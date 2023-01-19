# ----------------------
def new_game(): #fuction pyhton using def similar methods on java
    
    guesses=[]
    correct_guesses=0
    questio_num=1

    for key in questions:
        print("----------------------")
        print(key)
        for i in options[questio_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D):") #new variable to make the choice
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess) #create after fuction "check_answer" has ben ceated
        questio_num += 1

    display_score(correct_guesses, guesses) #untuk menampilkan methode "display_score"

# ----------------------
def check_answer(answer, guess): #fuction pyhton using def similar methods on java
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG!")
        return 0
    
# ----------------------
def display_score(correct_guesses, guesses): #fuction pyhton using def similar methods on java
    print("----------------------")
    print("RESULTS")
    print("----------------------")

    print("Answers: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

    # pass //pass created for frame basic so program not error in early program(hanya dibuat diawal supaya gak error)

# ----------------------
def play_again(): #fuction pyhton using def similar methods on java

    response = input("Mau main lagi? (ya atau tidak): ")
    response = response.upper()
    
    if response == "YA":
        return True
    else:
        return False
    pass
# ----------------------


questions = {
    "Pembuat python yaitu: ": "A",
    "Python dibuat pada tahun: ": "B",
    "Python di distribusikan untuk kelompok komedi: ": "C",
    "Bumi berotasi: ": "A"
}

options=[["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
         ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
         ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
         ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"],
        ]

new_game()

while play_again():
    new_game()

print("Byeeeeee")