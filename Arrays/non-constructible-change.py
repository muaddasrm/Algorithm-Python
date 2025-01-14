# def nonConstructibleChange(coins):
#     if not coins:
#         return 1
#     memory=coins.copy()
#     index=0
#     while index<len(coins):
#         for i in range(len(coins)):
#             if index == i:
#                 continue
#             sum = coins[index] + coins[i]
#             if sum not in memory:
#                 memory.append(sum)
#         index+=1
#     memory=sorted(memory)
#     for i in range(1,memory[-1]):
#         if i not in memory:
#             return i
#     return 1
##########################################################################
def nonConstructibleChange(coins):
    coins.sort()

    currentchnagecreated=0
    for coin in coins:
        if coin > currentchnagecreated+1:
            return currentchnagecreated+1
        currentchnagecreated+=coin
    return currentchnagecreated+1
        
