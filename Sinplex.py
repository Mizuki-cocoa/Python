VNUM=6
CNUM=3

COLUMN=VNUM+1
ROW=CNUM+1

table= [
[ 1, 1, 1, 0, 0, 0, 0 ],
[ 2, 1, 1, 1, 0, 0, 80 ],
[ 1, 2, 1, 0, 1, 0, 40 ],
[ 1, 1, 2, 0, 0, 1, 60 ]]

c=0
for i in range(5):
    if(table[0][c]<0):
        break
    r=1
    for i in range(ROW):
        if (table[r][c] == 0):
            continue
        else:
            a= table[r][COLUMN - 1] / table[r][c]
            b= table[i][COLUMN - 1] / table[i][c]
            if (a>b):
                r=i
            
    
    k=0
    for q in range(ROW):
        if(r!=q):
            k=table[q][c]/table[r][c]
        table[q][c]=table[q][c]-k*table[r][c]

    for j in range(COLUMN):
        table[r][j]=table[r][j]/table[r][c]
    c+=1
    

print(table[ROW][COLUMN])
            
    


    
