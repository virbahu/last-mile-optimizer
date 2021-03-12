import numpy as np
def savings_algorithm(depot, customers, demands, capacity, coords):
    n=len(customers); dist=lambda a,b: np.linalg.norm(coords[a]-coords[b])
    savings=[]
    for i in range(n):
        for j in range(i+1,n):
            s=dist(depot,customers[i])+dist(depot,customers[j])-dist(customers[i],customers[j])
            savings.append((s,i,j))
    savings.sort(reverse=True)
    routes=[[c] for c in customers]; route_of={c:i for i,c in enumerate(customers)}
    for s,i,j in savings:
        ci,cj=customers[i],customers[j]
        ri,rj=route_of[ci],route_of[cj]
        if ri==rj: continue
        load_i=sum(demands[c] for c in routes[ri]); load_j=sum(demands[c] for c in routes[rj])
        if load_i+load_j>capacity: continue
        if routes[ri][-1]==ci and routes[rj][0]==cj:
            routes[ri].extend(routes[rj])
            for c in routes[rj]: route_of[c]=ri
            routes[rj]=[]
    return [r for r in routes if r]
if __name__=="__main__":
    np.random.seed(42); n=8
    coords={0:np.array([50,50])}
    for i in range(1,n+1): coords[i]=np.random.rand(2)*100
    demands={i:np.random.randint(5,20) for i in range(1,n+1)}
    routes=savings_algorithm(0,list(range(1,n+1)),demands,50,coords)
    print("Routes:",routes)
