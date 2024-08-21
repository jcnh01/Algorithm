def solution(routes):
    routes.sort(key = lambda x : x[0])
    st = [False] * len(routes)
    routes.reverse()
    
    print(routes)
    
    li = []
    now = 0
    
    for i in range(len(routes)) :
        if st[i] :
            continue
        li.append(routes[i][0])
        now = routes[i][0]
        for j in range(i, len(routes)) :
            if routes[j][0] <= now and routes[j][1] >= now :
                st[j] = True
    
    return len(li)