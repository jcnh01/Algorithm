import sys

S, E, Q = map(str, input().split())

s_hour, s_minute = map(str, S.split(":"))
e_hour, e_minute = map(str, E.split(":"))
q_hour, q_minute = map(str, Q.split(":"))

s_hour, s_minute = int(s_hour), int(s_minute)
e_hour, e_minute = int(e_hour), int(e_minute)
q_hour, q_minute = int(q_hour), int(q_minute)

s = set()
e = set()

rs = 0

for i in sys.stdin :
    time, name = i.split()

    hour, minute = map(str, time.split(":"))

    hour, minute = int(hour), int(minute)
    
    if hour < s_hour or (hour == s_hour and minute <= s_minute) :
        s.add(name)

    if hour > e_hour or (hour == e_hour and minute >= e_minute) :
        if hour < q_hour or (hour == q_hour and minute <= q_minute) :
            if name in e :
                continue
            if name in s :
                rs += 1
                e.add(name)

print(rs)