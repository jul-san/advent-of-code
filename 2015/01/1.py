with open("./input.txt", 'r') as file:
    contents = file.read();
    
    counter = 0
    position = 0

    for i, x in enumerate(contents):
        if x == "(":
            counter += 1
        elif x == ")":
            counter -= 1
        if counter == -1:
            position = i + 1
            break

file.close()
print(position)
        
