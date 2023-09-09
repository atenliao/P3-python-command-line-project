from simple_term_menu import TerminalMenu

class Prompt():

    def askQuestion(self, question):
        userInput = input(question +"\n")
        if self.confirm(userInput):
            return userInput
        else:
            return askQuestion(question)
    


    def confirm(self,content,input="input"):
        print(f"your {input} is {content}\n are you confirm\n")
        
        return self.yesno() == "Yes"

    def yesno(self, option=None):
        options = ["Yes","No"]
        if isinstance(option,list):
            options.extend(option)
        elif option:
            options.append(option)
        return self.makeMenu(options)

    def makeMenu(self, options, option = None):
        
        if option:
            options.append(option)
        menu = TerminalMenu(options)
        selection = menu.show()
        return options[selection]

    def getGender(self):
        options=["Female","Male"]
        options_dic = {
            1: "Female",
            2: "Maile"
        }
        gender_key = self.confirm(self.makeMenu(options),input="Gender")
        
        return options_dic.get(gender_key,"None")

    def getShift(self):
        options=[
        '7:30am-6:00pm', 
        '7:30am-12:30pm', 
        '1:00pm-6:00pm', 
        '6:30pm-5:00am', 
        '6:30pm-11:30pm',
        '0:00am-5:00am'
        ]
        options_dic={
            1: '7:30am-6:00pm', 
            2: '7:30am-12:30pm', 
            3: '1:00pm-6:00pm', 
            4: '6:30pm-5:00am', 
            5: '6:30pm-11:30pm',
            6: '0:00am-5:00am'
        }
        default= '7:30am-6:00pm'
        shift_key = self.confirm(self.makeMenu(options),input="time shift")
        return options_dic.get(shift_key, default)