#this is disgusting i know im sorry i suck at neat code i need to fix up
#done in approx 2-3 hours (idk i wasn't really counting)

print("begin module...") #debugging done in prints (i removed them all now though because no need)

title = "Password Checker and Generator"
list_of_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS123456789[ !#$%&'()*+,-./[\/]^_"
global score

try:
    import re
    import string
    import time
    import random
    import Tkinter
    from Tkinter import Frame, Text, Tk
    from Tkconstants import YES, BOTH
    from Tkinter import messagebox
except ImportError: #catch importerror, then add in correct information instead of allowing exception to be thrown
    import re
    import string
    import time
    import random
    import tkinter
    from tkinter import Frame, Text, Tk
    from tkinter.constants import YES, BOTH
    from tkinter import messagebox

def set_text(string): #easier than having to write out two lines
    input_field.delete(0, 'end')
    input_field.insert(0, string)

def verify_password(password): #check password integrity
    if len(password) < 10:
        return "too short"

    elif not re.search("[a-z]", password):
        return "no lowercase"

    elif not re.search("[0-9]", password):
        return "no numbers"

    elif not re.search("[A-Z]", password):
        return "no uppercase"

    elif not re.search("[!$#@*+,-./^_]", password):
        return "no specials"

    elif re.search("\s", password):
        return "whitespace character"
    
    else:
        return "valid"
    
def pw_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def go_back_checker():
    root.deiconify()
    check_root.withdraw()

def go_back_generate():
    root.deiconify()
    generate_root.withdraw()

def check_password():
    score = 0
    check_button.config(state='disabled') #to avoid spamming of msgboxes (yes im talking to you)
    contents = checker_field.get()
    password_integrity = verify_password(contents)
    length = len(contents)
    global length_msg
    
    if length > 100: #extra cool kid stuff (:cool:)
        length_msg = "Wow! " + str(length) + " characters! Don't you think that's a bit overboard?"

    elif length < 1:
        messagebox.showwarning("Password Issue", "You didn't input anything! It can't work without input")
        check_button.config(state='normal')
        return 0

    else:
        length_msg = "You use a total of " + str(length) + " characters!"
    
    if password_integrity == "too short":
        messagebox.showwarning("Password Issue", "Password entered is too short! (minimum = 10) ")

    elif password_integrity == "no lowercase":
        messagebox.showwarning("Password Issue", "Password does not have any lowercase characters!")

    elif password_integrity == "no uppercase":
        messagebox.showwarning("Password Issue", "Password does not have any uppercase characters!")

    elif password_integrity == "no specials":
        messagebox.showwarning("Password Issue", "Password does not have any special characters! (ex: !$@)")

    elif password_integrity == "no numbers":
        messagebox.showwarning("Password Issue", "No numbers in password!")

    elif password_integrity == "whitespace character":
        messagebox.showwarning("Password Issue", "Whitespace character detected! Do not use spaces in your password!")

    elif password_integrity == "valid":
        messagebox.showinfo("Password Valid!", "Nice job! Password entered is valid! " + length_msg)

    else:
         messagebox.showerror("Error!", "No clue what you have done, however it's caused an error with the checking system! Verify your password you damn hacker")

    check_button.config(state='normal')

def generate_password():
    password = ''.join(random.choice(list_of_chars) for _ in range(20))
    
    set_text(password)

def initiate_check():
    root.withdraw()
    global check_root
    check_root = tkinter.Tk()
    
    check_root.title(title)
    check_root.configure(background="#5b90e5")
    check_root.geometry("320x100")

    global checker_field
    global check_button
    checker_field = tkinter.Entry(check_root)
    check_button = tkinter.Button(check_root, text="Verify Password", command=check_password)
    goback_button = tkinter.Button(check_root, text="Go Back", command=go_back_checker)

    checker_field.pack()
    check_button.pack()
    goback_button.pack()
    
    check_root.focus() 
    check_root.wm_attributes("-topmost", 1)
    check_root.wm_iconbitmap("lock.ico")
    check_root.resizable(False, False)
    check_root.mainloop()

    
def initiate_generate():
    root.withdraw()
    global generate_root
    generate_root = tkinter.Tk()

    generate_root.title(title)
    generate_root.configure(background="#5b90e5")
    generate_root.geometry("320x100")

    global input_field
    input_field = tkinter.Entry(generate_root)
    input_field.pack()

    begin_button = tkinter.Button(generate_root, text="Generate", command=generate_password).pack()
    goback_button = tkinter.Button(generate_root, text="Go Back", command=go_back_generate).pack()
    
    generate_root.focus() 
    generate_root.wm_attributes("-topmost", 1)
    generate_root.wm_iconbitmap("lock.ico")
    generate_root.resizable(False, False)
    generate_root.mainloop()


#settings for the main window
global root
root = tkinter.Tk()
root.configure(background="#5b90e5")
root.title(title)
root.geometry("320x100")

#widgets for the main window
info_label = tkinter.Label(root, text="Choose an option:", bg="#5b90e5")
checker_button = tkinter.Button(root, text="Check Password", command=initiate_check)
generate_button = tkinter.Button(root, text="Generate Password", command=initiate_generate)

#pack widgets
info_label.pack()
checker_button.pack()
generate_button.pack()

#load in main window 
root.focus() #direct input focus to this window
root.wm_attributes("-topmost", 1) #make window topmost (essientally always on top of most applications)
root.wm_iconbitmap("lock.ico")
root.resizable(False, False)
root.mainloop()
