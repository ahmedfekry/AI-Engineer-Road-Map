
# using while loop to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1


print("=========================================== For Loop ===========================================")

#using for loop to print numbers from 1 to 10

for i in range(1, 11):
    print(i)


# range(start, end) function generates numbers from start to end-1

numbers = list(range(1, 11))
print(numbers)  # prints [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("=====================================")

print(range(5))  # prints range(0, 5)

print("===================================== Guessing Game ===========================================")

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1

        if guess == secret_word:
            break

if(guess != secret_word):
     print("game over")


#loop on a list 
numbers = [1, 2, 3, 4, 5]

for x in numbers:
    print(x)