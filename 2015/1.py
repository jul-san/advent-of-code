with open("./input.txt", 'r') as file:
    contents = file.read();
    
    counter = 0

    for x in contents:
        if x == "(":
            counter += 1
        elif x == ")":
            counter -= 1

    print(counter)
        
