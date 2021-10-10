# testing
birth = input("When were you born? ")
age = 2021 - float(birth)
response = "You're " + str(age) + " years old"

print(response.upper())
print(response.find("re"))
print(response.replace("You're", "Are you"))
print("old" in response)

print(age > 18 and age < 30)

# if statement
if age > 18:
    print("you're an adult")
elif age >= 12:
    print("You're a teenager")
else:
    print("You're a child")

# while loop
i = 0
while i < 5:
    print(i)
    i = i + 1


def times_tables():
    lst = []
    for i in range(10):
        for j in range(10):
            lst.append(i * j)
    return lst


# list
names = ["Roy", "Helen", "Andy", "Kelly"]
names[0] = "RL"
names.insert(3, "David")
print(names[1])
print(names)
print(names.count("Helen"))

names.remove("David")
print(names)
print(len(names))

# While loop
i = 0
while i < len(names):
    print(names[i])
    i = i + 1

# For Loops (easier with list)
for i in names:
    print(i)

# Range & For Loops
range = range(0, 10, 2)  # excluding 10 see
for x in range:
    print(x)

print(99 // 3)
print(100 % 3)

x = 10
x = x + 8
print(x)
y = 10
y += 8
print(y)
