import mysql.connector 

db = mysql.connector.connect(host='localhost', user='root', password='Directioner@3')
cursor = db.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS hms_db')
cursor.execute('USE hms_db')

cursor.execute("""
CREATE TABLE IF NOT EXISTS doctors (
    doc_id INT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    specialization VARCHAR(60) NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS patients (
    pat_id INT PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    age INT CHECK(age >= 0),
    phone VARCHAR(15)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS appointments (
    appt_id INT PRIMARY KEY,
    pat_id INT NOT NULL,
    doc_id INT NOT NULL,
    appt_date DATE NOT NULL,
    appt_time TIME NOT NULL,
    status ENUM('SCHEDULED','COMPLETED','CANCELLED') DEFAULT 'SCHEDULED',
    FOREIGN KEY (pat_id) REFERENCES patients(pat_id),
    FOREIGN KEY (doc_id) REFERENCES doctors(doc_id),
    UNIQUE (doc_id, appt_date, appt_time)
);
""")

cursor.execute("""
INSERT IGNORE INTO doctors VALUES
(1, 'Sreeja', 'Gynaec'),
(2, 'Pradeep', 'ENT');
""")

cursor.execute("""
INSERT IGNORE INTO patients VALUES
(101, 'Kevin', 38, '111'),
(102, 'Nick', 29, '222'),
(103, 'Joe', 34, '333');
""")

cursor.execute("""
INSERT IGNORE INTO appointments VALUES
(1, 101, 2, '2025-10-30', '10:00:00', 'COMPLETED'),
(2, 102, 1, '2025-10-30', '10:30:00', 'SCHEDULED');
""")

while True:
    choice = int(input("1.Add Appointment\n2.View All Appointments\n3.Update Appointment\n4.Delete Appointment\n5.Search Appointments by Doctor and Date\n6.Exit\nEnter Your Choice: "))
    
    if choice == 1:
        id = int(input("Enter Appointment ID: "))
        pat_id = int(input("Enter Patient ID: "))
        doc_id = int(input("Enter Doctor ID: "))
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        while True:
            time = input("Enter Appointment Time (HH:MM:SS): ")
            cursor.execute("SELECT * FROM appointments WHERE appt_time=%s AND appt_date=%s", (time, date,))
            f = cursor.fetchall()
            if len(f) == 0:
                cursor.execute("INSERT INTO appointments (appt_id, pat_id, doc_id, appt_date, appt_time) VALUES (%s, %s, %s, %s, %s)", (id, pat_id, doc_id, date, time))
                print("Appointment Added Successfully.")
                db.commit()
                break
            else:
                print("Slot already booked for this doctor. Choose another time.")
    
    elif choice == 2:
        cursor.execute("""
        SELECT a.appt_id, a.appt_date, a.appt_time, p.name, d.name, a.status
        FROM appointments AS a
        JOIN patients AS p ON a.pat_id = p.pat_id
        JOIN doctors AS d ON a.doc_id = d.doc_id
        """)
        rows = cursor.fetchall()
        for i in rows:
            print("#", str(i[0]), "|", str(i[1]), str(i[2]), "|", "Patient:", str(i[3]), "|", "Doctor:", str(i[4]), "|", i[5])
    
    elif choice == 3:
        id = int(input("Enter Appointment ID to Update: "))
        status = input("Enter New Status (SCHEDULED/COMPLETED/CANCELLED): ")
        cursor.execute("UPDATE appointments SET status=%s WHERE appt_id=%s", (status, id))
        print("Appointment Updated Successfully.")
        db.commit()
    
    elif choice == 4:
        id = int(input("Enter Appointment ID to Delete: "))
        cursor.execute("DELETE FROM appointments WHERE appt_id=%s", (id,))
        print("Appointment Deleted Successfully.")
        db.commit()
    
    elif choice == 5:
        doc_id = int(input("Enter Doctor ID: "))
        date = input("Enter Appointment Date (YYYY-MM-DD): ")
        cursor.execute("SELECT * FROM appointments WHERE doc_id=%s AND appt_date=%s", (doc_id, date))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    
    elif choice == 6:
        break
    else:
        print("Invalid Choice. Please Try Again.")

db.commit()