def gauss(m):
    #eliminate columns
    for col in range(len(m[0])):
        for row in range(col+1,len(m)):
            r=[(rowValue * (-(m[row][col]/m[col][col]))) for rowValue in m[col]]
            m[row]=[sum(pair) for pair in zip(m[row],r)]
    
    # back substitution
    ans=[]
    m.reverse() # reversing the matrix for making back substitution easier
    for sol in range(len(m)):
        if sol == 0:
            ans.append(m[sol][-1]/m[sol][-2])
        else:
            inner=0
            for x in range(sol):
                inner+=ans[x]*m[sol][-2-x]
            ans.append((m[sol][-1]-inner)/m[sol][-2-sol])
    ans.reverse()
    return ans
