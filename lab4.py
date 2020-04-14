import PyHook3
import pythoncom

def OnKeyboardEvent(event):

    print(chr(event.Ascii), end='')

    return True

hooks_manager = PyHook3.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()