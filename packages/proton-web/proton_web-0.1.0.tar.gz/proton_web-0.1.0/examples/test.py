

import sys
sys.path.append('..')

import proton as pt
if __name__ == "__main__":  
    win = pt.Window("Hi mom!", ".")
    win.start(debug=True)
    document = pt.Document(win)
    