def mutiply(n1,n2):  
 if is_number(n1) and is_number(n2):
   return float(n1) + float(n2)
 else:
   return None
  
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
