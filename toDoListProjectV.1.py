#!/usr/bin/env python
# coding: utf-8

# In[35]:


#To Do List Project
#Create GUI Elements
import tkinter as tk
import random
import datetime


#Root Window
root = tk.Tk()

#Change Title
root.title("Arnav's To Do List")

#Change window size
root.geometry("200x500")

#Create an empty list

tasks = []

#For testing purposes use a default list

tasks = ["call mom", "buy a guitar","eat icecream"] 

#Functions

def update_listbox():
    #clear the current list
    clear_listbox()
    #populate the listbox
    for task in tasks:
        lb_tasks.insert("end", task)
        
def clear_listbox():
    lb_tasks.delete(0, "end")
        
def add_task():
    #get task to add
    task = txt_input.get()
    #make sure task is not empty
    if task !="":
        #append to the list
        tasks.append(task)
        #update the listbox
        update_listbox()
    else: 
        lbl_display["text"] = "Please enter a task"
    txt_input.delete(0,"end")

def del_all():
    #global tasks list
    global tasks
    #clear the tasks list
    tasks = []
    #update the listbox
    update_listbox()
    

def del_one():
    #get the text of the currently selected item
    task = lb_tasks.get("active")
    #confirm its in the list
    if task in tasks:
        tasks.remove(task)
    #update the listbox
    update_listbox()

def sort_asc():
    tasks.sort()
    #update the listbox
    update_listbox()

def sort_desc():
    tasks.sort()
    #reverse the list
    tasks.reverse()
    #update the listbox
    update_listbox()

def choose_random():
    #choose random task
    task = random.choice(tasks)
    #update the display label
    lbl_display["text"]=task

def show_number_of_tasks():
    #get # of tasks
    number_of_tasks = len(tasks)
    #create and format message
    msg = "Number of tasks: %s" %number_of_tasks
    #display the message
    lbl_display["text"]= msg
def save():
    #file name
    current_dt = datetime.datetime.now()

    date = (current_dt.strftime("%m.%d.%y"))

    path = "/Users/abajpay/Downloads/6testtoDoList"

    file_name = path + date + '.txt'
    
    #write listbox to file
    
    with open(file_name, "w") as wf:
        global tasks
        for list_item in tasks:
            wf.write("%s\n" % list_item)
        wf.close()
    
    


lbl_title = tk.Label(root, text="To-Do-List", bg="white")
lbl_title.pack()

lbl_display = tk.Label(root, text="", bg="white")
lbl_display.pack()

txt_input = tk.Entry(root, width=15)
txt_input.pack()

btn_add_task = tk.Button(root, text="Add Task", fg="green", bg="white", command=add_task)
btn_add_task.pack()

btn_del_one = tk.Button(root, text="Delete", fg="green", bg="white", command=del_one)
btn_del_one.pack()

btn_del_all = tk.Button(root, text="Delete All", fg="green", bg="white", command=del_all)
btn_del_all.pack()


btn_sort_asc = tk.Button(root, text="Sort (ASC)", fg="green", bg="white", command=sort_asc)
btn_sort_asc.pack()

btn_sort_desc = tk.Button(root, text="Sort (DESC)", fg="green", bg="white", command=sort_desc)
btn_sort_desc.pack()

btn_choose_random = tk.Button(root, text="Choose Random", fg="green", bg="white", command=choose_random)
btn_choose_random.pack()

btn_number_of_tasks = tk.Button(root, text="Number of Tasks", fg="green", bg="white", command=show_number_of_tasks)
btn_number_of_tasks.pack()

btn_save = tk.Button(root, text="Save", fg="green", bg="white", command=save)
btn_save.pack()

btn_exit = tk.Button(root, text="Exit", fg="green", bg="white", command=exit)
btn_exit.pack()

lb_tasks = tk.Listbox(root)
lb_tasks.pack()




root.mainloop()


# In[ ]:





# In[ ]:




