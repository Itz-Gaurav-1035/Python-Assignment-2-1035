num = int(input("Enter a two-digit number: "))

tens = num // 10
ones = num % 10
digit_sum = tens + ones

print("Sum of digits:", digit_sum)