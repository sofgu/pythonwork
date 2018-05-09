class Student:
    def __init__(self, new_id, new_fname, new_lname, classes):
        self.__uteid=new_id
        self.__fname=new_fname
        self.__lname=new_lname
        self.__class_list=classes
    def get_uteid(self):
        return self.__uteid
    def get_fname(self):
        return self.__fname
    def get_lname(self):
        return self.__lname
    def get_classes(self):
        return self.__class_list
    def add_class(self,unique_num):
        if unique_num not in self.__class_list:
            self.__class_list.append(unique_num)
            return True
        else:
            print('Student already enrolled in',unique_num,'Please select a different course')
            return False
    def drop_class(self,unique_num):
        if unique_num in self.__class_list:
            self.__class_list.remove(unique_num)
            return True
        else:
            print('Student not enrolled in',unique_num, 'Please enter a new course')
            return False
    def line_for_file(self):
        line=''
        line+=self.get_uteid()+':'
        line+=self.get_fname()+':'
        line+=self.get_lname()+':'
        for item in self.__class_list:
            line+=item+':'
        line=line.rstrip(':')
        line+='\n'
        return line
            
    def __str__(self):
        string = "Student ID: " + str(self.get_uteid()) + "\n"
        string=string + "Student Name: " + str(self.get_fname()) + " " + str(self.get_lname())
        return string
