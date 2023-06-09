def binSearch(list1,num):
    low,high = 0,len(list1)-1
    while low<=high:
        mid = int((low+high)/2)
        if list1[mid]>num:
            answer = mid
            high = mid-1
        else:
            low = mid+1
    return answer

for _ in range(int(input())):
    n = int(input())
    input_list = list(map(int,input().split()))
    list1 = [input_list[0]]
    for i in range(1,len(input_list)):
        if input_list[i] >= list1[-1]:
            list1.append(input_list[i])
        else:
            list1[binSearch(list1,input_list[i])] = input_list[i]
    print(len(list1),*list1)


