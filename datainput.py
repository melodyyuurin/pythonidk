// inputing data variable and using a loop.

name = input("whats your name? ")
print("Cool name !")

while True:
    age = input("how old are you? ")
    try: 
        age =int(age)
        break
    except ValueError:
        print("please a valid number")

colorArray = ["red", "green", "blue", "yellow", "white", "black", "pink", "purple", "violet", "brown", "cyan", "orange"]
while True: 
    color = input("whats your favortie color? ")
    if color in colorArray:
        print("nice.")
        break
    else:
        print("is that a color? please enter a valid color")
        
print(f"Hi, {name}! so youre {age} and you like {color}. Nice to meet you!")
