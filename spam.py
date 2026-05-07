a = float(input("Spam emails %: "))
b = float(input("Spam emails with 'free' %: "))
c = float(input("Normal emails with 'free' %: "))

a = a / 100
b = b / 100
c = c / 100

d = 1 - a

e = (b * a) + (c * d)

f = (b * a) / e

print("Spam probability:", round(f * 100, 2), "%")
