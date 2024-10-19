a=10
b=2
try:
    num=a/b
    res="El resultado es"+str(num)
except Exception as e:
    print("el error es:",e)
else:
    print(res)