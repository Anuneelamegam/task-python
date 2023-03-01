def Remove(duplicate):
    final_arr = []
    for num in duplicate:
        if num not in final_arr:
            final_arr.append(num)
    return final_arr
     

duplicate = [ 5,4,10,20,4,6,10,39,4,39]
print(Remove(duplicate))
