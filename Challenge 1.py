#This is the code for the first challenge of the 2020 Foobar.
#The task was that of creating a program which was capable of finding the largest square value of an input, then find the largest square of the value of after the first one was removed from the input, and so on until it would be equal to 0. 

def solution(area):
    # Your code here
    ints = []

    for x in range(1000000, 0, -1):
        while sum(ints) + x**2 < area:
            if area % x == 0 and x != area:
                ints.append(x**2)
            elif area % x != 0 and x != area:
                ints.append(x**2)
        if sum(ints) + x**2 == area:
            ints.append(x**2)
    if sum(ints) < area:
        while sum(ints) < area:
            ints.append(1)
    return ints

for x in range(5):
    print(x, solution(x))