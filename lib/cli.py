
from prettycli import red,green,yellow,blue,color
from simple_term_menu import TerminalMenu
from models import Worker, Role, Workerrole
from pyfiglet import figlet_format
import signal
import random
import time
import re
from Department import Department
from prompt import Prompt
from banner import Banner
from Session import session

prompt = Prompt()
class Cli():
    def start(self):
        self.clear_screen(1)
        Banner.Displaystring("Wellcome Workers database")
        return self.welcome()

    def welcome(self):
        print("Are you a new Worker")
        selection = prompt.yesno(option=["Exit","Debug"])
        if selection == "Yes":
            getlogin = self.create_new_worker()
            if getlogin:
                print(getlogin)
                print("The new worker create successful!!!\n")
                self.handle_login(getlogin)
        elif selection == "Exit":
            self.exit()
        elif selection == "Debug":
            self.debug()
        else:
            Lastname = "Lastname"
            Firstname = "Firstname"
            print(f"the Login Format is {yellow(Lastname)} + first 4 chars of {yellow(Firstname)}\n")
            login = input("Please enter login:\n\n")
            self.handle_login(login)

    def Main_menu(self):
        options= ["Main Menu", "Exit"]
        selection = self.show_options(options)
        if selection == "Main Menu":
            self.welcome()
        elif selection == "Exit":
            self.exit()

    def clear_screen(self,lines):
        print("\n" * lines)

    def worker_Menu(self,worker):
        options=["Show worker Info","Show worker Department","Show worker roles","Edit worker Info", "Delete worker", "Exit"]
        selection = self.show_options(options,"Worker Options Menu")
        if selection == "Show worker Info":
            print("\n\n===========================")
            print(f"Lastname: {blue(worker.lastname)}\n" \
                + f"Firstname: {blue(worker.firstname)}\n" \
                + f"Gender: {blue(worker.gender)}\n" \
                + f"Shift: {green(worker.shift)}\n" \
                + f"Login: {yellow(worker.login)}\n" \
                + f"Employee ID: {red(str(worker.Employee_ID))}")
            print("===========================\n\n")
            self.handle_login(worker.login)
        elif selection == "Show worker Department":
            self.show_department(worker.department_id)
            self.handle_login(worker.login)
        elif selection == "Show worker roles":
            self.show_worker_roles(worker.id)
            self.handle_login(worker.login)
        elif selection == "Edit worker Info":
            self.edit_worker_Info(worker)
            print(worker)
            self.worker_Menu(worker)
        elif selection == "Delete worker":
            print(f"worker login {worker.login} is deleted")
            self.delete_Login(worker.login)
            self.Main_menu()
        else:
            self.exit()
        
    def handle_login(self,login):
        regex = r"[A-Za-z]"
        if re.match(regex,login):
            worker = Worker.find_or_create_by(login)
            if worker:
                self.worker_Menu(worker) 
            else:
                print("The worker is not in the database \n")
                print("The Login Format is Lastname + first 4 chars of firstname\n")
                login = input("Please enter login:\n\n")
                self.handle_login(login)
        else:
            print(red("Invalid login"))
            time.sleep(2)
            self.start()
        pass

    def show_department(self, ID):
        department = session.query(Department).filter(Department.id == ID).first()
        print(f"The Worker department is {blue(department.name)} locate in {yellow(department.city)}\n\n")

    def get_worker_info(self, question):
        return prompt.askQuestion(question)

    def show_worker_roles(self,id):
        workerrole = session.query(Workerrole).filter(Workerrole.workers_id==id).all()
        print("worker is assigned roles in")
        for worker in workerrole:
            workerroles = session.query(Role).filter(Role.id == worker.roles_id).first()
            print(f"{blue(workerroles.name)} with level {green(str(workerroles.level))}")

        print("\n")

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
        
        return login
               
    def edit_worker_Info(self, worker):
        options=["Lastname", "Firstname","Gender", "Shift", "Exit"]
        selection = self.show_options(options,"Edit Worker Info")
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
            print('Shift is',shift)
            worker.shift = shift
            session.commit()
            print("Your Shift has already updated successfully!")
        elif selection == "Exit":
            self.exit()

    def show_options(self,options=None,title=None):
        print("\n")
        if isinstance(options,list):
            terminal_menu = TerminalMenu(menu_entries=options,title = title,menu_highlight_style=("bg_black","fg_yellow"),)
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

    def handler(signum, frame):
        print(red(" Ctrl-c was pressed!!"))
        print(blue(" See you! Have a nice day."))
        exit(1)
    
    signal.signal(signal.SIGINT,handler)

    def exit(self):
        print("Bye!")

    def debug(self):
        import ipdb; ipdb.set_trace()

app = Cli()
app.start()
