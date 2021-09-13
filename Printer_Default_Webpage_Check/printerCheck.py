import requests

f = open("ips.txt", 'r')

ips = f.readlines()

print(ips)

excepts = []
res = []

for ip in ips:
    try:
        response = requests.get("http://" + ip[:-1], timeout=10)
        
        if(response.status_code >= 200 and response.status_code < 400):
            res.append(ip[:-1])

        else:
            excepts.append(ip[:-1])
        
        print(response.status_code)

    except Exception as e:
        if "HTTPS" not in str(e):
            excepts.append(ip[:-1])

        else:
            res.append(ip[:-1])

print("Exceptions >> " + str(excepts))
print("RESULTS >> " + str(res))


# excepts =  []

# errors = []
# for i in excepts:
#     print(i)

# print("\n\n\n\n\n")

# for i in errors:
#     print(i)
