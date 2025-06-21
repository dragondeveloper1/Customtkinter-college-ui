import psycopg2
from psycopg2 import sql
import logging
########################################################################################
#   Notes:this py file has only table create and data add                              #
#         Please check db_logics for all logic                                         #
# #####################################################################################

 
# Function to create a connection to the database
def create_connection():
    try:
        conn = psycopg2.connect(
            dbname="db_name_you_choose",       # Replace with your DB name
            user="postgres",         # Replace with your DB user
            password="postgres_db_password", # Replace with your DB password
            host="localhost",            # Database host (localhost or IP)
            port="5432"              # Default PostgreSQL port
        )
        return conn
    except Exception as e:
        print(f"Error: Unable to connect to the database - {e}")
        return None
  
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_all_tables():
    conn = create_connection()
    if conn is None:
        logger.error("Database connection failed.")
        return False

    try:
        cursor = conn.cursor()
        table_definitions = [
    # Department
    ("""
        CREATE TABLE IF NOT EXISTS department (
            department_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            head_id INT,
            office_location VARCHAR(100),
            budget DECIMAL(15, 2),
            contact_info VARCHAR(100)
        );
    """, "department"),

    # Professor
    ("""
        CREATE TABLE IF NOT EXISTS professor (
            professor_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            department_id INT,
            email VARCHAR(100) UNIQUE,
            phone_number VARCHAR(20),
            office_location VARCHAR(100),
            hire_date DATE,
            salary DECIMAL(10, 2),
            degree VARCHAR(50),
            position VARCHAR(50),
            research_interests TEXT,
            FOREIGN KEY (department_id) REFERENCES department(department_id)
                ON DELETE SET NULL
        );
    """, "professor"),

    # Department Head Foreign Key
    ("""
        ALTER TABLE department
        ADD CONSTRAINT fk_head
        FOREIGN KEY (head_id) REFERENCES professor(professor_id)
        ON DELETE SET NULL;
    """, "department head reference"),

    # Course
    ("""
        CREATE TABLE IF NOT EXISTS course (
            course_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            code VARCHAR(50) UNIQUE,
            description TEXT,
            department_id INT,
            credit_hours INT,
            semester_offered VARCHAR(20),
            schedule VARCHAR(50),
            instructor_id INT,
            FOREIGN KEY (department_id) REFERENCES department(department_id) ON DELETE SET NULL,
            FOREIGN KEY (instructor_id) REFERENCES professor(professor_id) ON DELETE SET NULL
        );
    """, "course"),

    # Course Prerequisites
    ("""
        CREATE TABLE IF NOT EXISTS course_prerequisite (
            course_id INT REFERENCES course(course_id) ON DELETE CASCADE,
            prerequisite_course_id INT REFERENCES course(course_id) ON DELETE CASCADE,
            PRIMARY KEY (course_id, prerequisite_course_id)
        );
    """, "course_prerequisite"),

    # Program
    ("""
        CREATE TABLE IF NOT EXISTS program (
            program_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            department_id INT REFERENCES department(department_id) ON DELETE SET NULL,
            status VARCHAR(50)
        );
    """, "program"),

    # Program-Course
    ("""
        CREATE TABLE IF NOT EXISTS program_course (
            program_id INT REFERENCES program(program_id) ON DELETE CASCADE,
            course_id INT REFERENCES course(course_id) ON DELETE CASCADE,
            PRIMARY KEY (program_id, course_id)
        );
    """, "program_course"),

    # Student
    ("""
        CREATE TABLE IF NOT EXISTS student (
            student_id SERIAL PRIMARY KEY,
            registration_no VARCHAR(18) UNIQUE NOT NULL,
            name VARCHAR(100) NOT NULL,
            date_of_birth DATE,
            gender VARCHAR(10),
            address VARCHAR(255),
            email VARCHAR(100),
            phone_number VARCHAR(20),
            enrollment_date DATE,
            program_id INT REFERENCES program(program_id) ON DELETE SET NULL,
            gpa DECIMAL(3, 2),
            year_of_study INT,
            status VARCHAR(50),
            password_hash TEXT
        );
    """, "student"),

    # Classroom
    ("""
        CREATE TABLE IF NOT EXISTS classroom (
            classroom_id SERIAL PRIMARY KEY,
            room_number VARCHAR(50),
            building_name VARCHAR(100),
            seating_capacity INT,
            equipment TEXT
        );
    """, "classroom"),

    # Course-Classroom
    ("""
        CREATE TABLE IF NOT EXISTS course_classroom (
            course_id INT REFERENCES course(course_id) ON DELETE CASCADE,
            classroom_id INT REFERENCES classroom(classroom_id) ON DELETE CASCADE,
            PRIMARY KEY (course_id, classroom_id)
        );
    """, "course_classroom"),

    # Administrator
    ("""
        CREATE TABLE IF NOT EXISTS administrator (
            admin_id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            position VARCHAR(50),
            email VARCHAR(100),
            phone_number VARCHAR(20),
            office_location VARCHAR(100),
            salary DECIMAL(10, 2)
        );
    """, "administrator"),

    # Exam
    ("""
        CREATE TABLE IF NOT EXISTS exam (
            exam_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            course_id INT,
            exam_date DATE,
            duration INTERVAL,
            location VARCHAR(100),
            max_marks INT,
            instructor_id INT,
            FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE,
            FOREIGN KEY (instructor_id) REFERENCES professor(professor_id) ON DELETE SET NULL
        );
    """, "exam"),

    # Library
    ("""
        CREATE TABLE IF NOT EXISTS library (
            library_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            location VARCHAR(100),
            number_of_books INT,
            collection_type VARCHAR(50)
        );
    """, "library"),

    # Author
    ("""
        CREATE TABLE IF NOT EXISTS author (
            author_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            qualification VARCHAR(50),
            designation VARCHAR(100)
        );
    """, "author"),

    # Publication
    ("""
        CREATE TABLE IF NOT EXISTS publication (
            publication_id SERIAL PRIMARY KEY,
            registration_code VARCHAR(10),
            name VARCHAR(200),
            address VARCHAR(100),
            email VARCHAR(100),
            contact VARCHAR(50)
        );
    """, "publication"),

    # Book
    ("""
        CREATE TABLE IF NOT EXISTS book (
            book_id SERIAL PRIMARY KEY,
            title VARCHAR(100),
            author_id INT REFERENCES author(author_id) ON DELETE SET NULL,
            publication_id INT REFERENCES publication(publication_id) ON DELETE SET NULL,
            edition VARCHAR(20),
            isbn VARCHAR(13) UNIQUE,
            price DECIMAL(10, 2),
            pages INT,
            registration_date DATE
        );
    """, "book"),

    # Event
    ("""
        CREATE TABLE IF NOT EXISTS event (
            event_id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            event_date DATE,
            type VARCHAR(50),
            location VARCHAR(100),
            organizing_department_id INT REFERENCES department(department_id) ON DELETE SET NULL
        );
    """, "event"),

    # Event Participation
    ("""
        CREATE TABLE IF NOT EXISTS event_participation (
            event_id INT REFERENCES event(event_id) ON DELETE CASCADE,
            student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
            participation_date DATE,
            PRIMARY KEY (event_id, student_id)
        );
    """, "event_participation"),

    # Student Borrow-Return
    ("""
        CREATE TABLE IF NOT EXISTS student_borrow_return (
            student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
            book_id INT REFERENCES book(book_id) ON DELETE CASCADE,
            borrow_date DATE,
            return_date DATE,
            PRIMARY KEY (student_id, book_id, borrow_date)
        );
    """, "student_borrow_return"),

    # Student Complaint
    ("""
        CREATE TABLE IF NOT EXISTS student_complaint (
            complaint_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
            program_id INT REFERENCES program(program_id) ON DELETE SET NULL,
            department_id INT REFERENCES department(department_id) ON DELETE SET NULL,
            complaint_date DATE,
            details TEXT,
            is_resolved BOOLEAN DEFAULT FALSE
        );
    """, "student_complaint"),

    # Student Feedback
    ("""
        CREATE TABLE IF NOT EXISTS student_feedback (
            feedback_id SERIAL PRIMARY KEY,
            student_id INT REFERENCES student(student_id) ON DELETE CASCADE,
            course_id INT REFERENCES course(course_id) ON DELETE CASCADE,
            feedback_date DATE,
            feedback_text TEXT
        );
    """, "student_feedback"),
]

        for query, name in table_definitions:
            try:
                cursor.execute(query)
                conn.commit()
                logger.info(f"✅ Table '{name}' created or already exists.")
            except Exception as e:
                conn.rollback()
                logger.error(f"❌ Failed to create '{name}': {e}")

    except Exception as e:
        logger.critical(f"Error initializing schema: {e}")
    finally:
        cursor.close()
        conn.close()

create_connection()
create_all_tables()