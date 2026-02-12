
#
def read(path):
    with open(path,'r') as file:
            listi_read =[list(line.split(",")) for line in file]
    return listi_read

def source_ip (ips):
    list_ip =[ip for ip in ips if not ip[1].startswith("10") and not ip[1].startswith("192.168")]
    return list(list_ip)


def filter_sensitive_ports(data):
    sensitive_ports = ["22", "23", "3389"]
    return [line for line in data if line[3].strip() in sensitive_ports]

def filter_by_size(data):

    return [line for line in data if int(line[5].strip()) > 5000]

def tag_traffic(data):

    return ["LARGE" if int(line[5].strip()) > 5000 else "NORMAL" for line in data]