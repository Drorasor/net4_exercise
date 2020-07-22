
def menu():
    while(True):
        choice=input("Menu:\n1.serch for URL \n2.add URL and IP \n3.delete IP from URL\n4.update the ip address of a specific URL\n5. print dict\n")
        if(choice=="1"):
            serch_url()
        elif(choice=="2"):
            add_url_ip()
        elif(choice=="3"):
            delete_url()
        elif(choice=="4"):
            update_ip()
        elif(choice=="5"):
            print_dict()
        else:
            print("Enter 1-5 only!!!\n")
            continue
        if(input("\nDo you want to exit? y/n\n")=="y"):
            break
    print("\nThanks and bye bye...\n")\


def serch_url():
    serch= input("please serch for a URL\n")
    if serch in url_dict:
        print("This URL is in the list")
    else:
        print("This URL is not in the list")


def add_url_ip():
    x = input("please enter URL\n")
    y = input("please enter IP address\n")
    url_dict[x] = y
    print("your new URL dict is\n" + str(url_dict))



def delete_url():
    print("this is the URE list\n ")
    print(url_dict)
    x = input("please choose one URL to delete from the dict above\n")
    url_dict.pop(x)
    print("new dict:\n" + str(url_dict))



def update_ip ():
    print("let's update the IP add to your choosen URL, this is the dict: \n" + str(url_dict))
    x = input("choose URL")
    url_dict.update({x: input("writ a new IP add")})
    print("new dict\n" + str(url_dict))


def print_dict():
    print(url_dict)





url_dict={
    "www.ynet.co.il" : "192.168.1.1",
    "www.google.com" : "192.168.1.2",
    "www.one.com" : "192.168.1.3" ,
    "www.calcalist.co.il" : "192.168.1.4",
    "www.mako.com" : "192.168.1.5"
}

menu()
