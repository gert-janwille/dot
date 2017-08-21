import time
import dot.common.ui as ui

def countdown(n) :
    while n > 0:
        print '%s...'%(n)
        time.sleep(1)
        n = n - 1
        if n ==0:
            return 0

def clearScreen(args):
    window = ui.UiTemplate()
    window.clearScreen()
