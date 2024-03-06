def checkstring(st1,st2,st3):
    return st1.startswith(st2) or st1.endswith(st3)
 
st1="Python Programming"
st2="Py"
st3="ming"
print(checkstring(st1,st2,st3))
 
st1="Python Programming"
st2="PY"
st3="MING"
print(checkstring(st1,st2,st3))