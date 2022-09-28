str = "3,5,7-10,11"
str = str.split(",")

pages = []

for i in str:
    if '-' in i:
        start = int(i[0:i.index("-")])
        end = int(i[i.index("-")+1:len(i)])
        for j in range(start, end+1):
            pages.append(j)
    else:
        pages.append(int(i))
        
print(pages)