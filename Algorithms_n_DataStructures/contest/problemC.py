n, l, s = map(int, input().split())
taxis = {}

for _ in range(n):
    event = input().split()
    if event[0] == 'TAXI':
        timestamp, taxi_id, taxi_pos = map(int, event[1:])
        taxis[taxi_id] = (timestamp, taxi_pos)
    else:
        timestamp, order_id, order_pos, time = map(int, event[1:])
        available_taxis = []

        for taxi_id, (taxi_timestamp, taxi_pos) in taxis.items():
            if taxi_timestamp > timestamp:
                continue

            time_diff = timestamp - taxi_timestamp
            max_distance = time_diff * s
            if taxi_pos + max_distance >= l:
                if taxi_pos <= order_pos < l or 0 <= order_pos <= (taxi_pos + max_distance) % l:
                    available_taxis.append(taxi_id)
            else:
                if taxi_pos <= order_pos <= taxi_pos + max_distance:
                    available_taxis.append(taxi_id)


        if not available_taxis:
            print(-1)
        else:
            print(' '.join(map(str, sorted(available_taxis)[:5])))
