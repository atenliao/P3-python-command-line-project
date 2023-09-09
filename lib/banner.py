from pyfiglet import figlet_format
from prettycli import color
class Banner():
    def Displaystring(string,r=150,g=152,b=23):
        print(color(figlet_format(string,width=220)).rgb_fg(r,g,b))