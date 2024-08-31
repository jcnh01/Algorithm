li = []
w = []

def dfs(words) :
    st = ""
    for i in range(len(w)) :
        st += w[i]
    li.append(st)
    if len(w) == 5 :
        return
    for wo in words :
        w.append(wo)
        dfs(words)
        w.pop()

def solution(word):
    answer = 0
    
    words = ['A', 'E', 'I', 'O', 'U']
    
    dfs(words)
    
    answer = li.index(word)
    
    return answer