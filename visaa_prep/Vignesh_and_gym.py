B,R,V=map(int,input().split())
if B+R<=V:
    print(2)
elif B<=V:
    print(1)
else:
    print(0)
