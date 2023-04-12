import time

B_YEAR = 1998
now = time.time()
# print(now)

now_tm = (time.gmtime(now))

# print(now_tm.tm_hour)

print(f'Evenimentul s-a intamplat in anul:{now_tm.tm_year}, in luna:{now_tm.tm_mon},\
 in ziua:{now_tm.tm_mday}, la ora:{now_tm.tm_hour}.')

# print(now_tm.tm_year - B_YEAR)

# time.strftime ("%Y", + structura pe care o vrem ) => STR

print(time.strftime("Data: %d.%B %Y Ora: %H:%M: %S", now_tm))
print(time.strftime('%c', now_tm))
