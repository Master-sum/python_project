def list_index():
    CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152,152,157,158,159,182,183,184, 187,188,147,178,1705]
    CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
    a=input('请输入电话号码：')
    b=a[:3]
    c=int(b)
    if len(a)==11 and c in CN_union:
        print(a+' 中国联通')
    elif len(a)==11 and c in CN_mobile:
        print(a+' 中国移动')
    elif len(a)==11 and c in CN_telecom:
        print(a+' 中国电信')
    elif len(a)!=11:
        print('输入格式有误：')
    else:
        print('输入非中国电话号码')
    print(list_index())
print(list_index())