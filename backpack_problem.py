def morral(size_morral : int,  weights : list, values : list, position : int):
    
    #Check if still having space or things, if not, then it ends
    if position == 0 or size_morral == 0:
        return 0
    
    # check if weight value is greater than the size 
    if weights[position - 1] > size_morral: 
        return morral(size_morral, weights, values, position-1)
    
    # Taking greater value, if not, then moving to the next position
    return max(
                values[position-1] + morral(size_morral - values[position-1], weights, values, position-1),
                morral(size_morral, values, weights, position-1)
               )



if __name__ == '__main__':
    values : list = [10, 30, 40, 25]
    
    weights : list = [5, 10, 21, 7]
    
    size_morral : int = 20
    
    position : int = len(values)
    
    result = morral(size_morral, weights, values, position)
    print(result)