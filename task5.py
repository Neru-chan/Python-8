di = {}
file = open("mbox-short.txt", "r")
for line in file:
    if line.find("From ", 0, 5) < 0: continue

    key = line.split()[1]
    if key not in di:
        di[key] = 1
        continue

    di[key] += 1

email = max(di, key=di.get)
value = di[email]

print(f"{email} : {value}")