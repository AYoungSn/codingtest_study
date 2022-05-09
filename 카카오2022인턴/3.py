from re import L

# fail

def solve(alp, cop, problems, visit, time):
    if len(visit) == sum(visit):
        return time
    cur = alp, cop
    min_alp = 150
    min_cop = 150
    poss = []

    for i in range(len(problems)):
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problems[i]
        if visit[i] == 0:
            if alp >= alp_req and cop >= cop_req:
                alp += alp_rwd
                cop += cop_rwd
                time += cost
                visit[i] = 1
                poss.append(i)
            else:
                min_alp = min(min_alp, alp_req)
                min_cop = min(min_cop, cop_req)
    
    if cur[0] == alp or cur[1] == cop:
        req_a = min_alp - alp
        req_c = min_cop - cop
        if len(poss) == 0:
            alp = min_alp
            time += req_a
            cop = min_cop
            time += req_c
            solve()
        else:
            tmp_alp = alp
            tmp_cop = cop
            for p in poss:
                problems[p][]
        
        

    return solve(alp, cop, problems, visit, time)
            

def solution(alp, cop, problems):
    answer = 0
    visit = [0 for _ in range(len(problems))]
    solve(alp, cop, problems, visit, 0)
    return answer

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))