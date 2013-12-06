import win32com.client as comclt
import thread
import time
import sys
import pyHook
import pythoncom

def get_txt(lang):
    try:
        txt = open(langs[lang]).read()
        return txt
    except:
        return "no input file"
        thread.start_new()
def start_inputing(txt):
    special = ['`','!','^','+']
    shifts = ['"','}','_','|',':','>','<','?']
    wsh= comclt.Dispatch("WScript.Shell")
    str_len = len(txt)
    for i in range(0,str_len):
        time.sleep(2)
        if txt[i] in special:
            t = "{"+txt[i]+"}"
        elif txt[i] in shifts:
            t = "+"+txt[i]    
        else:
            t = txt[i]
        
        wsh.SendKeys(t)
def OnKeyboardEvent(event):
    if event.Ascii == 3:
        sys.exit() 


def hook_detect():
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()


def main():
    global langs
    
    langs = {'python':'python.txt','php':'php.txt','css':'css.txt','javascript':'js.txt'}
    try:
        lang = sys.argv[1]
        if not lang in langs:
            lang = "python"
    except:
        lang = "python"
    try:
        time_t = sys.argv[2]
        time_t = int(time_t)
    except:
        time_t = 0
    txt = get_txt(lang)
    time_t = 60*time_t
    thread.start_new(hook_detect,())
    print 66
    time.sleep(time_t)
    
    start_inputing(txt)

if __name__ == '__main__':
	main()

