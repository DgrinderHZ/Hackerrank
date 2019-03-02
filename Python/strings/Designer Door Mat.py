# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = tuple(map(int, input().split()))

res = ""
for i in range(n//2):
    hyphen = (m - (2*i+1) * 3) // 2
    temp = ".|."
    res += hyphen * "-"+ temp * (2*i+1) + hyphen * "-" + "\n"

print(res,  end='') 

hyphen_welcom = (m - 7) // 2

print( hyphen_welcom * "-" + "WELCOME" + hyphen_welcom * "-"  )
res = res[:len(res)-1]
print(res[::-1]) 


