def solution(orders, course):
    answer =[]

    orders.sort( key=lambda x: len(x))

    for i in course:
        
        count=[]
        for j in range(len(orders)):           
            if i == len(orders[j]):
                count.append(j)
        for q in count:
            tmp=[]
            cnt=0
            for j in range(len(orders)):           
                if q == j:
                    for k in range(len(orders[j])):
                        tmp.append(orders[j][k])
                    break
               
            print(orders, tmp)
            for j in orders:        
                flag=True
                for h in range(len(tmp)):                
                    if j.find(tmp[h])==-1:                   
                        flag=False
                        break
                if flag==True:
                    cnt+=1
            if cnt>=2:
                answer.append(''.join(tmp))        

        
            print(cnt)
    ans=list(set(answer))
    
    ans.sort()
    print(ans)



    return answer

o=["XYZ", "XWY", "WXA"]
c=[2,3,4]

solution(o,c)