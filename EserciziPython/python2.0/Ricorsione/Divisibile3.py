def divisibile3(n):
    if n<10:
        return n%3==0
    else:
        return divisibile3(sum(map(int,str(n))))




