import sqlite3 as lite

class DatabaseManage(object):

    def __init__(self):
        global con
        try:
            con = lite.connect('courses.db')
            with con:
                cur = con.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to connect to DB!")
    
    def insert_course(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute("INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)", data)
                return True
        except Exception:
            return False

    def fetch_courses(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            return False

    def delete_course(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
                return True
        except Exception:
            return False

def main():
    print("*"*40)
    print("\t :: Course Management :: ")
    print("*"*40)

    db = DatabaseManage()

    print("\n :: User Manual :: ")

    print("\nPress 1. Insert a new course")
    print("Press 2. Show all courses")
    print("Press 3. Delete a course (NEED ID)")
    print("Press any other key to EXIT\n")
    print("*"*40)
       
    choiceInput(db)

    

def choiceInput(db):
    choice = input("\nPlease enter you choice: ")
    if choice == "1":
        name = input("\nEnter name of the course: ")
        description = input("\nEnter description of the course: ")
        price = input("\nEnter price of the course: ")
        private = input("\nIs the course private? (0/1): ")
        if db.insert_course([name, description, price, private]):
            print("\nCourse added successfully!")
        else:
            print("\nSomething went wrong!")
        choiceInput(db)

    elif choice == "2":
        print("\n\n :: List of Courses :: \n\n")
        for index, item in enumerate(db.fetch_courses()):
            print("S No. " + str(index +1))
            print("\nCourse Id: " + str(item[0]))
            print("Course Name: " + str(item[1]))
            print("Course Description: " + str(item[2]))
            print("Price: " + str(item[3]))
            private = 'Yes' if item[4] else 'No'
            print("Private: " + private)
            print("\n")
        choiceInput(db)

    elif choice == "3":
        record_id = input("\nEnter ID of the course: ")
        if db.delete_course(record_id):
            print("\nCourse deleted successfully!")
        else:
            print("\nSomething went wrong!")
        choiceInput(db)

    else:
        print("BAD CHOICE !! ")


if __name__ == '__main__':
    main()
