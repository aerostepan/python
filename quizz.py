questions = ("How old are you?: ", 
             "How are you?: ",
             "What's your name?: ", 
             "Where do you live?: ",
             "Who is your friend?: ")

options = (("A.21","B.20","C.101","D.2"),
           ("A.perfect","B.bad","C.good","D.fine"),
           ("A.Stepan","B.Joe","C.Mark","D.Tony"),
           ("A.Russia","B.Zimbabwe","C.USA","D.Austria"),
           ("A.Tony Kark","B.Derman Gzhugas","C.Bill Gates","D.Jeffrey Epstein"))

answers = ("A","C","A","D","B")
guesses = []
score = 0   
question_num = 0    

for question in questions:
    print("---------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter guess(A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1

print("--------------")
print("    RESULTS     ")
print("--------------")

print("answers", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guess: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")
