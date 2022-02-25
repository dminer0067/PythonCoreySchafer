import random
import os

grt = ["Hello","Hey","Hi","Hola","Hey You"]
val = random.randint(0,1)
cols = ["Red","Balck","Green"]

msg = random.choice(grt)
cols_res = random.choices(cols,weights=[10,5,2],k=15)

# print(val)
# print(msg)
# print(cols_res)

deck = list(range(1,53))
hand = random.sample(deck,k=5)

random.shuffle(deck)

print(deck)
print(hand)







x = os.getcwd()
print(x)