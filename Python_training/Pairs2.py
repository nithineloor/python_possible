List_A = []
List_B = []
i = 0
while i != 10:
    x = int(input())
    List_A.append(x)
    i = i+1
i = 0
while i != len(List_A):
    f = List_A[i] % 2
    if f == 0:
        List_B.append(List_A[i])
    i = i+1
print(List_B)