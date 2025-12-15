# Author: Saksham Shrestha
# Description: Design an ER diagram based on the provided scenario for a clinic and develop an OOP project that meets the following requirements:
# List the full information of all patients who are classified as seniors in the clinic (age > 65 years).
# Display the total number of doctors who specialise in ophthalmology.

import sqlite3

#class to connect to hospital database
class Hospital_db:
    def __init__(self):
        self.conn = sqlite3.connect('hospital.db')
        self.cursor = self.conn.cursor()

    #close function to delete the tables and close the database
    def close(self):
        self.cursor.execute('''DELETE FROM Doctor''')
        self.cursor.execute('''DELETE FROM Patient''')
        self.cursor.execute('''DELETE FROM Appointment''')
        self.conn.commit()
        self.conn.close()

class Doctor:
    def __init__(self,db,name,email,specialization):
        db.cursor.execute('''CREATE TABLE IF NOT EXISTS Doctor(
                             Doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             email TEXT NOT NULL,
                             specialization TEXT NOT NULL
                             )
                          ''')
        db.cursor.execute("INSERT INTO Doctor(name,email,specialization) VALUES(?,?,?)",
                          (name,email,specialization))
        db.conn.commit()

    @staticmethod
    def display_count_specializations(db,specialization):
        db.cursor.execute('''SELECT count(*) FROM Doctor WHERE specialization = ?''',(specialization,))
        result = db.cursor.fetchone()[0]
        print("The number of doctor specialized in",specialization,"is",result)

class Patient:
    def __init__(self,db,name,age,email,gender,address):
        db.cursor.execute('''CREATE TABLE IF NOT EXISTS Patient(
                             Patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             name TEXT NOT NULL,
                             age INTEGER NOT NULL,
                             email TEXT NOT NULL,
                             gender TEXT NOT NULL,
                             address TEXT NOT NULL
                             )
                          ''')
        db.cursor.execute("INSERT INTO Patient(name,age,email,gender,address) VALUES(?,?,?,?,?)",
                          (name,age,email,gender,address))
        db.conn.commit()

    @staticmethod
    def display_info_seniors(db):
        db.cursor.execute('''SELECT * FROM Patient WHERE age >= 65''')
        rows = db.cursor.fetchall()
        print("The senior patients are:")
        for row in rows:
            print(row)

class Appointment:
    def __init__(self,db,Patient_id,Doctor_id,date,diagnosis):
        db.cursor.execute('''CREATE TABLE IF NOT EXISTS Appointment(
                             Appointment_num INTEGER PRIMARY KEY AUTOINCREMENT,
                             Doctor_id INTEGER,
                             Patient_id INTEGER,
                             date TEXT NOT NULL,
                             diagnosis TEXT NOT NULL,
                             FOREIGN KEY(Doctor_id) REFERENCES Doctor(Doctor_id),
                             FOREIGN KEY(Patient_id) REFERENCES Patient(Patient_id)
            )
                          ''')
        db.cursor.execute("INSERT INTO Appointment(Patient_id,Doctor_id,date,diagnosis) VALUES(?,?,?,?)",
                          (Patient_id,Doctor_id,date,diagnosis))
        db.conn.commit()

def main():
    hospital = Hospital_db()
    Doctor(hospital,"Dr. James Nolan","james@gmail.com","ENT")
    Doctor(hospital,"Dr. Ciara Murphy","ciara@gmail.com","ophthalmology")
    Doctor(hospital,"Dr. Hari Bista","hari@gmail.com","ophthalmology")
    Patient(hospital,"Suren Chaudhari",20,"suren@gmail.com","Male","Remuera")
    Patient(hospital,"Ashim Shakya",30,"ashim@gmail.com","Male","Penrose")
    Patient(hospital,"Mukesh Shah",65,"mukesh@gmail.com","Male","Wellington")
    Patient(hospital,"Rosey Bhandari",68,"rosey@gmail.com","Female","christchurch")
    Patient(hospital,"Durgesh Rai",70,"durgesh@gmail.com","Male","Greenville")
    Appointment(hospital,1,1,"2025-12-20","Fever")
    Patient.display_info_seniors(hospital)
    Doctor.display_count_specializations(hospital,"ophthalmology")
    hospital.close()
if __name__ == "__main__":
    main()
