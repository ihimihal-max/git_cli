

def read(path):
    with open(path,'r') as file:
            listi_read =[list(line.split(",")) for line in file]
    return listi_read
