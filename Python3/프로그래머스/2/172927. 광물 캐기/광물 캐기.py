def solution(picks, minerals):
    if sum(picks) * 5 < len(minerals): 
        minerals = minerals[:sum(picks) * 5]
     
    list_load = []

    while (len(minerals)):
        load = dia = 0
        
        if len(minerals) >= 5:
            set_size = 5
        else:
            set_size = len(minerals)
        
        for i in range(set_size):
            if minerals[0] == "diamond":
                load += 25
                dia += 1
            elif minerals[0] == "iron":
                load += 5
            else:
                load += 1
            
            del minerals[0]
        
        list_load.append((load,dia,set_size))

    list_load.sort(reverse=True)

    tiredness = 0
    for i in range(len(list_load)):
        if (picks[0]):
            tiredness  += list_load[i][2]
            picks[0] -= 1
        elif (picks[1]):
            tiredness  += list_load[i][1] * 5 + (list_load[i][2] - list_load[i][1])
            picks[1] -= 1
        else:
            tiredness  += list_load[i][0]

    return tiredness