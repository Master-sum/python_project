def name01():
    for name1 in range(1, 11):
        name=str(name1)
        op_path=r'C:\Users\polo1\Desktop\python书籍\ '
        full=op_path+name+'.txt'
        file=open(full,'w')
        file.close()
        print('Done')
print(name01())