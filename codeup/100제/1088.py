data = int(input())
return_data = str()

for a in range(1,data+1):
    if a % 3 != 0:
        return_data = return_data + str(a) + str(' ')

print(return_data)