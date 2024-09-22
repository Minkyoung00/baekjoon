def solution(survey, choices):
    answer = ''
    N = len(survey)
    result = {'R' : 0, 'T' : 0, 'F' : 0, 'C' : 0, 'M' : 0, 'J' : 0, 'A' : 0, 'N' : 0}
    
    for i in range(N):
        if choices[i] < 4:
            result[survey[i][0]] += 4 - choices[i]
        elif choices[i] > 4:
            result[survey[i][1]] += choices[i] - 4

    if result['R'] >= result['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if result['F'] > result['C']:
        answer += 'F'
    else:
        answer += 'C'
    
    if result['M'] > result['J']:
        answer += 'M'
    else:
        answer += 'J'

    if result['A'] >= result['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer