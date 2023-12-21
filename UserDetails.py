

        

        



'''import random 
class UserDetails:
    def __init__(self):
        self.name      = input("Name   : ")
        self.gender    = input("Gender : ")
        self.dob       = input("DOB    : ")
        number         = random.randint(10, 99)
        self.user_name = self.name + str(number)
        
    def write_in_file(self):
        user_arr = []
        user_file = open("UserDetailsFile.txt")
        for details in user_arr:
            user_file.write(user_arr[0] + "," + user_arr[1] + "," + user_arr[2] + "," + user_arr[3] + ",\n")
        pass

    '''    