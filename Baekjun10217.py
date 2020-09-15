from heapq import *
input=__import__('sys').stdin.readline
for __ in range(int(input())):
    n,m,k=map(int,input().split())
    D=[[] for _ in range(n+1)]
    for i in range(k):
        u,v,c,d=map(int,input().split())
        D[u].append((v,c,d))
    S=[[float('INF')]*(m+1) for _ in range(n+1)]
    S[1][0]=0
    q=[]
    heappush(q,[0,0,1])
    while q:
        t,e,x=heappop(q)
        if S[x][e]!=t:continue
        for nx,ne,nt in D[x]:
            if ne+e<=m:
                if S[nx][ne+e]>nt+t:
                    S[nx][ne+e]=nt+t
                    heappush(q,[nt+t,ne+e,nx])
    k=min(S[n])
    print([k,'Poor KCM'][k==float('INF')])