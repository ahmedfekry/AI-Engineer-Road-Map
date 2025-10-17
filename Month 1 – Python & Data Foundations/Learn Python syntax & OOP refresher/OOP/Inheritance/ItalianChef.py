import sys
import os
sys.path.append(os.path.dirname(__file__))
from Chef import Chef

class ItalianChef(Chef):
    def make_pasta(self):
        print("The Italian chef makes pasta")

    def make_special_dish(self):
        print("The Italian chef makes chicken parm")