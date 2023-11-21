# Amstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
# https://en.wikipedia.org/wiki/Narcissistic_number
def check_amstrong(number):
    digits = len(str(number))
    sum = 0
    temp = number
    while temp > 0:
        sum += pow(temp % 10, digits)
        temp //= 10
    return number == sum

num = int(input("Enter a number: "))
if check_amstrong(num):
    print(num, "is an Amstrong number")
else:
    print(num, "is not an Amstrong number")