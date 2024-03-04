# -*- coding: utf-8 -*-
"""
Created on Mon Mar 4 19:44:49 2024

@author: varung
"""
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Student:
   def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("STUDENT REGISTRATION SYSTEM")

        # variables
        self.var_enrollment = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_department = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_section = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()

        # 1st image
        img = Image.open('mits.jpg')
        img = img.resize((1550, 170), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        self.label_image = Label(self.root, image=self.photoimg)
        self.label_image.place(x=0, y=0, width=1550, height=170)

        # background image
        img_4 = Image.open('university.png')
        img_4 = img_4.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)

        bg_label = Label(self.root, image=self.photoimg_4, bd=2, relief=RIDGE)
        bg_label.place(x=0, y=160, width=1530, height=650)

        label_title = Label(bg_label, text="STUDENT REGISTRATION SYSTEM", font=("Comic Sans MS", 37, "bold"), fg="blue", bg="white")
        label_title.place(x=0, y=0, width=1530, height=50)

        # manage frames
        manage_frame = Frame(bg_label, bd=2, relief=RIDGE, bg="white")
        manage_frame.place(x=15, y=55, width=1500, height=560)

        # left data frame
        left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=("Comic Sans MS", 12, "bold"), fg="red", bg="white")
        left_frame.place(x=10, y=10, width=660, height=540)

        img_5 = Image.open(r'C:\Users\Hi\.spyder-py3\3.jpg')
        img_5 = img_5.resize((650, 120), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)

        my_label = Label(left_frame, image=self.photoimg_5, bd=2, relief=RIDGE)
        my_label.place(x=0, y=0, width=650, height=120)

        # current course
        student_info_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Current Course Information", font=("Comic Sans MS", 12, "bold"), fg="red", bg="white")
        student_info_frame.place(x=0, y=120, width=667, height=115)

        course_label = Label(student_info_frame, text="Course", font=("Comic Sans MS", 12, "bold"), bg="white")
        course_label.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        course_combo = ttk.Combobox(student_info_frame, textvariable=self.var_course, font=("Arial", 12, "bold"), width=17, state="readonly")
        course_combo["value"] = ("Select Courses", "B.E/B.Tech", "Ph.D", "MBA", "MCA", "M.E", "M.Tech")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # department drop box
        department_label = Label(student_info_frame, text="Department", font=("Comic Sans MS", 12, "bold"), bg="white")
        department_label.grid(row=0, column=2, padx=2, sticky=W)

        department_combo = ttk.Combobox(student_info_frame, textvariable=self.var_department, font=("Arial", 12, "bold"), width=17, state="readonly")
        department_combo["value"] = ("Select Department", "Computer Science And Engineering", "Computer Science And Design", "Information Technology", "Artificial Intelligence And Machine Learning", "Artificial Intelligence And Data Science", "Artificial Intelligence And Robotics", "Electrical Engineering", "Internet Of Things Offered By Electrical Engineering", "Internet Of Things Offered By Information Technology", "Mathematics And Computing", "Autombile Engineering", "Electronics And TeleCommunication", "Chemical Engineering", "Architecture", "Electronics Engineering", "Civil Engineering Department", "Mechanical Engineering")
        department_combo.current(0)
        department_combo.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # year
        current_year = Label(student_info_frame, text="Year:", font=("Comic Sans MS", 12, "bold"), bg="white")
        current_year.grid(row=1, column=0, padx=2, sticky=W)

        current_year_combo = ttk.Combobox(student_info_frame, textvariable=self.var_year, font=("Arial", 12, "bold"), width=17, state="readonly")
        current_year_combo["value"] = ("Select Your Current Year", "1st Year", "2nd Year", "3rd Year", "4th Year")
        current_year_combo.current(0)
        current_year_combo.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # current semester
        current_semester = Label(student_info_frame, text="Semester:", font=("Comic Sans MS", 12, "bold"), bg="white")
        current_semester.grid(row=1, column=2, padx=2, pady=10, sticky=W)

        current_semester_combo = ttk.Combobox(student_info_frame, textvariable=self.var_semester, font=("Arial", 12, "bold"), width=17, state="readonly")
        current_semester_combo["value"] = ("Select Your Current Semester", "1st Semester", "2nd Semester", "3rd Semester", "4th Semester", "5th Semester", "6th Semester", "7th Semester", "8th Semester")
        current_semester_combo.current(0)
        current_semester_combo.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # student class information
        student_class = LabelFrame(left_frame, bd=4, relief=RIDGE, padx=2, text="Student Class Information", font=("Comic Sans MS", 12, "bold"), fg="red", bg="white")
        student_class.place(x=0, y=195, width=650, height=235)

        # student name
        student_name = Label(student_class, text="Student Name: ", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_name.grid(row=0, column=0, padx=2, pady=7, sticky=W)

        name_entry = ttk.Entry(student_class, textvariable=self.var_name, font=("Comic Sans MS", 12, "bold"), width=15)
        name_entry.grid(row=0, column=1, sticky=W, padx=2, pady=7)

        # student id
        student_id = Label(student_class, text="Enrollment", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_id.grid(row=0, column=2, padx=2, pady=7, sticky=W)

        id_entry = ttk.Entry(student_class, textvariable=self.var_enrollment, font=("Comic Sans MS", 12, "bold"), width=15)
        id_entry.grid(row=0, column=3, sticky=W, padx=2, pady=7)

        # sections
        class_section = Label(student_class, text="Section: ", font=("Comic Sans MS", 12, "bold"), bg="white")
        class_section.grid(row=1, column=0, padx=2, pady=7, sticky=W)

        section_entry = ttk.Combobox(student_class, textvariable=self.var_section, state="readonly", font=("Arial", 10, "bold"), width=18)
        section_entry["values"] = ("Select Your Branch Section", "A", "B", "C")
        section_entry.current(0)
        section_entry.grid(row=1, column=1, sticky=W, padx=2, pady=7)

        # gender
        student_gender = Label(student_class, text="Gender:", font=("Comic Sans MS", 10, "bold"), bg="white")
        student_gender.grid(row=1, column=2, padx=2, pady=7, sticky=W)

        gender_combo = ttk.Combobox(student_class, textvariable=self.var_gender, state="readonly", font=("Arial", 10, "bold"), width=19)
        gender_combo["values"] = ("Select Your Gender", "Male", "Female")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, sticky=W, padx=2, pady=7)

        # dob
        student_dob = Label(student_class, text="DOB:", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_dob.grid(row=2, column=0, padx=2, pady=7, sticky=W)

        dob_entry = ttk.Entry(student_class, textvariable=self.var_dob, font=("Arial", 12, "bold"), width=15)
        dob_entry.grid(row=2, column=1, sticky=W, padx=2, pady=7)

        # mobile number
        student_mobile = Label(student_class, text="Phone", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_mobile.grid(row=2, column=2, padx=2, pady=7, sticky=W)

        num_entry = ttk.Entry(student_class, textvariable=self.var_phone, font=("Arial", 12, "bold"), width=16)
        num_entry.grid(row=2, column=3, sticky=W, padx=2, pady=7)

        # mail
        student_email = Label(student_class, text="Email I'D:", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_email.grid(row=3, column=0, padx=2, pady=7, sticky=W)

        email_entry = ttk.Entry(student_class, textvariable=self.var_email, font=("calibri", 12, "bold"), width=15)
        email_entry.grid(row=3, column=1, sticky=W, padx=2, pady=7)

        # address
        student_address = Label(student_class, text="Address:", font=("Comic Sans MS", 12, "bold"), bg="white")
        student_address.grid(row=3, column=2, padx=2, pady=7, sticky=W)

        address_entry = ttk.Entry(student_class, textvariable=self.var_address, font=("Comic Sans MS", 12, "bold"), width=15)
        address_entry.grid(row=3, column=3, sticky=W, padx=2, pady=7)

        # button
        self.button1 = Button(self.root, text="New", command=self.add_data, cursor="hand2")
        self.button1.place(x=250, y=525, width=90, height=40)

        # save button
        save_button = Button(button_frame, text="Save", command=self.add_students, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        save_button.grid(row=0, column=0)

        # update button
        update_button = Button(button_frame, text="Update", command=self.update_data, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        update_button.grid(row=0, column=1)

        # delete button
        delete_button = Button(button_frame, text="Delete", command=self.delete_data, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        delete_button.grid(row=0, column=2)

        # reset button
        reset_button = Button(button_frame, text="Reset", command=self.reset_data, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        reset_button.grid(row=0, column=3)

        # right frame
        right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE, padx=2, text="Student Information", font=("Comic Sans MS", 12, "bold"), fg="red", bg="white")
        right_frame.place(x=670, y=10, width=820, height=540)

        # img_6 = Image.open("college_images/student.jpg")
        # img_6 = img_6.resize((820, 540), Image.ANTIALIAS)
        # self.photoimg_6 = ImageTk.PhotoImage(img_6)

        # my_label = Label(right_frame, image=self.photoimg_6, bd=2, relief=RIDGE)
        # my_label.place(x=0, y=0, width=810, height=120)

        # search frame
        search_frame = LabelFrame(right_frame, bd=4, relief=RIDGE, text="Search System", font=("Comic Sans MS", 12, "bold"), fg="red", bg="white")
        search_frame.place(x=5, y=70, width=810, height=70)

        # search by
        search_by = Label(search_frame, text="Search By:", font=("Comic Sans MS", 12, "bold"), bg="white")
        search_by.grid(row=0, column=0, padx=2, pady=10, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("Arial", 12, "bold"), state="readonly", width=17)
        search_combo["value"] = ("Select", "Enrollment", "Name", "Mobile")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # search entry
        search_entry = ttk.Entry(search_frame, font=("Arial", 12, "bold"), width=15)
        search_entry.grid(row=0, column=2, padx=2, pady=10, sticky=W)

        # search button
        search_button = Button(search_frame, text="Search", command=self.search_data, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        search_button.grid(row=0, column=3, padx=2, pady=10)

        # show all button
        showall_button = Button(search_frame, text="Show All", command=self.fetch_data, font=("Comic Sans MS", 12, "bold"), bg="blue", fg="white", width=15)
        showall_button.grid(row=0, column=4, padx=2, pady=10)

        # table frame
        table_frame = Frame(right_frame, bd=4, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=145, width=810, height=350)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column=(
            "enrollment", "name", "course", "department", "year", "semester", "section", "gender", "dob", "phone", "email", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("enrollment", text="Enrollment")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("department", text="Department")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("section", text="Section")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("address", text="Address")

        self.student_table["show"] = 'headings'

        self.student_table.column("enrollment", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("department", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("semester", width=100)
        self.student_table.column("section", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("address", width=150)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # function to add students
   def add_students(self):
        if self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_course.get() == "Select Courses" or self.var_department.get() == "Select Department" or self.var_year.get() == "Select Your Current Year" or self.var_semester.get() == "Select Your Current Semester" or self.var_section.get() == "" or self.var_gender.get() == "Select Your Gender" or self.var_dob.get() == "" or self.var_phone.get() == "" or self.var_email.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="your_password", database="your_database_name")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                                  (self.var_enrollment.get(),
                                   self.var_name.get(),
                                   self.var_course.get(),
                                   self.var_department.get(),
                                   self.var_year.get(),
                                   self.var_semester.get(),
                                   self.var_section.get(),
                                   self.var_gender.get(),
                                   self.var_dob.get(),
                                   self.var_phone.get(),
                                   self.var_email.get(),
                                   self.var_address.get()
                                   ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # function to fetch data
   def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="your_password", database="your_database_name")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.student_table.delete(
                *self.student_table.get_children())
            for i in rows:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # function to get cursor
   def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        rows = content['values']

        self.var_enrollment.set(rows[0])
        self.var_name.set(rows[1])
        self.var_course.set(rows[2])
        self.var_department.set(rows[3])
        self.var_year.set(rows[4])
        self.var_semester.set(rows[5])
        self.var_section.set(rows[6])
        self.var_gender.set(rows[7])
        self.var_dob.set(rows[8])
        self.var_phone.set(rows[9])
        self.var_email.set(rows[10])
        self.var_address.set(rows[11])

    # function to update data
   def update_data(self):
        if self.var_enrollment.get() == "" or self.var_name.get() == "" or self.var_course.get() == "Select Courses" or self.var_department.get() == "Select Department" or self.var_year.get() == "Select Your Current Year" or self.var_semester.get() == "Select Your Current Semester" or self.var_section.get() == "" or self.var_gender.get() == "Select Your Gender" or self.var_dob.get() == "" or self.var_phone.get() == "" or self.var_email.get() == "" or self.var_address.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno(
                    "Update", "Do you want to update this student details?", parent=self.root)
                if update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="your_password", database="your_database_name")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s,Course=%s,Department=%s,Year=%s,Semester=%s,Section=%s,Gender=%s,DOB=%s,Phone=%s,Email=%s,Address=%s where Enrollment=%s", (
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_department.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_section.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_phone.get(),
                        self.var_email.get(),
                        self.var_address.get(),
                        self.var_enrollment.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo(
                    "Success", "Student details have been updated successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # function to delete data
   def delete_data(self):
        if self.var_enrollment.get() == "":
            messagebox.showerror(
                "Error", "Enrollment must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Student Delete Page", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="your_password", database="your_database_name")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "delete from student where Enrollment=%s", (self.var_enrollment.get(),))
                else:
                    if not delete:
                        return
                messagebox.showinfo(
                    "Success", "Student details have been deleted successfully", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

    # function to reset data
   def reset_data(self):
        self.var_enrollment.set("")
        self.var_name.set("")
        self.var_course.set("Select Courses")
        self.var_department.set("Select Department")
        self.var_year.set("Select Your Current Year")
        self.var_semester.set("Select Your Current Semester")
        self.var_section.set("")
        self.var_gender.set("Select Your Gender")
        self.var_dob.set("")
        self.var_phone.set("")
        self.var_email.set("")
        self.var_address.set("")

    # function to search data
   def search_data(self):
        if self.var_combobox.get() == "" or self.var_search_entery.get() == "":
            messagebox.showerror(
                "Error", "Please select option from search combobox", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="your_password", database="your_database_name")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select * from student where " + str(self.var_combobox.get()) + " LIKE '%" + str(self.var_search_entery.get()) + "%'")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.student_table.delete(
                        *self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Due to:{str(es)}", parent=self.root)

# root object
root = Tk()
obj = Student(root)
root.mainloop()
