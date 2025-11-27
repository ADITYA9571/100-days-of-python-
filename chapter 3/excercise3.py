print("kae bhail Crorepati!!")
sum = 0
prize=[1000,2000,3000,5000,10000,20000,40000,80000,160000,3,20000]
ques=["What is the capital of India?","Which planet is known as the Red Planet?","How many colors are there in a rainbow?","Which animal is known as the ‘King of the Jungle’?","Which festival is known as the Festival of Lights?","Which is the largest ocean in the world?","What is the national currency of India?","Which sport is known as the ‘Gentleman’s Game’?","Which flower is the national flower of India?","Who wrote the national anthem of India?"]
ans=["C) New Delhi","B) Mars","C) 7","B) Lion","A) Diwali","D) Pacific","C) Rupee","B) Cricket","B) Lotus","A) Rabindranath Tagore"]
options = ["A) Mumbai B) Kolkata C) New Delhi D) Chennai","A) Venus B) Mars C) Jupiter D) Mercury","A) 5 B) 6 C) 7 D) 8","A) Tiger B) Lion C) Elephant D) Leopard","A) Diwali B) Holi C) Eid D) Christmas","A) Atlantic B) Indian C) Arctic D) Pacific","A) Dollar B) Pound C) Rupee D) Euro","A) Football B) Cricket C) Hockey D) Tennis","A) Rose B) Lotus C) Sunflower D) Jasmine","A) Rabindranath Tagore B) Mahatma Gandhi C) Subhash Chandra Bose D) Jawaharlal Nehru"]
for i in range(10):
    if i != 0:
        print("next question for amount",prize[i])
    print(ques[i])
    print(options[i])
    correct=str(input("choose option A B C D: "))
    if correct in ans[i]:
        print("congrats correct answer")
        sum += prize[i]
    else:
        print("OOH OO")
        break
print("Winning amount is: " ,sum)