print("STUDENT MANAGEMENT SYSTEM")

from db import conn, cursor 


def add_student():
    roll_no = input("Enter Roll_no ")
    name = input("Enter Name ")
    dob = input("Enter DOB ")
    st_class = input("Enter Student's Class ")
    age = input("Enter Age ")
    
    # Validation
    if not roll_no or not name or not dob or not st_class or not age:
        print("All fields are required!")
        return
    
    if not roll_no.isdigit():
        print("Roll number must be in numeric !")
        return
    
    if not name.replace(" ", "").isalpha():
        print("Name must be Alphabatic !")
        return
    
    if not dob:
        print("Date of Birth is required !")
        return
    
    if not age.isnumeric():
        print("Age must be numerical !")
        return
    
    age = int(age)
    if age<3 or age>40:
        print("Enter valid Age !")
        return
    
    try:
        # Check Duplicate
        cursor.execute(
            "Select * from students where roll_no = %s",
            (roll_no,)
        )
        if cursor.fetchone():
            print("Roll number already exists!")
            return
        
        # Insert If not Duplicate
        sql="""
        Insert into students (roll_no, name, dob, st_class, age)
        Values (%s, %s, %s, %s, %s)
        """
        values = (roll_no, name, dob, st_class, age)
    
        cursor.execute(sql,values)
        conn.commit()

        print("Student Details Added Successfully")

    except Exception as err:
        print("Error", err)


def view_student():
    try:
        cursor.execute("select * from students")
        rows = cursor.fetchall()

        if len(rows)==0:
            print("No Record Found.")
        else:
            print("\n Students Records:")
            for row in rows:
               print("roll No:", row[0])
               print("name:", row[1])
               print("dob:", row[2])
               print("Class:", row[3])
               print("age:", row[4])
               print("----------------------------------------------")

    except Exception as err:
        print("Error", err)        



def search_student():
    roll_no=input("Enter Roll_No.:")

    try:
        cursor.execute(
            "select * from students where roll_no = %s ",
            (roll_no,)
        )

        row = cursor.fetchone()

        if row:
            print("\nStudent Found:")
            print("Roll No:", row[0])
            print("Name:", row[1])
            print("DOB:", row[2])
            print("Class:", row[3])
            print("Age:", row[4])
        else :
            print("Student Not Found")

    except Exception as err:
        print("Error", err)
                

def update_student():
    roll_no = input("Enter Roll_No to update: ")
    name = input("Enter New Name :")
    
    try:
        cursor.execute(
            "Update students SET name = %s where roll_no = %s",
            (name, roll_no)
        )
            
        conn.commit()
        
        if cursor.rowcount > 0:
            print("Student Updated Successfully.")
        else:
            print("Student not found.")

    except Exception as err:
        print("Error", err)



def delete_student():
    roll_no = input("Enter Roll_No to delete: ")
    
    try:
        cursor.execute(
            "Delete from students where roll_no = %s",
            (roll_no,)
        )
        conn.commit()

        if cursor.rowcount > 0:
            print("Student Deleted Successfully.")
        else:
            print("Student not found.")
    except Exception as err:
        print("Error", err)


while True:
    print("1. Add Student")
    print("2. View Student")
    print("3. Search ")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")
    
    choose=input("Enter choice")
    if choose=='1' :
        add_student()
    elif choose=='2':
        view_student()
    elif choose=='3':
        search_student()
    elif choose=='4':
        update_student()
    elif choose=='5':
        delete_student()
    elif choose=='6':
        break

    else:
        print("Choose correct option!!!")

