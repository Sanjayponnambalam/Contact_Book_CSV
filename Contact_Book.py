import csv
import pandas as pd
file="Contact Book.csv"
data=[]
print("------------------------------------WELCOME TO YOUR CONTACT BOOK--------------------------------")
while True:
    import pandas
    choice=input("FEATURES\n1.Add New Contact(add)\n2.Search Contact(search)\n3.Display Contact(display)\n4.Edit Contact(edit)\n5.Delete Contact(del)\n6.Exit(exit)\n\n")
    if choice not in ['add','search','display','edit','del','exit']:
        print("Wrong Input!\n")
    if choice=="add":
        name=input("Enter Name: ")
        nom=input("Enter Contact Number : ")
        em=input("Enter email Address : ")
        data.append(name)
        data.append(nom)
        data.append(em)
        with open(file,'a') as f:
            write=csv.writer(f)
            write.writerow(data)
        print("Contact Added Successfully to the ContactBook\n\n")
        print("------------------------------------------------------------------------------------------------")
    elif choice=="search":
        search=input("Enter the Contact Name to be searched : ")
        search=search.lower()
        with open (file,'r') as f:
            read=csv.reader(f)
            for i,r,e in read:
                if i==search:
                    print("\nContact Name : ",i,"\nContact Number : ",r,"\nEmail Address : ",e,"\n")
                    break
        print("------------------------------------------------------------------------------------------------")     
                 
    elif choice=="display":
        p=pd.read_csv(file)
        if p is not False:
            print(p)
            print()
        else:
            print("No Contacts Available in Contact Book")
        print("------------------------------------------------------------------------------------------------")    

    elif choice=="edit":
        da=[]
        edit=input("Contact Name to be Edited : ")
        new=input("New Contact Number : ")
        newe=input("New Email Address : ")
        edit=edit.lower()
        da.append(edit)
        da.append(new)
        da.append(newe)
        index=0
        with open(file,'r')as f:
            read=csv.reader(f)
            lines=list(read)
            if edit in lines:
                for i,val in enumerate(lines):
                    index=i
                lines[index]=da
        with open(file,'w')as f1:
            write=csv.writer(f1)
            write.writerows(lines)
        print("\nContact Edited Successfully!\n")
        print("------------------------------------------------------------------------------------------------")
    elif choice=="del":

        dele=input("\nEnter the Contact name to be deleted : \n")
        dele=dele.lower()
        
        index=0
        with open(file,'r')as f:
            read=csv.reader(f)
            lines=list(read)
            if dele in lines:
                for dele,r in enumerate(lines):
                    index=i
            lines.pop(index)
               
        print("\nContact deleted successfully!\n")
        print("------------------------------------------------------------------------------------------------")
    elif choice=="exit":
        print("----------------------------------------THANK YOU-----------------------------------------------")
        break
    

                      
                    
        
        


           
