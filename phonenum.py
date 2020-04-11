def phonenum():
    CN_mobile = ['134', '135', '136', '137', '138', '139', '150', '151', '152', '157','158', '159', '182', '183', '184', '187', '188', '147', '178', '1705']
    CN_union = ['130', '131', '132', '155', '156', '185', '186', '145', '176', '1709']
    CN_telecom = ['133', '153', '180', '181', '189', '177', '1700']
    num=input('请输入电话号码：')
    number=num[:3]
    phonenumnber=int(num)
    if len(num)==11 and number in CN_mobile:
        print(num+'中国移动')
    elif len(num)==11 and number in CN_union:
        print(num + '中国联通')
    elif len(num)==11 and number in CN_telecom:
        print(num + '中国电信')
    elif len(num)!=11:
        print('输入电话格式不对')
    else:
        print('电话号码不在中国区')
    return phonenum()
print(phonenum())