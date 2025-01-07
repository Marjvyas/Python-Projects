print("We are taking your test...")
print("rules of the test:")
print("1:you will earn 4 points on each correct answer." )
print("2:You will lose 1 point from your total score on each incorrect answer.")
print("3:you can skip the question, if you are not sure.")
input("Press enter to continue...")
print()
questions={1:'What is the hottest planet in the milky way?',
           2:'The Big Bang Theory is related to which of the following?',
           3:'Who was the first woman to win a Nobal Prize?',
           4:'In which part of the human body is the smallest bone found?',
           5:'Which is the smallest flightless bird?'
             }
options={1:'A)Saturn\nB)Venus\nC)Jupiter\nD)Pluto',
         2:'A)Continental Drift\nB)Origin Of Universe\nC)Origin Of Himalayas\nD)Eruption of Volcanoes',
         3:'A)P.T. Usha\nB)Indira Gandhi\nC)Marie Curie\nD)Pierre Curie',
         4:'A)Fourhead\nB)Thumb\nC)Ear\nD)Mouth',
         5:'A)Kingfisher\nB)Kiwi\nC)Sparrow\nD)Hummingbird'}
Answers={1:'b',
         2:'b',
         3:'c',
         4:'c',
         5:'b'}
total=0
your_answer={}
correct_ans=()
for key,value in questions.items():
    print(f"{key}:{value}")
    print()
    for key1,value1 in options.items():
        if(key==key1):
            print(value1)
    print()
    w=input("Enter your answer(a or b or c or d) and enter to skip:")
    if(w.lower()=='s'):
        continue
    else:
        for key2, value2 in Answers.items():
            if(key==key2):
                if(w.lower()==value2):
                    print("Correct Ans\n")
                    total+=4
                elif(w.lower()==''):
                    continue
                else:
                    total-=1
                    print("Wrong Ans\n")
print(f"Your score:{total}/20")
