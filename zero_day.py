node_id = input("Enter Node Identificaton: ")
node = input("Enter The Raw Packet Count Error For " +node_id+": ")
convert = int(node) // 4
administrative_privileges = True
emergency_override = True
auditor_flag = False
if (administrative_privileges or emergency_override) and not auditor_flag:
  print("Access Granted")
else:
  print("Access Denied")
if convert > 3:
  print("IT IS LOCKED:More  Than 3 Attempt")
elif convert == 2:
  print("ONE MORE ATTEMPT:Your Locked")
else:
  print("TWO OR MORE:You will be locked")
print(node_id,node,convert)
