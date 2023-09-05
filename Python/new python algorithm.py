def insert_sort(ls):
    new_ls = []
    for i in range(len(ls)):
        new_ls.append(ls[i])
        for j in range(1,len(new_ls)):
            if new_ls[j] < new_ls[j-1]:
                new_ls[j],new_ls[j-1] = new_ls[j-1], new_ls[j]


    return new_ls
