def max(list):
    a=list[0]
    for i in range(0,len(list)):
        if list[i]>a:
            a=list[i]
    return a
def minimum(list):
    a=list[0]
    for i in range(0,len(list)):
        if list[i]<a:
            a=list[i]
    return a
def sum(list):
    s=0
    for i in range(0,len(list)):
        s=s+list[i]
    return s
def average(list):
    s1=sum(list)
    avg=s1/len(list)
    return avg

    

