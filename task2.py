my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}


list = [0, 0, 0]
for i in range(3):
    MAX = [0, 0, 0]
    for key, value in my_dict.items():
        if [key, value] == list[0]: continue
        if [key, value] == list[1]: continue
        if [key, value] == list[2]: continue
        if value > MAX[1]: MAX = [key, value]
    list[i] = MAX

print(list)