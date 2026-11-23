dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))

quotient = dividend // divisor
remainder = dividend - (quotient * divisor)

print("Remainder:", remainder)