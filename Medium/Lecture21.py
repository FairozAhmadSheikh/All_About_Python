import random

# Random integer generator  

#Range
start=1
end=100
# Generator 
number=random.randint(start,end)
# Output
print(number)

# Random Floating point value genrator from 0 to 1

number2=random.random()
print(number2)

# Choice maker

sample_space=["heads","tails"]
sample_space2=("rock","paper","scissor")

print(random.choice(sample_space))
print(random.choice(sample_space2))

# Shuffle 
cards=["2","3","4","5","6","7","8","9","10","A","K","Q","J"]
print(cards)
random.shuffle(cards)
print(cards)


