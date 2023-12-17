print("Input some integers to calculate their sum and average. Input 0 to exit.")
count = 0
sum = 0
number = 1

while number != 0:
  number = int(input())
  sum = sum + number
  count += 1

if count == 1:
  print("Input some numbers")
else:
  average = sum / (count - 1)
  print("Average of the above numbers are: ", average)
