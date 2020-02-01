def missing(N, integerList):
    if type(N) != int:
        print("Error: a non-integer value is provided in the first or as part of the second argument")
        return(0)
    for element in integerList:
        if type(element) != int:
            print("Error: a non-integer value is provided in the first or as part of the second argument")
            return(0)
          
    if len(integerList) != (N - 1):
        print("Error: the number of items provided in the second argument does not match N-1")
        return(0)

    else:
        evaluate = []
        for i in range(N):
            count = 0 
            for j in range(N - 1):
                if integerList[j] == (i+1):
                    count = count + 1
            evaluate.append(count)
        print(evaluate)
  
    if sum(evaluate) == (N - 1):
        for i in range(N):
            if evaluate[i] == 0:
                return(i + 1)
    else:
        print("Error: the second argument has duplicate values.")
        return(0)
