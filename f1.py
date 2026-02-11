

def read(path):
    with open(path,'r') as file:
            listi_read =[list(line.split(",")) for line in file]
    return listi_read

def source_ip (ips):
    list_ip =[ip for ip in ips if not ip[1].startswith("10") and not ip[1].startswith("192.168")]
    return list(list_ip)


