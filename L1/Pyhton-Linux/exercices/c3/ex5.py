# print(1200%100)
# a = 2
# if(a%100):
#     if(a%400):
#         r = True
#     else:
#         r = False
# else:
#     if(a%4 == 0):
#         r = True
#     else:
#         r= False
a = int(input('année'))
if((a%100 ==0 and a%400 ==0) or (not(a%100 == 0) and a%4 == 0)):
    print('bissextile')
else:
    print('non')
