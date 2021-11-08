lst = [1.25, True, "some"]
dct = {"one": "red", "two": "orange", "three": "yellow"}
a = {1, "a", None}
print(lst[1])


years = 25
if years < 0:
    print("Некорректный возраст")
elif years < 18:
    print("Дети")
elif years > 60:
    print("Пенсионеры")
else:
    print("Взрослые")


s = 10
while s > 0:
    s -= 1


lst2 = [5, False, "new"]
for i in lst2:
    print(i)


for i in range(6):
    print(i)


string = "TEST"
if "E" in string:
    print("pass")


name = input("Представьтесь пожалуйста!\n")
print(f"Здравствуйте, {name}!")


with open("README.md", "r", encoding="utf-8") as file:
    for line in file:
        print(line, end="")


def summa(x, y):
    return x + y


def any_amount(*args):
    for i in args:
        print(i)
