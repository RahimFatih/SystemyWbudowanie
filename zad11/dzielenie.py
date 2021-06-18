a = [1,12,3,84,5,0,32,23,53,13,2,3,1,7,345,]
b = [9,12,3,122,3,0,-1,532,23,43,0,323,23,21,45]
for i,x in enumerate(a):
    try:
        print(x/b[i])
    except ZeroDivisionError:
        print("Pamiętaj kolego, nie dziel przez 0!")
