i = 3# i=3 到 i>0 的次数是三次
password = 'a123456'
while i > 0 : #有三次机会
	i = i - 1#剩余机会
	pwd = input('please input the password:')

	if pwd == 'a123456' :#succeed
	    print ('Congratulation! Log in successfully!')
	    break #to stop the code
	else :#fail
	    if i > 0 :
	        print('You have only', i ,'change!')
	    else :
		    break


# 0 to 3 and 3 to 0 的机会是一样的，要灵活运用顺序倒序
# print 中间加数字是comma
#灵活运用if

	   
	  
	      

