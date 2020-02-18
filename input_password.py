i = 3# i=3 到 i>0 的次数是三次
password = 'a123456'
while i > 0 : #有三次机会
	
	pwd = input('please input the password:')

	if pwd == 'a123456' :
	    print ('Congratulation! Log in successfully!')
	    break #to stop the code
	else :
	    i = i - 1#剩余机会
	    print('You have only', i ,'change!') 
	   
	  
	      

