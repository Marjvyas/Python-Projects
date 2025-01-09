from knowledge_key import key
a=[]
h=[]
for i in range(len(key)):
    if i%3==0:
        a.append(key[i])
    else:
        a.append('_')
        h.append(key[i])
def index(guess):
    for i in range(len(key)):
        if guess.lower()==key[i]:
            return i
k=list('KNOWLEDGE')
j=0
q=0
f=[' ']*len(k)
while True:
    if a==key:
        q=1
        break
    print("###################################")
    print(' '.join(k))
    if k==['X']*len(key):
        break
    print(' '.join(f))
    print(' '.join(a))
    guess=input('Guess the letter":')
    if guess.isalpha():
        if guess.lower() in h:
            print("Congratulations!!!")
            a[index(guess)]=guess.lower()
        else:
            print("Entered number is not in key... So sad")
            k[j]='*'
            f[j]=guess.lower()
    else:
        print("Invalid Entry!!!!")
if q==1:
    print("You got the word!!!")
else:
    print("You lose the game...")
