
def menu():
    while(True):
        choice=input("Menu:\n1.serch for IP \n2.delete one ip \n3.add new ip to the list\n4. print ip to the screen\n")
        if(choice=="1"):
            serch_ip()
        elif(choice=="2"):
            delete_ip()
        elif(choice=="3"):
            add_new_ip()
        elif(choice=="4"):
            print_ip_screen()
        else:
            print("Enter 1-4 only!!!\n")
            continue
        if(input("\nDo you want to exit? y/n\n")=="y"):
            break
    print("\nThanks and bye bye...\n")\


def serch_ip():
    new_ip = input("\nlet's serch IP address")
    if (new_ip in ip) == True:
        print("This IP is in the list")
    else:
        print("This ip is available\nAdding to the list")


def delete_ip():
    delete=input(("please choose one ip to delete\n"))
    if (delete in ip) == True:
        ip.remove(delete)
        print(ip)



def add_new_ip():
    new=input("add another ip\n")
    ip.append(new)
    print(ip)



def print_ip_screen():
    print("this is your new IP list: \n")
    print(ip)





ip=[]
for i in range(6):
    ip.append(input("Please insert an IP address:"))
menu()


