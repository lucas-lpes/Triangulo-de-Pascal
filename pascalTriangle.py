#Representation of the coefficients of binomial expansions from order 0 to infinity

def pascal(target, acc = 0, list = [1]):
    #acc its the variable to control when it gets to the target
    print(list)

    if acc == target:
        return


    temp = [1]
    for i in range(len(list)-1):
        next = list[i] + list[i+1]
        temp.append(next)

    temp.append(1)
    
    #Recursive call to fullfil the next line
    pascal(target, acc+1, temp)
