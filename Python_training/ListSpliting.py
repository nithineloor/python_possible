listA = [844,213,914,906,238,831,972,576,154,37,616,116,683,546,650,395,634,583,765,599,477,26,150,781,539,602,884,988,291,807,581,21,588,219,963,457,229,295,502,457,914,574,700,908,307,129,422,315,628,548,370,506,876,741,211,751,699,321,150,849,401,545,621,484,481,883,922,521,218,108,41,402,371,800,387,559,783,920,734,519,446,293,801,86,669,175,194,608,389,131,962,714,504,665,985,213,388,231,998,448]
listB = []
listC = []
listD = []
listE = []
listA.sort()
j = 0 
print('ListB')
while j != 25:
    listB.append(listA[j])
    j=j+1
print(listB)
print(len(listB))

k = 25 
print('ListC')
while k != 50:
    listC.append(listA[k])
    k=k+1
print(listC)
print(len(listC))

y = 50 
print('ListD')
while y != 75:
    listD.append(listA[y])
    y=y+1
print(listD)
print(len(listD))

p = 75 
print('ListE')
while p != 100:
    listE.append(listA[p])
    p=p+1
print(listE)
print(len(listE))