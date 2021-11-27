arr_exp = [2200, 2350, 2600, 2130, 2190]
print (" in feb we have spent", arr_exp[1] - arr_exp[0])
print( " quarter avg", arr_exp[0] + arr_exp[1] + arr_exp[2])

print(" did i spend 2000 in any month?", 2000 in arr_exp)


arr_exp.append(1980)
print (arr_exp)

arr_exp[3] = arr_exp[3] - 200
print(arr_exp[3])
