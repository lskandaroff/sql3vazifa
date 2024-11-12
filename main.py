# import psycopg2
# from pprint import pprint
# from collections import namedtuple

# db = psycopg2.connect(
#     database="fn27",
#     user="postgres",
#     host="localhost",
#     password="1"
# )
#
# Product = namedtuple('Product', ['id', 'name', 'description', 'code', 'price', 'quantity', 'added', 'published'])
#
# cursor = db.cursor()
#
# cursor.execute("""select * from products""")
# products = cursor.fetchall()
#
# cursor.execute('''
# insert into products(product_name, description, code, price, quantity) values
# ('Toxir', 'dahshat', 'AB', 10000.25, 6),
# ('Jobir', 'dahshat', 'AB', 10000.25, 6);
# ''')
#
# name = 'Nokia'
# des = 'Zor'
#
# cursor.execute(f'''
# insert into products(product_name, description, code, price, quantity) values
# (%s, %s, 'AB', 10000.25, 6);
# ''', (name, des))
#
# for product in products:
#     print(product)
#
# db.commit()
# db.close()


# db = psycopg2.connect(
#     database="5-oy 2-dars",
#     user="postgres",
#     host="localhost",
#     password="1"
# )
#
# cursor = db.cursor()

# School = namedtuple('School', ['id', 'name', 'address', 'phone_number', 'davlat_maktabi'])
#
#
#
# cursor.execute('''drop table if exists School;''')
#
# cursor.execute(
#     '''
#     create table if not exists School(
#     s_id serial primary key,
#     s_name varchar(150),
#     address text,
#     phone_number bigint,
#     davlat_maktabi bool
#     );
#     '''
# )

# cursor.execute(
#     '''
#     INSERT INTO School(s_name, address, phone_number, davlat_maktabi) VALUES
#     ('8-maktab', 'quvasoy', 998941234567, TRUE),
#     ('7-maktab', 'quvasoy', 99894121465, FALSE);
#     '''
# )

# cursor.execute(
#     '''
#     select * from School
#     '''
# )

# cursor.execute('''
#     alter table School
#     rename to maktab;
# ''')

# cursor.execute(
#     '''
#     select * from maktab
#     '''
# )
#
# schools = cursor.fetchall()
#
# for i in schools:
#     school = School(*i)
#     print(school.id, school.name, school.address, school.phone_number, school.davlat_maktabi)

# Teacher = namedtuple('Teacher', ['id', 'first_name', 'last_name', 'email', 'phone_number', 'school_id'])
#
# cursor.execute('''drop table if exists Teacher''')
#
# cursor.execute('''
# create table if not exists Teacher(
#     t_id serial primary key,
#     first_name varchar(150),
#     last_name varchar(150),
#     email text,
#     phone_number bigint,
#     school_id integer references School(s_id)
# );
# ''')
#
# cursor.execute('''
# insert into Teacher(first_name, last_name, email, phone_number) values
# ('Anna', 'Smith', 'Anna123@gmail.com', 998956474545),
# ('Adele', 'Sui', 'Adele123@gmail.com', 998956477777)
# ''')
#

# cursor.execute('''
#     alter table Teacher
#     rename to oqituvchilar;
# ''')
#
# cursor.execute('''select * from oqituvchilar''')
# teachers = cursor.fetchall()
#
# for i in teachers:
#     teacher = Teacher(*i)
#     print(teacher.id, teacher.first_name, teacher.last_name, teacher.email, teacher.phone_number)

# Student = namedtuple('Student', ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'school_id'])
#
# cursor.execute('''drop table if exists Student''')
#
# cursor.execute('''
# create table if not exists Student(
#     student_id serial primary key,
#     first_name varchar(150),
#     last_name varchar(150),
#     date_of_birth date,
#     gender char(1),
#     school_id integer references School(s_id)
# );
# ''')

# cursor.execute('''
#     alter table Student
#     add column email text;
# ''')
#
# cursor.execute('''
# insert into Student(first_name, last_name, date_of_birth, gender) values
# ('John', 'Smith', to_date('01.02.2005', 'dd.mm.yyyy'), 'M'),
# ('Klar', 'Wither', to_date('04.11.2005', 'dd.mm.yyyy'), 'F')
# ''')
#
# cursor.execute('''select * from Student''')
# students = cursor.fetchall()
#
# for i in students:
#     student = Student(*i)
#     print(student.id, student.first_name, student.last_name, student.date_of_birth, student.gender)


# Class = namedtuple('Class', ['id', 'name', 'teacher_id', 'school_id'])
#
# cursor.execute('''drop table if exists Class''')
#
# cursor.execute('''
# create table if not exists Class(
#     class_id serial primary key,
#     name varchar(150),
#     teacher_id integer references Teacher(t_id),
#     school_id integer references School(s_id)
# );
# ''')

# cursor.execute('''
#     alter table Class
#     drop column school_id;
# ''')

#
# cursor.execute('''
# insert into Class(name) values
# ('Physics'),
# ('Math')
# ''')
#
# cursor.execute('''select * from Class''')
# classes = cursor.fetchall()
#
# for i in classes:
#     classs = Class(*i)
#     print(classs.id, classs.name)

# Subject = namedtuple('Subject', ['id', 'name', 'class_id', 'teacher_id'])
#
# cursor.execute('''drop table if exists Subject''')
#
# cursor.execute('''
# create table if not exists Subject(
#     subject_id serial primary key,
#     name varchar(150),
#     class_id integer references Class(class_id),
#     teacher_id integer references Teacher(t_id)
# );
# ''')
#
# cursor.execute('''
# insert into Subject(name) values
# ('English'),
# ('Biology')
# ''')
#
# cursor.execute('''select * from Subject''')
# subjects = cursor.fetchall()
#
# for i in subjects:
#     subject = Subject(*i)
#     print(subject.id, subject.name)

#
# Enrollment = namedtuple('Enrollment', ['id', 'student_id', 'class_id', 'enrollment_date'])
#
# cursor.execute('''drop table if exists Enrollment''')
#
# cursor.execute('''
# create table if not exists Enrollment(
#     enrollment_id serial primary key,
#     student_id integer references Student(student_id),
#     class_id integer references Class(class_id),
#     enrollment_date date default current_date
# );
# ''')
#
#
# cursor.execute('''select * from Enrollment''')
# enrollments = cursor.fetchall()
#
# for i in enrollments:
#     enrollment = Enrollment(*i)
#     print(enrollment.id, enrollment.student_id, enrollment.class_id)



# Grade = namedtuple('Grade', ['grade_id', 'student_id', 'subject_id', 'grade_value', 'date_given'])
#
# cursor.execute('''drop table if exists Enrollment''')
#
# cursor.execute('''
# create table if not exists Grade(
#     grade_id serial primary key,
#     student_id integer references Student(student_id),
#     subject_id integer references Subject(subject_id),
#     grade_value char(3),
#     date_given date default current_date
# );
# ''')
#
# cursor.execute('''
# insert into Grade(grade_value) values
# (5),
# (4)
# ;
# ''')
#
#
# cursor.execute('''select * from Grade''')
# grades = cursor.fetchall()
#
# for i in grades:
#     grade = Grade(*i)
#     print(grade.date_given, grade.student_id, grade.grade_value)

#
# Attendance = namedtuple('Attendance', ['attendance_id', 'student_id', 'class_id', 'date_given'])
#
# cursor.execute('''drop table if exists Attendance''')
#
# cursor.execute('''
# create table if not exists Attendance(
#     attendance_id serial primary key,
#     student_id integer references Student(student_id),
#     class_id integer references Class(class_id),
#     date_given date default current_date
# );
# ''')
#
#
#
# cursor.execute('''select * from Attendance''')
# attendances = cursor.fetchall()
#
#
# for i in attendances:
#     attendance = Attendance(*i)
#     print(attendance.date_given, attendance.student_id, attendance.attendance_id)

#
# db.commit()
# db.close()



