import numpy

def LCM(a:int,b:int):
    a_Absolute=abs(a)
    b_Absolute=abs(b)
    #print(a,b)
    if(a_Absolute<b_Absolute):a_Absolute,b_Absolute=b_Absolute,a_Absolute
    while(a_Absolute!=0 and b_Absolute!=0):
        tmp=a_Absolute%b_Absolute
        a_Absolute=b_Absolute
        b_Absolute=tmp
        #print(a_Absolute,b_Absolute)
    result=int(a*b/a_Absolute)
    #print(result)
    return result

def display(Target_Matrix):
    for i in Target_Matrix:
        for j in i:
            print(j,end=" ")
        print()
    print("\n")

def simplify(original_row,target_row,magnification):
    result_row=[]
    for i in range(0,len(original_row)):
        result_row.append(target_row[i]-original_row[i]*magnification)
    return result_row

def main(Matrix,m_Of_Matrix,n_Of_Matrix):
    pivot_element_column_pos=[]#pivot_element_column_pos[0]=0代表 第一行中主元在第一列
    print(m_Of_Matrix,n_Of_Matrix)
    #for i in range(0,m_Of_Matrix,1):
    #    Matrix.append([])
    #    for j in range(0,n_Of_Matrix,1):
    #        Matrix[i].append(float(input()))

    non_pivot_element_column_count=0
    display(Matrix)
    i=0
    while(i<m_Of_Matrix):
        if(i+non_pivot_element_column_count>=n_Of_Matrix):
            break
        if(Matrix[i][i+non_pivot_element_column_count]==0):
            target_row=i
            for j in range(i+1,m_Of_Matrix):
                if(Matrix[j][i+non_pivot_element_column_count]!=0):
                    target_row=j
                    break
            if(target_row==i):
                non_pivot_element_column_count=non_pivot_element_column_count+1
                continue
            else:
                Matrix[i],Matrix[target_row]=Matrix[target_row],Matrix[i]
        pivot_element_column_pos.append((i+non_pivot_element_column_count))
        for j in range(i+1,m_Of_Matrix):
            magnification=Matrix[j][i+non_pivot_element_column_count]/Matrix[i][i+non_pivot_element_column_count]
            Matrix[j]=simplify(Matrix[i],Matrix[j],magnification=magnification)
            #print(tmp,"为",i," ",i+non_pivot_element_column_count," ",j," ",i+non_pivot_element_column_count)
            #display(Matrix)
           # print("\n")
        i=i+1
    display(Matrix)
    i=len(pivot_element_column_pos)-1
    while(i>=0):
        pos=pivot_element_column_pos[i]
        for j in range(0,i):
            magnification=Matrix[j][pos]/Matrix[i][pos]
            Matrix[j]=simplify(Matrix[i],Matrix[j],magnification=magnification)
        simplifier=Matrix[i][pos]
        Matrix[i]=[round(x/simplifier,3) for x in Matrix[i]]
        i=i-1
    display(Matrix)
    return Matrix

