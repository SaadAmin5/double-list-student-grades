scores=[[54,76,78,98],
       [50,70,77,44],
       [70, 77,55,98],
       [66,88,40,55]]

count=0
total=0

for row in scores:
    count=count+1
    total=0       #reseting total to zero at the beginning of each iteration of the outer loop
    count_col=0   #reseting count_col to zero at the beginning of each iteration of the outer loop
    print('\n')
    print('Term', count)
    
    for column in row:
        print('Grade: ', column)
        total=total+column
        count_col=count_col+1
        average=total/count_col
        
    print('sum: ', total)
    print('average grade: ', average)