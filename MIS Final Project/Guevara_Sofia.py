#create global constant for student.txt input file
student_input = "students-sample.txt"
#create global constant for course.txt input file
course_input = "courses-sample.txt"
#create global constant for students updated output file
student_output = "students-updated.txt"
#create global constant for courses updated output file
courses_input = "courses-updated.txt"

#import student class file to create objects
import student
#import course class file to create objects
import course
#import matplot lib and patches and numpy for bar graph in option 5
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
    
#define print_menu function
def print_menu():
    print()
    print("1. Add course")
    print("2. Drop course")
    print("3. Print student's schedule")
    print("4. Print course schedule")
    print("5. Plot a bar graph with unique numbers on the x-axis,"+
          "\n   capacity and actual enrollment on the Y-axis.")
    print("6. Done")
    print()
          
#Define getuseroption function
def getuseroption():
    
    useroption = input("Choose a menu option (1-6): ")
    try:
        useroption = int(useroption)
    except:
        print("Must be an integer.")
        getuseroption()
 
    while (useroption != 1 and useroption != 2 and useroption != 3
           and useroption != 4 and useroption != 5 and useroption != 6):
        print("You have entered an invalid choice.")
        getuseroption()
                           
    return useroption
                           
       
#define process_students function   
def process_students(infile):
    student_dictionary={}
    for line in infile:
        line=line.rstrip('\n')
        line=line.split(':')
        eid=line[0]
        fname=line[1]
        lname=line[2]
        classes=line[3:]
        student_object=student.Student(eid,fname,lname,classes)
        student_dictionary[eid]=student_object
    return student_dictionary
   
    
#define process_courses function
def process_courses(infile):
    course_dictionary={}
    for line in infile:
        line=line.rstrip('\n')
        line=line.split(';')
        unique_num=line[0]
        title=line[1]
        professor=line[2]
        seats_taken=line[3]
        capacity=line[4]
        course_object=course.Course(seats_taken)
        course_object.set_unique(unique_num)
        course_object.set_title(title)
        course_object.set_prof(professor)
        course_object.set_capacity(int(capacity))
        course_dictionary[unique_num]=course_object
    return course_dictionary
    
    
def get_eid(student_dict):
    student_eid = input("Please enter a student ID:")
    while student_eid not in student_dict:
        student_eid = input("Error. Please enter an existing student ID:")
    return student_eid

def get_unique_number(course_dict):
    unique_number = input("Please enter the unique number: ")
    while unique_number not in course_dict:
        unique_number = input("Error. Please enter an existing unique number: ")
    return unique_number
                           
def print_course_schedule(course_dict):
    for unique in course_dict:
        print(course_dict[unique])

def print_student(student_object,student_dict,course_dict):
    print()
    print(student_object)
    print('Courses:')
    for unique in student_object.get_classes():
        class_object=course_dict[unique]
        class_title=class_object.get_title()
        print(unique, class_title)

def write_to_file(dictionary,outfile):
    for key in dictionary:
        this_object=dictionary[key]
        line=this_object.line_for_file()
        outfile.write(line)

def print_bar_graph(course_dict):
    uniquelist = []
    capacitylist = []
    enrollmentlist = []
    
    for course_object in course_dict.values():
        unique = course_object.get_unique()
        capacity = course_object.get_capacity()
        enrollment = course_object.get_seats_taken()

        uniquelist.append(unique)
        capacitylist.append(capacity)
        enrollmentlist.append(enrollment)

        print (uniquelist)
        print (capacitylist)
        print (enrollmentlist)
        
    x = np.arange(len(enrollmentlist))
    bar_width = 0.15
    plt.bar(x,enrollmentlist, width = bar_width, color = 'green', zorder = 2)
    plt.bar(x + bar_width, capacitylist, width= bar_width, color = 'red', zorder = 2)

    plt.xticks(x+bar_width, uniquelist)
    plt.title('Enrollment and Capacity per Course Unique Number')
    plt.xlabel('Course Unique Number')
    plt.ylabel('Students')

    green_patch = mpatches.Patch(color = 'green', label = 'Enrollment')
    red_patch = mpatches.Patch(color = 'red', label = 'Capacity')
    plt.legend(handles = [green_patch, red_patch])

    plt.grid(axis = 'y')

    plt.show()
    
    
                           
def main():
    student_file = open(student_input, 'r')
    course_file = open(course_input, 'r')
    student_dict=process_students(student_file)
    course_dict=process_courses(course_file)
    print_menu()
    choice = getuseroption()
    while choice != 6:
        if choice == 6:
            updated_info()
        
        elif choice == 1:
            eid = get_eid(student_dict)
            student_object = student_dict[eid]
            unique = get_unique_number(course_dict)
            course_object = course_dict[unique]
            while course_object.space_available() == False:
                print('Error. Course is full. Please pick a new course.')
                unique = get_unique_number(course_dict)
                course_object = course_dict[unique]
            while student_object.add_class(unique) == False:
                unique = get_unique_number(course_dict)
                course_object=course_dict[unique]
                while course_object.space_available()==False:
                    print('Error. Course is full. Please pick a new course')
                    unique=get_unique_number(course_dict)
                    course_object=course_dict[unique]
            course_object.enroll_student()
            print('Student',eid,'enrolled in', unique)
            
        elif choice == 2:
            eid=get_eid(student_dict)
            student_object=student_dict[eid]
            unique=get_unique_number(course_dict)
            course_object=course_dict[unique]
            while student_object.drop_class(unique)==False:
                unique=get_unique_number(course_dict)
                course_object=course_dict[unique]
                
            course_object.drop_student()
            print('Student',eid,'dropped from', unique)
            
        elif choice == 3:
            eid = get_eid(student_dict)
            student_object=student_dict[eid]
            print_student(student_object,student_dict,course_dict)

        elif choice == 4:
            print_course_schedule(course_dict)

        elif choice == 5:
            print_bar_graph(course_dict)

        print()
        print_menu()
        choice = getuseroption()
        
    updated_student_file=open('students-updated.txt','w')
    updated_course_file=open('courses-updated.txt','w')

    write_to_file(student_dict,updated_student_file)
    write_to_file(course_dict,updated_course_file)
    
    
    updated_student_file.close()
    updated_course_file.close()
    student_file.close()
    course_file.close()



#call main
main()
            

    
    
