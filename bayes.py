a = float(input("M1 production %: "))
b = float(input("M2 production %: "))
c = float(input("M3 production %: "))

d = float(input("M1 defect %: "))
e = float(input("M2 defect %: "))
f = float(input("M3 defect %: "))

a = a / 100
b = b / 100
c = c / 100

d = d / 100
e = e / 100
f = f / 100

g = (d * a) + (e * b) + (f * c)

h = (e * b) / g

print("Defective bolt from M2:", round(h * 100, 2), "%")
