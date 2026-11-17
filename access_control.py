has_root_access = False
security_clearance = True
is_Auditor = False
if security_clearance and is_Auditor:
  print("Access Granted: Full Audit Mode")
else:
  print("Audit Access Denied.")
if has_root_access or security_clearance:
  print("System Control Portal Unlocked")
else:
  print("portal lockedown.")
if not is_Auditor:
  print("Standard User Profile Active")
