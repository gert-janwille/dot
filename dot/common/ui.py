"""
This module was made to handle the curses sections for the ap selection,
template selection and the main window
"""
import os

class UiTemplate(object):

    def __init__(self):

        self.green_text = None
        # heightlight the phishing scenario
        self.heightlight_text = None
        # record current hightlight template number
        self.heightlight_number = 0
        # store the current page number
        self.page_number = 0
        # store the phishing contents of each scenario
        self.sections = list()
        # map the section to page number
        self.sec_page_map = {}
        # the window size for (y, x)
        self.dimension = [0, 0]


    def clearScreen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
