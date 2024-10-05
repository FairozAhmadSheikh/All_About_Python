# Python Quiz Game using 2D Collections 

questions=("What is the Largest Animal ? : ",
           "Who was the first person to land on moon ? : ",
           "what is a cpu? :",
           "What Happened on 2nd October? : ",
           "Hittler was from which Country? : ")
options=(("A.Cat","B.Dog","C.Elephant","D.Whale"),
         ("A.Abdul","B.Azeez","C.Gafar","D.Neil Arm Strong"),
         ("A.central","B.process","C.thread","D.central processing unit"),
         ("A.Ghandi Jayanti","B.Jallian Wala Bagh","C.Green Revolution","D.Whale Auction"),
         ("A.Russia","B.America","C.Germany","D.France"))
answers=["D","D","D","A","C"]
guesses=[]
question_number=0
score=0


for question in questions:
    print("----------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)
    guess=input("Enter A B C Or D ").upper()
    guesses.append(guess)
    if guess==answers[question_number]:
        print("Correct Option Selected ")
        score+=1
    else:
        print("Incorrect")
    question_number+=1
print()
print("RESULT CARD".center(40,"="))
print(f"Your Scrore is {score} out of {len(questions)} : {score/len(questions)*100}%")
print()
print()
print(f"Your Answers : {guesses}")
print(f"Answer Key : {answers}")