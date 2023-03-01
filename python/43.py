try:
  a=10/2
  print(a)
  try:
      b=[1,2,4,5]
      print(b[31])
  except IndexError:
    print("IndexError")

except ZeroDivisionError:
    print("ArithmeticError")
