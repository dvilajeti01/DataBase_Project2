def add_instructor(ID,name,dept_name)
    cursor.execute("use university")
    cursor.execute("insert into instructor values(",ID,",'",name,"','"dept_name,"');")

def search_department()
    cursor.execute("use universtiy")
    cursor.execute("select dept_name,building,budget,name from instructor natural join department")
    for n in cursor.fetchall():
    print (n[0])

    return;

def search_instructor(ID)
    cursor.execute("use universtiy")
    cursor.execute("select ID,name,dept_name,building from instructor natural join department where ID = ",ID)
    for n in cursor.fetchall():
    print (n[0])

    return;
    
    

def switch(choice)
    switcher = {
        1: ID = input("Enter instructor ID you are looking for"
           search_instructor(ID),
        2: dept_name = input("Enter the department name you are looking for: ")
           search_department(dept_name),
        3: ID = input("Enter the instructor ID:)
           name = input("Enter the name of the instructor: ")
           dept_name = input("Enter the name of the department: ")
           add_instructor(ID,name,dept_name),
        4: break
        }
    

def main_interface():

    print("===================================================================")
    print("\t  WELCOME TO MANHATTAN COLLEGE DATABASE \t")
    print("===================================================================")

    print("MENU") 
    print("1. ENTER INSTRUCTOR ID FOR MORE INFO")
    print ("2. ENTER DEPARTMENT ID FOR MORE INFO")
    print ("3. ENTER NEW INSTRUCTOR TO DATABASE")
    print ("4. EXIT")

    choice = input("Please select option: )

    switch(choice)
    

    return;

    
main_interface()
