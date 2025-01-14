def majorityElement(array):
    temp={}
    for i in range(len(array)):
        if array[i] not in temp:
            temp[array[i]]=1
        else:
            value=temp[array[i]]
            temp[array[i]]=value+1
    Keymax = max(zip(temp.values(), temp.keys()))[1]
    return Keymax
