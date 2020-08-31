#Lottery Number Generstor

UserPlaying = "Yes"
LotteryNumbers = []

import random

while UserPlaying == "Yes":
  print("Hey welcome to the Lottery Number Generator")
  PressToSpin = input("Just press enter to spin")
  if PressToSpin == "":
    LotteryNumber1 = random.randint(1,49)
    LotteryNumber2 = random.randint(1,49)
    LotteryNumber3 = random.randint(1,49)
    LotteryNumber4 = random.randint(1,49)
    LotteryNumber5 = random.randint(1,49)
    LotteryNumber6 = random.randint(1,49)
    LuckyBall = random.randint(1,49)

    print("Here are your numbers")
    print(LotteryNumber1)
    print(LotteryNumber2)
    print(LotteryNumber3)
    print(LotteryNumber4)
    print(LotteryNumber5)
    print(LotteryNumber6)
    print('Your Lucky Ball Number is',LuckyBall)

    LotteryNumbers.append(LotteryNumber1)
    LotteryNumbers.append(LotteryNumber2)
    LotteryNumbers.append(LotteryNumber3)
    LotteryNumbers.append(LotteryNumber4)
    LotteryNumbers.append(LotteryNumber5)
    LotteryNumbers.append(LotteryNumber6)    
    

    UserPlaying = "No"
    KeepPlaying = input("Would you like to go again?").lower()
    if KeepPlaying == "yes" or KeepPlaying == "y":
      UserPlaying = "Yes"
    elif KeepPlaying == "no" or KeepPlaying == "n":
      UserPlaying = "No"
