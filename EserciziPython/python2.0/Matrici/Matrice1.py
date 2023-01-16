
def invertiCR(x,R,C):
#@param x:int
#@param R:int; number of rows
#@param C:int; number of columns
  mat1=matrix(R,C)
  riga=[]
  colonna=[]
  if x==0:
    return mat1
  for i in range(0,R):
    mat1[i]=input("write a row as a list of " + str(C) + " values (enclosed in square brackets): ")
  riga=mat1[x]
  
  for i in range(0,R):
    colonna.append(mat1[i][x])
    mat1[i][x]=riga[i]
  for c in range(0,C):
    mat1[x][c]=colonna[c]
  return mat1

def matrix(R,C):
#@param R: int; number of rows
#@param C: int; number of columns
  mat=[]
  for i in range(0,R):
    row=[0]*C
    mat.append(row)
  return mat
      
  
    
      
        
    
