con = mysql.connector.connect(user='root',password='root',host='127.0.0.1',port='3306')

cursor = con.cursor()

#create database and table
#cursor.execute("drop database university;")    #carry out every run after initial run of program
cursor.execute("create database university;")
cursor.execute("use university;")
cursor.execute("create table department(dept_name varchar(10), building varchar(30), budget int, primary key(dept_name));")
cursor.execute("create table instructor(ID int, name varchar(30), dept_name varchar(10), primary key (ID), foreign key (dept_name) references department(dept_name) on delete set null);")

#department insert statements
cursor.execute("insert into department values('CMPT', 'RLC', 75000);")
cursor.execute("insert into department values('MATH', 'RLC', 55000);")
cursor.execute("insert into department values('BIOL', 'LEO', 60000);")

#instructor insert statements
cursor.execute("insert into instructor values(1001, 'Robert Smith', 'CMPT');")
cursor.execute("insert into instructor values(1002, 'Natasha Anderson', 'MATH');")
cursor.execute("insert into instructor values(1003, 'James Nassimi', 'BIOL');")
cursor.execute("insert into instructor values(1004, 'Guiling Wei', 'CMPT');")
cursor.execute("insert into instructor values(1005, 'Mary Harnett', 'BIOL');")
cursor.execute("insert into instructor values(1006, 'David Ochs', 'CMPT');")
con.commit()


#checks if department entered exists in the database
def existing_dept(dept_name):
    cursor.execute("select dept_name from department where dept_name = '"+dept_name+"';")
    if cursor.fetchone() is None:   #if department does not exist, return false
        return False;
    return True;    #if department appears in table, return true

#checks if ID entered exists in the database
def existing_instr(ID):
    cursor.execute("select ID from instructor where ID = "+ID+";")
    if cursor.fetchone() is None:   #if ID does not exist, return false
        return False;
    return True;   #if ID entered is in the table



#**************************************CHOICE 1***************************************#
#first menu item, searches instructor ID in instructor table and returns associated info
def search_instructor(ID):
    if existing_instr(ID) != True:
        print("The ID does not appear in the database.")
        return;
    
    query = "select ID,name,dept_name,building from instructor natural join department where ID = " +ID+";"
    cursor.execute(query)
    for n in cursor:
        print("ID: ",n[0])
        print("NAME: ", n[1])
        print("DEPT: ", n[2])
        print("BUILDING: ", n[3])
    return;

#**************************************CHOICE 2***************************************#
#second menu item, searches department name in department table and returns associated info
def search_department(dept_name):
    #checks if department exists in database
    if existing_dept(dept_name) != True:
        print("The department name does not appear in the database.")
        return;

    #shortened queries
    deptInfoQuery = "select dept_name, building, budget from department where dept_name = '" +dept_name+"';"
    instrInfoQuery = "select distinct name from instructor natural join department where dept_name = '" +dept_name+"';"

    #if department exists, carry out search
    cursor.execute(deptInfoQuery)   #display department info once
    for n in cursor:
        print("DEPT: ", n[0])
        print("LOCATION: ", n[1])
        print("BUDGET: ", n[2])

    cursor.execute(instrInfoQuery)  #display instructors' names
    print("NAMES OF INSTRUCTORS: ")
    for n in cursor:
        print(" ", n[0])
    return;

#**************************************CHOICE 3***************************************#
#third menu item, inserts new instructor info given it follows all requirements
def add_instructor(ID,name,dept_name):
    #checks if ID entered is a duplicate or not
    if existing_instr(ID) == True:
        print("Instructor ID already exists in the file.")
        return;
    #checks if dept_name entered is an existing department
    if existing_dept(dept_name) != True:
        print("The department does not exist and hence the instructor record cannot be added to the database")
        return;

    #if both requirements are met, a new instructor will be added
    cursor.execute("insert into instructor values("+ID+", '"+name+"', '"+dept_name+"');")
    cursor.nextset()
    return;


                      
def main_interface():
    another = True  #allows user to choose multiple menu items
    while another:
        print("===================================================================")
        print("\t  WELCOME TO MANHATTAN COLLEGE DATABASE \t")
        print("===================================================================")

        print("MENU") 
        print("1. ENTER INSTRUCTOR ID FOR MORE INFO")
        print ("2. ENTER DEPARTMENT NAME FOR MORE INFO")
        print ("3. ENTER NEW INSTRUCTOR TO DATABASE")
        print ("4. EXIT")
        
        choice = input("Please select option: ")
        if choice == '1':
            ID = input('Enter instructor ID: ') 
            search_instructor(ID)   #calls instructor search function w/ user input
        elif choice == '2':
            dept_name = input('Enter department name: ')
            search_department(dept_name)    #calls department search function w/ user input
        elif choice == '3':
            ID = input('Enter instructor ID: ')
            name = input('Enter instructor name: ')
            dept_name = input('Enter department name: ')
            add_instructor(ID, name, dept_name) #calls add instructor function w/ user input
        else:
            print("END")
            break

        a = input("Another choice?(y/n): ") #if user wants to choose another menu item
        if (a == 'y'):
            another = True
        elif(a == 'n'):
            another = False   
            
main_interface()


cursor.close()
con.close()



