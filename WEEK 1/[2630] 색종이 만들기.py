def check_col(paper,white,blue):     #종이의 모든 색이 같은 지 확인 후 T,F 
    col = paper[0][0]
    len_n = len(paper)

    for i in range(len_n):
        for j in range(len_n):       
            if paper[i][j] != col:
                for k in split(paper):
                    white, blue = check_col(k,white,blue)
                return white, blue

    if col == 0: white += 1
    else: blue += 1 
    return white, blue

def split(paper):
    len_n = len(paper)
    half = len_n //2
    paper1 = [i[:half] for i in paper[:half]]
    paper2 = [i[half:] for i in paper[:half]]
    paper3 = [i[:half] for i in paper[half:]]
    paper4 = [i[half:] for i in paper[half:]]
    return [paper1, paper2, paper3, paper4]

N = int(input())
paper = []
for i in range(N):
    paper.append([int(i) for i in input().split()])

white, blue = 0, 0

white, blue = check_col(paper,white,blue)

print(white)
print(blue)