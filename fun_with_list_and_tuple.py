
List =[(10, 7), (18, 3), (50, 12), (84, 2)]
listLen = len(List); 
for i in range(0, listLen):
    for j in range(0, listLen - i - 1):
        if(List[j][-1] > List[j + 1][-1]):
            swap = List[j]
            List[j] = List[j + 1]
            List[j + 1] = swap
print(" Tuple after sorting : " + str(List))