# Write an algorithm that takes an array and moves all of the zeros to the end, 
# preserving the order of the other elements.

# move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

def move_zeros(array):
    output = []
    zeros = 0
    for elem in array:
        if (elem != 0) or (type(elem) == bool):
            output.append(elem)
        elif elem == 0:
            zeros += 1
    for _ in range(zeros):
        output.append(0)
    return output
