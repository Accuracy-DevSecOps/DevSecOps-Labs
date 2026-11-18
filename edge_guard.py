integrity = input("Enter ID: ")
payload = input("Enter The Packet Size: ")
identifier = input("Enter Validation check: ")
length = len(identifier)
size = int(payload) 
if size % 3 == 0:
    print("The Node Is Secure")
elif size % 3 == 1:
    print("Node Secured")
else:  
    print("WARNING!!!:System Breach")
    print(integrity,payload,identifier,length,size) 