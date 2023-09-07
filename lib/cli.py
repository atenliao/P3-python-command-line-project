# import ipdb
from prettycli import red
from simple_term_menu import TerminalMenu
from models import Worker
from pyfiglet import figlet_format
import time
import re
from Session import session

class Cli():
    def __init__(self):
        current_worker = None


    def start(self):
        self.clear_screen(1)
        self.welcome()
        options = ["Login","Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        # print(f"You have selected {options[menu_entry_index]}!")
        if options[menu_entry_index] =="Login":
            self.handle_login()
        elif options[menu_entry_index] == "Exit":
            self.exit()

    def welcome(self):
        words = figlet_format("Workers database",width =110)
        print(words)

    def clear_screen(self,lines):
        print("\n" * lines)

    def handle_login(self):
        login = input("Please enter your worker login:\n\n")
        regex = r"[A-Za-z]"
        if re.match(regex,login):
            print("find the worker by login")
            worker = Worker.find_or_create_by(login)
            if worker:

                self.current_worker = worker
                print(session.query(Worker).filter(Worker.login.like(login)).first())
                self.show_worker_options()
                # import ipdb; ipdb.set_trace()
            else:
                print("Please create a new worker")
        else:
            print(red("Invalid login"))
            time.sleep(2)
            self.start()
        
        pass

    def show_worker_options(self):
        options=["All worker", "New worker","Edit worker Info", "Exit"]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()
        print(options[menu_entry_index])
    def exit(self):
        print("Bye!")

app = Cli()
app.start()
# def start():
#     options = ["All workers", "add worker","Exit"]
#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()
#     print(f"You have selected {options[menu_entry_index]}!")
#     # print("Welcome to Worker Tracker!\n")
#     # print("1. ")
#     # print("2. add worker")
#     # print("3. Exit")
#     # user_intput = input("please make selection (1-3): ")
#     # handle_user_input(user_intput)

# def handle_user_input(input):
#     is_number = input.isdigit()
#     if(is_number):
#         selection = int(input)
#         if 1 <= selection  <= 3:
#             handle_selection(selection)
#             print("selection in 1 and 3")
#         #     handle_selection(selection)
#         else:
#             print(red("Incorrect selection"))
#             start()
#         # ipdb.set_trace()

# start()