'''

这个地方封装的是接口的请求参数信息

'''
#   1  查询用户行为轨迹接口数据************************************************************************************

tokenRight="Bearer 397a8491-ef14-4f8c-9844-5b1effa4c102" #测试之前抓取一个正确的token值(最好用登录接口抓取)

tokenLate="Bearer f36f1500-5216-428f-8f9a-4f56784f259f" #过期的token

nullParameter="" #空的token值

tokenWrong="Bearer ec608034-3fac-4a54-a4b3-239dcb76666" #错误的token值

def paraMeter1():

    paraMeter1=(
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenWrong, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenLate, 'customerId': nullParameter, 'code': "900"},
        {'Authorization': tokenRight, 'customerId': nullParameter, 'code': "200"},
        {'Authorization': tokenRight, 'customerId': '480', 'code': "200"},
        {'Authorization': tokenRight, 'customerId': '92233720368547758070', 'code': "500"},
        {'Authorization': tokenRight, 'customerId': '你好', 'code': "500"},
        {'Authorization': tokenRight, 'customerId': 'ABC', 'code': "500"}
    )


    return paraMeter1

#*****************************************************************************************************

queryType='1'
customerName=''
empId=''
customerSource=''
customerFollowStateId=''
followLatestTimeStart=''
followLatestTimeEnd=''
code='200'

queryType1='2'
customerName1=''
empId1=''
customerSource1=''
customerFollowStateId1=''
followLatestTimeStart1=''
followLatestTimeEnd1=''
code1='200'

queryType2='3'
customerName2=''
empId2=''
customerSource2=''
customerFollowStateId2=''
followLatestTimeStart2=''
followLatestTimeEnd2=''
code2='200'

queryType3='A'
customerName3=''
empId3=''
customerSource3=''
customerFollowStateId3=''
followLatestTimeStart3=''
followLatestTimeEnd3=''
code3='500'

queryType4='2'
customerName4='博文.夏'
empId4='881'
customerSource4='866'
customerFollowStateId4='353'
followLatestTimeStart4='biyvyx'
followLatestTimeEnd4='ynaiik'
code4='200'

queryType5='2'
customerName5='博文.夏'
empId5='A'
customerSource5='866'
customerFollowStateId5='353'
followLatestTimeStart5='biyvyx'
followLatestTimeEnd5='ynaiik'
code5='500'

def paraMeter2():

    paraMeter1=(
        {'queryType': queryType, 'customerName': customerName,'empId':empId,'customerSource':customerSource,
         'customerFollowStateId':customerFollowStateId,'followLatestTimeStart':followLatestTimeStart,
         'followLatestTimeEnd':followLatestTimeEnd,'code': code,'Authorization': nullParameter},

        {'queryType': queryType1, 'customerName': customerName1, 'empId': empId1, 'customerSource': customerSource1,
         'customerFollowStateId': customerFollowStateId1, 'followLatestTimeStart': followLatestTimeStart1,
         'followLatestTimeEnd': followLatestTimeEnd1, 'code': code1,'Authorization': nullParameter},

        {'queryType': queryType2, 'customerName': customerName2, 'empId': empId2, 'customerSource': customerSource2,
         'customerFollowStateId': customerFollowStateId2, 'followLatestTimeStart': followLatestTimeStart2,
         'followLatestTimeEnd': followLatestTimeEnd2, 'code': code2,'Authorization': nullParameter},

        {'queryType': queryType3, 'customerName': customerName3, 'empId': empId3, 'customerSource': customerSource3,
         'customerFollowStateId': customerFollowStateId3, 'followLatestTimeStart': followLatestTimeStart3,
         'followLatestTimeEnd': followLatestTimeEnd3, 'code': code3,'Authorization': nullParameter},

        {'queryType': queryType4, 'customerName': customerName4, 'empId': empId4, 'customerSource': customerSource4,
         'customerFollowStateId': customerFollowStateId4, 'followLatestTimeStart': followLatestTimeStart4,
         'followLatestTimeEnd': followLatestTimeEnd4, 'code': code4,'Authorization': nullParameter},

        {'queryType': queryType5, 'customerName': customerName5, 'empId': empId5, 'customerSource': customerSource5,
         'customerFollowStateId': customerFollowStateId5, 'followLatestTimeStart': followLatestTimeStart5,
         'followLatestTimeEnd': followLatestTimeEnd5, 'code': code5,'Authorization': nullParameter},
    )


    return paraMeter1


#*****************************************************************************************************
customerId=''
content=''
code_1='200'

customerId1='650870476872224768'
content1=''
code1_1='200'


customerId2='650870476872224768'
content2='3jgw8a'
code2_1='200'

customerId3='92233720368547758070'
content3='3jgw8a'
code3_1='500'

customerId4='A'
content4='3jgw8a'
code4_1='500'

customerId5='你好'
content5='3jgw8a'
code5_1='500'

customerId6='444'
content6='444'
code6_1='500'

def paraMeter3():

    paraMeter1=(
        {'customerId':customerId,'content':content,'Authorization': tokenRight,'code':code_1},
        {'customerId':customerId1, 'content':content1,'Authorization': tokenRight,'code':code1_1},
        {'customerId': customerId2, 'content': content2,'Authorization': tokenRight,'code':code2_1},
        {'customerId': customerId3, 'content': content3,'Authorization': tokenRight,'code':code3_1},
        {'customerId': customerId4, 'content': content4,'Authorization': tokenRight,'code':code4_1},
        {'customerId': customerId5, 'content': content5,'Authorization': tokenRight,'code':code5_1},
        {'customerId': customerId6, 'content': content6,'Authorization': tokenRight,'code':code6_1},



    )
    return paraMeter1



#*****************************************************************************************************
customerIda_1=''
codea_1='200'

customerIda_2='650870476872224768'
codea_2='200'

customerIda_3='92233720368547758070'
codea_3='500'

customerIda_4='A'
codea_4='500'

customerIda_5='你好'
codea_5='500'







def paraMeter4():

    paraMeter1=(
        {'customerId':customerIda_1,'Authorization': tokenRight,'code':codea_1},
        {'customerId':customerIda_2,'Authorization': tokenRight,'code':codea_2},
        {'customerId': customerIda_3,'Authorization': tokenRight,'code':codea_3},
        {'customerId': customerIda_4, 'Authorization': tokenRight,'code':codea_4},
        {'customerId': customerIda_5, 'Authorization': tokenRight,'code':codea_5}



    )
    return paraMeter1



#*****************************************************************************************************
id_29='188'
content_29='rl6u1q'
empId_29='219'
code_29='200'

id_29_1='A'
content_29_1='rl6u1q'
empId_29_1='219'
code_29_1='500'

id_29_2='188'
content_29_2='rl6u1q'
empId_29_2='A'
code_29_2='500'

id_29_3='A'
content_29_3='rl6u1q'
empId_29_3='A'
code_29_3='500'

id_29_4='188'
content_29_4='rl6u1q'
empId_29_4='92233720368547758070'
code_29_4='500'

#令牌信息错误
id_29_5='188'
content_29_5='rl6u1q'
empId_29_5='219'
code_29_5='900'


#令牌信息失效
id_29_6='188'
content_29_6='rl6u1q'
empId_29_6='219'
code_29_6='900'





def paraMeter5():

    paraMeter1=(
        {'id':id_29,'content':content_29,'empId':empId_29,'Authorization': tokenRight,'code':code_29},
        {'id':id_29_1,'content':content_29_1,'empId':empId_29_1,'Authorization': tokenRight,'code':code_29_1},
        {'id':id_29_2,'content':content_29_2,'empId':empId_29_2,'Authorization': tokenRight,'code':code_29_2},
        {'id':id_29_3,'content':content_29_3,'empId':empId_29_3,'Authorization': tokenRight,'code':code_29_3},
        {'id':id_29_4,'content':content_29_4,'empId':empId_29_4,'Authorization': tokenRight,'code':code_29_4},
        {'id':id_29_5, 'content':content_29_5, 'empId':empId_29_5, 'Authorization':tokenWrong, 'code':code_29_5},
        {'id':id_29_6, 'content':content_29_6, 'empId':empId_29_6, 'Authorization':tokenLate, 'code':code_29_6},

    )
    return paraMeter1

#*****************************************************************************************************

#未授权
'''


未授权暂时无法给数据测试


'''





#*****************************************************************************************************
id_37=''
code_37='200'

#id不存在
id_37_1='168'
code_37_1='200'

id_37_2='288'
code_37_2='200'

id_37_3='A'
code_37_3='500'

id_37_4='92233720368547758070'
code_37_4='500'








def paraMeter6():

    paraMeter1=(
        {'id':id_37,'Authorization': tokenRight,'code':code_37},
        {'id': id_37_1, 'Authorization': tokenRight, 'code': code_37_1},
        {'id': id_37_2, 'Authorization': tokenRight, 'code': code_37_2},
        {'id': id_37_3, 'Authorization': tokenRight, 'code': code_37_3},
        {'id': id_37_4, 'Authorization': tokenRight, 'code': code_37_4}

    )
    return paraMeter1


#*****************************************************************************************************
code_43='200'

code_43_1='900'

code_43_2='900'


def paraMeter7():

    paraMeter1=(
        {'Authorization': tokenRight,'code':code_43},
        {'Authorization': tokenLate, 'code': code_43_1},
        {'Authorization': tokenWrong, 'code': code_43_2},

    )
    return paraMeter1




code_45='200'

code_45_1='900'

code_45_2='900'

#*****************************************************************************************************
def paraMeter8():

    paraMeter1=(
        {'Authorization': tokenRight,'code':code_45},
        {'Authorization': tokenLate, 'code': code_45_1},
        {'Authorization': tokenWrong, 'code': code_45_2},

    )
    return paraMeter1
#*****************************************************************************************************

id_48=''
code_48='200'


id_48_1='666'
code_48_1='200'

id_48_2='820'
code_48_2='900'

id_48_3='ABC'
code_48_3='500'

id_48_4='92233720368547758070'
code_48_4='500'



def paraMeter9():

    paraMeter1=(
        {'id':id_48, 'Authorization': tokenRight,'code':code_48},
        {'id':id_48_1, 'Authorization': tokenRight, 'code': code_48_1},
        {'id':id_48_2,'Authorization': tokenRight, 'code': code_48_2},
        {'id': id_48_3, 'Authorization': tokenRight, 'code': code_48_3},
        {'id': id_48_4, 'Authorization': tokenRight, 'code': code_48_4}

    )
    return paraMeter1





#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************
#*****************************************************************************************************


