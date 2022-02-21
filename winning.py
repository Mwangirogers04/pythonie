
winning_number=100
number=int(input("Guess a number:"))
if number==winning_number:
  print("CONGRATULATIONS YOU WON!!!")
else:
  print("YOU DIDN'T MATCH")
  if number>winning_number:
    print("TOO HIGH")
  else:
    print("TOO LOW")
    