import sys
input = sys.stdin.readline

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            #'2' + '35' + '17', which results in '23517'.
            if '3' in str(i) + str(j) + str(k):
                count +=1
print(count)