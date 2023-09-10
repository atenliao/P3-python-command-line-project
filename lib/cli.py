# import ipdb
from prettycli import red
from simple_term_menu import TerminalMenu
from models import Worker,Department, Role
from pyfiglet import figlet_format
import random
import time
import re
from Department import Department
from prompt import Prompt
from banner import Banner
from Session import session

prompt = Prompt()
class Cli():
    def __init__(self):
        self.current_worker = None

    def start(self):
        self.clear_screen(1)
        Banner.Displaystring("Wellcome Workers database")
        return self.welcome()

    def welcome(self):
        print("Are you a new Worker")
        selection = prompt.yesno(option=["Exit","Debug"])
        if selection == "Yes":
            print("please sign up")
            self.create_new_worker()
        elif selection == "Exit":
            self.exit()
        elif selection == "Debug":
            self.debug()
        else:
            self.handle_login()

    def clear_screen(self,lines):
        print("\n" * lines)

    def handle_login(self):
        print("the Login Format is Lastname + first 4 chars of firstname\n")
        login = input("Please enter login:\n\n")
        regex = r"[A-Za-z]"
        if re.match(regex,login):
            worker = Worker.find_or_create_by(login)
            if worker:
                print("found the worker by login")
                options=["Show worker Info", "Delete worker","Edit worker Info", "Exit"]
                selection = self.show_worker_options(options)
                print(selection)
                if selection == "Show worker Info":
                    print(self.current_worker)
                elif selection == "Delete worker":
                    self.delete_Login(login)
                elif selection == "Edit worker Info":
                    self.edit_worker_Info(worker)
                else:
                    self.exit()   
            else:
                print("Please Input again")
                self.handle_login()
        else:
            print(red("Invalid login"))
            time.sleep(2)
            self.start()
        
        pass

    def get_worker_info(self, question):
        return prompt.askQuestion(question)


    def create_new_worker(self):
        department = random.choice(session.query(Department).all())
        
        Lastname = self.get_worker_info("please enter your lastname")
        Firstname = self.get_worker_info("please enter your firstname")
        Gender = prompt.getGender()
        Shift = prompt.getShift()
        login =  self.create_Login(Lastname, Firstname)
        role = random.choice(session.query(Role).all())
        worker = Worker.create(
            lastname = Lastname,
            firstname = Firstname,
            gender = Gender,
            shift = Shift,
            login = Lastname + Firstname[0:4] ,
            Employee_ID =random.randint(10000,50000),
            department_id = department.id
            
            )
        worker.roles.append(role)
        session.add(worker)
        session.commit()
               
    
    def edit_worker_Info(self, worker):
        options=["Lastname", "Firstname","Gender", "Shift", "Exit"]
        selection = self.show_worker_options(options)
        if selection == "Lastname":
            lastname = input("please input your lastname: ")
            worker.lastname = lastname
            worker.login = self.create_Login(worker.lastname, worker.firstname)
            session.commit()
            print("Your Lastname has already updated successfully!")
        elif selection == "Firstname":
            firstname = input("please input your firstname: ")
            worker.firstname = firstname
            worker.login = self.create_Login(worker.lastname, worker.firstname)
            session.commit()
            print("Your Firstname has already updated successfully!")
        elif selection == "Gender":
            gender = prompt.getGender()
            worker.gender = gender
            session.commit()
            print("Your Gender has already updated successfully!")
        elif selection == "Shift":
            shift = prompt.getShift()
            print('shift is',shift)
            worker.shift = shift
            session.commit()
            print("Your Shift has already updated successfully!")
        elif selection == "Exit":
            self.exit()

    def show_worker_options(self,options=None):
        if isinstance(options,list):
            terminal_menu = TerminalMenu(options)
            menu_entry_index = terminal_menu.show()
            return(options[menu_entry_index])


    
    def delete_Login(self,login):
        worker = session.query(Worker).filter(Worker.login.like(login)).first()
        session.delete(worker)
        session.commit()

    def create_Login(self,lastname, firstname):
        if lastname:
            if len(firstname) >= 4:
                login = lastname + firstname[0:4]
            else:
                login = lastname + firstname
        return login

    def exit(self):
        print("Bye!")

    def debug(self):
        import ipdb; ipdb.set_trace()

app = Cli()
app.start()
