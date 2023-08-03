def grade_mcq(sol,ans):
    count=0
    if len(ans)!=len(sol):
        return -1
    else:
        for i in range(len(sol)):
            if sol[i]==ans[i]:
                count+=1    
        return count
    

exec(input())