i = 0
List_A = []
List_B = []
while i != 5:
    x = int(input())
    y = int(input())
    List_A.append(x)
    List_B.append(y)
    i = i+1
print(List_A)
print(List_B)
List_C = []
i = 0
while i != 5:
    f = List_A[i] * List_B[i]
    List_C.append(f)
    i = i+1
print(List_C)