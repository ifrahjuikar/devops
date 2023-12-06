import itertools

def fizz_buzz(n):
    for i in itertools.islice(itertools.count(1), n):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

# Get the user input for the upper limit
try:
    n = int(input("Enter a number: "))
    fizz_buzz(n)
except ValueError:

    print("Invalid input. Please enter a valid number.")


    