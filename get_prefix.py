def get_prefix(strs):
    prefix=''
    prefix_list=[]
    sorted_list = sorted(strs, key=len)
    new_list = []
    for i in sorted_list:
        new_list.append(list(i))
    # print(new_list)
    for x in range(len(new_list)-1):
        for j in range(len(new_list[x])):
            if new_list[x][j] == new_list[x+1][j]:
                prefix += new_list[x][j]
        prefix_list.append(prefix)
        prefix =''
        return min(prefix_list, key=len)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
        print(prefix_list)
                

strs = ['start', 'stair', 'step']
# strs = ['start', 'wework', 'today']
get_prefix(strs)