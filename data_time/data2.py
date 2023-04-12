import time

event_time = '12 April 2023 16:48:53'

ev_tm = time.strptime(event_time, "%d %B %Y %H:%M:%S")
# print(ev_tm)

ev1 = '20-02-2023 10:11'
ev2 = '22-02-2023 12:45'
ev_tm1 = time.strptime(ev1, "%d-%m-%Y %H:%M")
ev_tm2 = time.strptime(ev2, "%d-%m-%Y %H:%M")

rezultat = (ev_tm2.tm_min - ev_tm1.tm_min)
delta_h = (ev_tm2.tm_hour - ev_tm1.tm_hour) * 60
delta_d = (ev_tm2.tm_mday - ev_tm1.tm_mday) * 60 * 24

print(rezultat, delta_h, delta_d)
