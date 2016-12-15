file = open("list.txt", "w")

color = input("What is your favorite color? ")

file.write(color)

x=1

while x <= 10:
    print(color)
    x+=1
    
file.close()