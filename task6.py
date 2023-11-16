def printInventory(dict : dict):
    count = sum(dict.values())
    
    for key, value in dict.items():
        print(f"{value} {key}")
    
    print(f"Total number of items : {count}")



printInventory({"rope" : 1, "torch" : 6, "dagger" : 1, "arrow" : 30, "diamond" : 4})