first_set = (1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29)
second_set = (2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30)
third_set = (4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 21, 23, 28, 29, 30)
fourth_set = (8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30)
fifth_set = (16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30)

number = 0

print("This is a program made to guess your number from 1-30")
print("First, pick a number from 1 to 30")
print("Answer the following questions with either 'yes' or 'no'")

#First Set
print(first_set)
answer1 = input("Is your number on this list? ")

str(answer1)
answer1.lower()
if (len(answer1)) == 3:
    number += first_set[0]

else:
    pass

#Second Set
print(second_set)
answer2 = input("Is your number on this list? ")

answer2.lower()
if (len(answer2)) == 3:
    number += second_set[0]

else:
    pass

#Third Set
print(third_set)
answer3 = input("Is your number on this list? ")

answer3.lower()
if (len(answer3)) == 3:
    number += third_set[0]

else:
    pass

#Fourth Set
print(fourth_set)
answer4 = input("Is your number on this list? ")

answer4.lower()
if (len(answer4)) == 3:
    number += fourth_set[0]

else:
    pass

#Fifth Set
print(fifth_set)
answer5 = input("Is your number on this list? ")

answer5.lower()
if (len(answer5)) == 3:
    number += fifth_set[0]

else:
    pass

print("Your number is " + str(number))