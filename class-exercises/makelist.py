file = open("list.txt", "w")    #Open file

color = input("What is your favorite color? ")  #Ask a question

file.write(color)   #Save the response

x=1 #Keep track of repetition

while x <= 10:  #Repeats user input 10 times
    print(str(x) + "." + color + "\n")    #Print x, the user input,and a line between each repetition to have a numbered list of the user input
    x+=1    #Adds to the number all the way till 1o
    
file.close()    #close the file so it cannot be changed