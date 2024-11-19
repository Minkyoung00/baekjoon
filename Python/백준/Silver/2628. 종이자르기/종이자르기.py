W, H = (int(i) for i in input().split())
w_cut = []
h_cut = []
w_piece = []
h_piece = []

for i in range(int(input())):
    way, num = input().split()
    if way == '0':
        w_cut.append(int(num))
    
    else:
        h_cut.append(int(num))
        
w_cut.sort()
h_cut.sort()

for i in range(len(w_cut)):
    if i == 0:
        h_piece.append(w_cut[i])
    else:
        h_piece.append(w_cut[i] - w_cut[i-1])

if w_cut:
    h_piece.append(H - w_cut[-1])
else:
    h_piece.append(H)

for i in range(len(h_cut)):
    if i == 0:
        w_piece.append(h_cut[i])
    else:
        w_piece.append(h_cut[i] - h_cut[i-1])

if h_cut:
    w_piece.append(W - h_cut[-1])
else:
    w_piece.append(W)

print(max(w_piece)*max(h_piece))