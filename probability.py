a = float(input("Disease % in population: "))
b = float(input("Test sensitivity %: "))
c = float(input("False positive %: "))

a = a / 100
b = b / 100
c = c / 100

d = 1 - a

e = (b * a) + (c * d)

f = (b * a) / e

print("Actual disease probability:", round(f * 100, 2), "%")
