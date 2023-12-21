import random
import sys
sys.path.append(r'C:\Users\sange\BadmintonCourtAllotment')
import UserDetails

class Booking:
    def __init__(self):
        self.booked_details_arr = []
        user_file = open("BookedDetailsFile.txt")
        for details in user_file:
            self.booked_details_arr.append(details.split(","))
        user_file.close()
        
        self.session_det_arr = []
        session_details = open("AvailableDetails.txt")
        for session_det in session_details:
            self.session_det_arr.append(session_det.split(","))
        session_details.close()
        print(self.session_det_arr)

        self.user_arr = []
        user_file = open("UserDetailsFile.txt")
        for details in user_file:
            self.user_arr.append(details.split(","))
        user_file.close()
     

        

    def session_booking(self):
        authenticate = self.authenticate()
        if authenticate != None:
            if self.session_limit(authenticate[0]) == 1:
                availability_check = self.check_availability(authenticate[1])
                if availability_check != "NOT AVAILABLE":
                    print("Session available")

                    self.booked_details_arr.append([authenticate[0], authenticate[1], authenticate[3], availability_check, "\n"])
                    self.booked_details()
                    self.write_in_file()
                    self.avl_write_in_file()
                else:
                    print("NOT AVAILABLE")
            else:
                print("Already you have booked 2 sessions")

    def sign_up(self):
        name      = input("Name                  : ")
        gender    = input("Gender (Male/ Female) : ")
        dob       = input("DOB                   : ")
        number         = random.randint(10, 99)
        user_name = name + str(number)
        print("Your username is", user_name)
        self.user_arr.append([name, gender, dob, user_name, "\n"])
        self.write_in_file()

    def check_availability(self, gender):
        session = self.session()
        
        check = self.check_availability_for_girls(gender)
        if check == "YES":
            for details in self.session_det_arr:
                if details[0] == session:
                    if details[1] == "AVL":
                        details[1] = "BOOKED"
                        return session
                    else:
                        return "NOT AVAILABLE"
        elif check == "OVER":
            print("Girls Sessions over")        
        else:
            print("The sessions only available for girls")        


    def session_limit(self, name):
        count = 0 
        for details in self.booked_details_arr:
            if details[0] == name:
                count += 1
        if count < 2:
            return 1
    def session(self):
        print("Choose the session")
        print("\n")
        print(" 1. Session 1 \n 2. Session 2 \n 3. Session 3 \n 4. Session 4 \n 5. Session 5 \n 6. Session 6 \n")
        option = int(input("Select any of the options : "))
        if option == 1:
            return "Session 1"
        elif option == 2:
            return "Session 2"
        elif option == 3:
            return "Session 3"
        elif option == 4:
            return "Session 4"
        elif option == 5:
            return "Session 5"
        elif option == 6:
            return "Session 6"

    def authenticate(self):
        for chances in range(3):
            user_name = input("Enter your username : ")
            for details in self.user_arr:
                if details[3] == user_name:
                    return details
            print("You have", 3 - chances, "chances left")
            print("Enter correct username")



    def check_availability_for_girls(self, gender):
        female_avl_count = 2
        avl_session_count = 0
        for details in self.booked_details_arr:
           
            if details[1].lower() == "female" and female_avl_count >= 0:
                female_avl_count -= 1
                if female_avl_count == 0 and gender.lower() == "female":
                    return "OVER"
        for details in self.session_det_arr:
            if details[1] == "AVL":
                avl_session_count += 1

        if avl_session_count >= female_avl_count:
            return "YES"
        else:
            return "NO"        


    

    def print_details(self):
        pass

    def print_sessions(self):
        if self.authenticate() != None:
            i = 1
            start = 4
            for details in self.session_det_arr:
                print("Session " + str(i) + "  -\t" + str(start) + " to " + str(start + 1) + " \t " + details[1])
                i += 1
                start += 1
        
    
    def booked_details(self):
        booked_details_file = open("BookedDetailsFile.txt", "w")
        for details in self.booked_details_arr:
            booked_details_file.write(details[0] + "," + details[1] + "," + details[2] + "," + details[3]+ ",\n")

        booked_details_file.close()     

    def write_in_file(self):
        user_file = open("UserDetailsFile.txt", "w")
        for details in self.user_arr:
            user_file.write(details[0] + "," + details[1] + "," + details[2] + "," + details[3] + ",\n")
        user_file.close()

    def avl_write_in_file(self):
        session_details = open("AvailableDetails.txt", "w")
        for details in self.session_det_arr:
            session_details.write(details[0] + "," + details[1] + ",\n")
        session_details.close()

def options():
    obj = Booking()
    while True:
        print("\n")
        print(" 1. Sign up\n 2. View Sessions\n 3. Book Sessions\n 4. Exit\n")
        option = int(input("Select any of the options : "))
        print("\n")
        if option == 1:
            obj.sign_up()

        elif option == 2:    
            obj.print_sessions()

        elif option == 3:
            obj.session_booking()

        elif option == 4:
            break

              


options()