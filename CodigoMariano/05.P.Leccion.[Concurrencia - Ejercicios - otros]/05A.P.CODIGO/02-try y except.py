a=10
b=2
try:
    num=a/b
    res="El resultado es"+num
    print(res)
except ZeroDivisionError:
    print("Error, no se puede dividir por cero" )
except Exception as e:
    print("Hay otro error y es:",e)
