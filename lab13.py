from tkinter import *
import psutil
from tkinter import messagebox as mb


class Priority:
    def __init__(self, pid=None, value=None):
        self.pid = pid
        self.value = value


selected_priority = Priority()

second_window = None


def get_processes_info():
    processes = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'nice'])
        except psutil.NoSuchProcess:
            pass
        else:
            processes.append(pinfo)

    return processes


def priority_converter(priority):
    output_value = ""
    if priority == "Priority.IDLE_PRIORITY_CLASS":
        output_value = "idle"
    if priority == "Priority.BELOW_NORMAL_PRIORITY_CLASS":
        output_value = "below normal"
    if priority == "Priority.NORMAL_PRIORITY_CLASS":
        output_value = "normal"
    if priority == "Priority.ABOVE_NORMAL_PRIORITY_CLASS":
        output_value = "above normal"
    if priority == "Priority.HIGH_PRIORITY_CLASS":
        output_value = "high"
    if priority == "Priority.REALTIME_PRIORITY_CLASS":
        output_value = "realtime"
    if priority == "None":
        output_value = "none"

    return output_value


def save_priority():
    try:
        process = psutil.Process(pid=selected_priority.pid)
        if selected_priority.value == 1:
            process.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
        if selected_priority.value == 2:
            process.nice(psutil.NORMAL_PRIORITY_CLASS)
        if selected_priority.value == 3:
            process.nice(psutil.ABOVE_NORMAL_PRIORITY_CLASS)
        if selected_priority.value == 4:
            process.nice(psutil.HIGH_PRIORITY_CLASS)

        processes = get_processes_info()
        listbox_1.delete(0, 999999999)

        for process in processes:
            item = str(process.get("pid")) + ") " + process.get("name") + " | " + priority_converter(
                str(process.get("nice")))
            listbox_1.insert(END, item)
    except psutil._exceptions.AccessDenied:
        mb.showerror("Error", "Access denied")
        second_window.destroy()
        return

    mb.showinfo("Success", "Priority was changed")
    second_window.destroy()


def update_selected_priority(value):
    selected_priority.value = value


def change_priority(event):
    global second_window

    second_window = Toplevel(root)
    second_window.geometry("400x200")
    second_window.resizable(0, 0)
    second_window.focus()

    index = listbox_1.curselection()[0]
    item = listbox_1.get(index)
    pid = item.split(")")[0].strip()
    selected_priority.pid = int(pid)
    pname = item.split(")")[1].split("|")[0].strip()

    title_label = Label(second_window, text="Change process priority:", font=("Helvetica", 16, "bold"))
    title_label.pack()
    process_label = Label(second_window, text=pname)
    process_label.pack()

    priority_value = IntVar()
    radiobutton_priority_below_normal = Radiobutton(second_window, text="BELOW NORMAL", value=1,
                                                    variable=priority_value,
                                                    command=lambda: update_selected_priority(1))
    radiobutton_priority_below_normal.pack()
    radiobutton_priority_normal = Radiobutton(second_window, text="NORMAL", value=2, variable=priority_value,
                                              command=lambda: update_selected_priority(2))
    radiobutton_priority_normal.pack()
    radiobutton_priority_abowe_normal = Radiobutton(second_window, text="ABOWE NORMAL", value=3,
                                                    variable=priority_value,
                                                    command=lambda: update_selected_priority(3))
    radiobutton_priority_abowe_normal.pack()
    radiobutton_priority_high = Radiobutton(second_window, text="HIGH", value=4, variable=priority_value,
                                            command=lambda: update_selected_priority(4))
    radiobutton_priority_high.pack()

    button_set_priority_save = Button(second_window, text="Save priority", command=save_priority)
    button_set_priority_save.pack()


# main window properties;
root = Tk()
root.geometry("1000x500")
root.resizable(0, 0)

# scrollbar properties;
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

# listboxes properties;
listbox_1 = Listbox(width=400, yscrollcommand=scrollbar.set)
listbox_1.pack(side=LEFT, fill=BOTH)
listbox_1.bind("<Button-3>", change_priority)
scrollbar.config(command=listbox_1.yview)

processes = get_processes_info()
for process in processes:
    item = str(process.get("pid")) + ") " + str(process.get("name")) + " | " + priority_converter(str(process.get("nice")))
    listbox_1.insert(END, item)

# start window;
root.mainloop()