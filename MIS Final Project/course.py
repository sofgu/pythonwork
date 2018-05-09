class Course:
    def __init__(self, seats_taken):
        self.__unique=0
        self.__title=''
        self.__prof=''
        self.__seats_taken=int(seats_taken)
        self.__capacity=0
    def get_unique(self):
        return self.__unique
    def set_unique(self,new_unique):
        self.__unique=new_unique
    def get_title(self):
        return self.__title
    def set_title(self, new_title):
        self.__title=new_title
    def get_prof(self):
        return self.__prof
    def set_prof(self, new_prof):
        self.__prof=new_prof
    def get_seats_taken(self):
        return self.__seats_taken
    def get_capacity(self):
        return self.__capacity
    def set_capacity(self, new_capacity):
        self.__capacity=new_capacity
    def calc_seats_remaining(self):
        return int(self.get_capacity())-int(self.get_seats_taken())
    def space_available(self):
        return self.calc_seats_remaining()>0
    def enroll_student(self):
        self.__seats_taken+=1
    def drop_student(self):
        self.__seats_taken-=1
    def line_for_file(self):
        line=''
        line+=self.get_unique()+';'
        line+=self.get_title()+';'
        line+=self.get_prof()+';'
        line+=str(self.get_seats_taken())+';'
        line+=str(self.get_capacity())+'\n'
        return line
    def __str__(self):
        string = "Course Number: "
        string = string + str(self.get_unique()) + "\n"
        string = string + "Title: "
        string = string + str(self.get_title()) + "\n"
        string = string + "Professor: "
        string = string + str(self.get_prof()) + "\n"
        string = string + "Seats Remaining: " + str(self.calc_seats_remaining()) + "\n"
        return string
