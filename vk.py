# -*- coding: utf-8 -*-


import vk_api
import time
import getpass

def auth_handler():
    print "введите код"
    a = raw_input()
    return a,True;

def main():
    
    print "Login"
    login = raw_input()
    password = getpass.getpass()
    vk_session = vk_api.VkApi(login,
                  password,
                  auth_handler=auth_handler)

    try:
    	vk_session.authorization()
    	       
     vk = vk_session.get_api()

    i=1
    while 1 :
        response = vk.account.setOnline()
        d = datetime.now()
        print i, "iteration"
        if response==1:
                print "Success"
        else:
                print "Failed, error:", response
                time.sleep(30)
                continue

        print d
        i = i+1
        print

        time.sleep(600)

    

if __name__ == '__main__':
   main()


