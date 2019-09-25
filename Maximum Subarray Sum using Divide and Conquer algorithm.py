def midlargest(S, li, ri, mi):
  ls=0
  sl=0
  leftl=0
  ll=[]
  rs=0
  sr=0
  rightl=0
  for i in range (mi, li-1, -1):
    sl+=S[i]
    if sl>ls:
      ls=sl
      leftl=i
  
  for i in range (mi+1,ri+1):
    sr+=S[i]
    if sr>rs:
      rs=sr
      rightl=i

  for i in range (leftl, rightl+1):
    ll.append(S[i])  
  print("maxs=",ls,"+",rs)
  maxs=ls+rs
  print("mid",maxs,ll)
  return (maxs,ll)

def sublargest(S,li,ri):
  if li==ri:
    print("ls",S[li],[S[li]])
    return (S[li],[S[li]])
  mi = (li+ri)//2

  return max(sublargest(S,li,mi),sublargest(S,mi+1, ri), midlargest(S,li,ri,mi))

S=[88,12,-6,10,-5,2]
n=len(S)
print(sublargest(S,0,n-1))
  
