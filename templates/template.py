# template='''
# 尊敬的%s:
#     我们将于%s在%s举办毕业典礼,邀请您作为这次典礼的观礼嘉宾
#                                                 %s
# '''
# print(template%('懒洋洋','1222-02-02','羊村大酒店','灰太狼'))


template='''
尊敬的%(name)s:
    我们将于%(time)s在%(address)s举办毕业典礼,邀请您作为这次典礼的观礼嘉宾
                                                %(yours)s
'''
print(template%{'name':"懒洋洋",'time':'1222-02-02','address':'羊村大酒店','yours':'灰太狼'})

