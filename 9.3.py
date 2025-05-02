def create_array(row,col,height,num):
    
    arr_row=[]
    for i in range(0,row):
        
        arr_col=[]
        for j in range(0,col):
            
            arr_height=[]
            for k in range(0,height):
                arr_height.append(num) 
            arr_col.append(arr_height)
        arr_row.append(arr_col)
    return arr_row

#Recursion
def create_array(row, col, height, num):
    if row==0:
        return []
    
    def create_2d(col):
        if col==0:
            return []
        
        def create_1d(height):
            if height==0:
                return []
            
            return [num]+create_1d(height-1)
        return [create_1d(height)]+create_2d(col-1)
    return [create_2d(col)]+create_array(row-1,col,height,num)

print(create_array(3,3,3,1))
