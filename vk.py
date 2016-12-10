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
    	       
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return

   
    i=1
    while 1 :
        response = vk.account.setOnline()
        d = datetime.now()
        print i, "iteration"
        if response==1:
                print "Success"
        else:
                print "Failed, error:", response
                continue

        print d
        i = i+1
        printsleep(600)

    

if __name__ == '__main__':
   main()


