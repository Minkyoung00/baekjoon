def ceil(a):
    if a > round(a):
        return round(a) + 1
    else:
        return round(a)
        
def solution(fees, records):
    answer = []
    cars_info = {}
    cars_num = []

    for record in records:
        time, num, in_out = record.split()
        
        h, m = time.split(":")
        time = int(h) * 60 + int(m)

        if in_out == "IN":
            time = -time
        
        if num in cars_info:
            cars_info[num].append(time)
        else:
            cars_info[num] = [time]
            cars_num.append(num)

    cars_num.sort()

    for car_n in cars_num:
        if len(cars_info[car_n]) % 2 != 0:
            cars_info[car_n].append(23 * 60 + 59)

        t_sum = sum(cars_info[car_n])
        if t_sum < fees[0]:
            charge = fees[1]
        else:
            charge = fees[1] + ceil((t_sum - fees[0]) / fees[2]) * fees[3]
        answer.append(charge)

    return answer