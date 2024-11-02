def add_contact():
    Name=input("Enter a contact Name : ")
    while True:
        try:
            Num=int(input("Enter a contact number : "))
        except Exception:
            print("Somthing Went Wrong!")
            continue
        if len(str(Num))!=10:
            print("Phone Number Has 10 Digits PLease enter Correctly!")
            continue
        if Num in Phone_book.values():
            print("This Number is Already Saved! Do You Enter Choice:2 to Check it?!")
            return
        Phone_book[Name]=Num
        print("Contact added successfully!")
        break

def view_contact():
    if len(Phone_book)==0:
        print("Phone Book Is Empty!")
    else:
        a=1
        for i in Phone_book:
            print(a,".","Name:",i,"=> Number:",Phone_book[i])
            a+=1
def edit_contact(): 
    while True:
        try:
            want=int(input("Which You Want To Edit? Name or Mobile Number? Enter 0 to Change Name or Enter 1 to Change Mobile Number : "))
            print()
        except:
            print("Something Went Wrong!!!")
            continue
        while True:
            if want==0:
                o_n=input("Enter Old Name Saved in Phone Book : ")
                n_n=input("Enter New Name to Change : ")
                try:
                    Phone_book[n_n]=Phone_book[o_n]
                    del Phone_book[o_n]
                    print("Name",o_n,"was Sucessfully Changed to",n_n,".")
                    return
                except Exception:
                    print("Please Enter a Old Name Correctly As In You Saved In Phonebook")
            elif want==1:
                num_name=input("Enter The Contact Name to Change Number : ")
                while True:
                    try:
                        new_num=int(input("Enter a number to Change : "))
                    except Exception:
                        print("Somthing Went Wrong!")
                        continue
                    if len(str(new_num))!=10:
                        print("Phone Number Has 10 Digits PLease enter Correctly!")
                        continue
                    if new_num in Phone_book.values():
                        print("This Number is Already Saved! Do You Enter Choice:2 to Check it?!")
                        return
                    break
                try:
                    Phone_book[num_name]=new_num
                    print("Number was Sucessfully Changed to",Phone_book[num_name])
                    return
                except Exception:
                    print("Please Enter a Name Correctly As You Saved In Phonebook")
                    continue
            else:
                print("Please Enter 0 or 1")

def del_contact():
    name_=input("Enter a Contact Name to Delete : ")
    try:
        del Phone_book[name_]
        print("Contact was Sucessfully Deleted.")
        return
    except Exception:
        print("This Contact is Not Available in Phone Book")
        return
def Exit():
    print("Thanks for Used Our Phone Book! Bye",chr(2))
    exit()

print("Contact Book Application:\n1. Add Contact\n2. View Contacts\n3. Edit Contact\n4. Delete Contact\n5. Exit")
Phone_book={}
while True:
    try:
        print()
        Choice=int(input("ENTER YOUR CHOICE: "))
        print()
    except Exception:
        print("Somthing Went Wrong! Please Enter a Choice as a Number 1 to 5")
        continue
    if Choice==1:
        add_contact()
    elif Choice in [2,3,4,5]:
        if Choice==2:
            view_contact()
        elif Choice==3:
            edit_contact()
        elif Choice==4:
            del_contact()
        elif Choice==5:
            Exit()
    else:
        print("Please Enter a Choice 1 to 5 !!!")
