# def item_in_common(list1, list2):
#     for i in list1:
#         for j in list2:
#             if i == j:
#                 return True
            
#     return False

# print(item_in_common([1,2,3],[3,4,5]))

def item_in_common(list1, list2):
    my_dict = {}

    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
        
    return False


print(item_in_common([1,2,3],[6,4,5]))