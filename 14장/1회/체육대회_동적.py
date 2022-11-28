def dfs(depth, selected, ability, dp):
    students, sports = len(ability), len(ability[0])
    if depth == sports: return 0

    if not dp[selected]:
        for student in range(students):
            if selected & (1 << student): continue
            current = ability[student][depth]
            select = dfs(depth + 1, selected | (1 << student), ability, dp)
            dp[selected] = max(current + select, dp[selected])
            
    return dp[selected]

def solution(ability):
    dp = [0] * (1 << len(ability))
    return dfs(0, 0, ability, dp)

