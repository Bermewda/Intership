import csv
import random

def game(fname):
    r = []
    score=0
    with open(fname,'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)   
        r = [row for row in reader]
    csvfile.close()
#     print(np.array(r))
    random.shuffle(r)
#     print(np.array(r))

    for i in r:
        guess=10
        print("\n")
        print("hint : "+i[1])
        
        word=[]
        for j in i[0]:
            if j in "1234567890-+!@#$%^&*()~ ":
                word.append(j.lower())
            else:
                word.append("_")
            
            
        while guess > 0 and '_' in word:
            print(str(word) + " remaining wrong guess "+str(guess))  
            
            ans = input()
            start=0
            if ans.lower() in word :
                guess-=1;
                print("you used to guess it : "+ans.lower())                
            elif ans.lower() in i[0].lower() :    
                for k in i[0].lower():
                    if ans.lower() in k: 
                        word[i[0].lower().find(ans.lower(),start)]=ans.lower()
                        start=i[0].lower().find(ans.lower(),start)+1
#                         print(start)
               
            else : 
                guess-=1;
                print("wrong guessed : "+ans.lower())
                
        print(str(word) + " remaining wrong guess "+str(guess)) 
        print("Answer : "+i[0].lower())
        if guess != 0:
            score+=1

    print("\n")
    print("You score : "+str(score))
    
    

print("Select Category:")
print("kpop brands (1)")
print("hit songs (2)\n")
category = input() 

if category == '1' :
    game('kpop.csv')
    
elif category == '2' :
    game('song.csv')
else:
    print("error!! don't have category")