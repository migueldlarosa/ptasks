import wx
import sqlite3
import time

location = 'data'
table_name = 'ptasks'

def init():    
    global conn
    global c
    conn = sqlite3.connect(location)
    c = conn.cursor()
    create_database()

def create_database():
    sql = 'create table if not exists ' + table_name + ' (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duedate TEXT, inputdate TEXT, status TEXT)'
    c.execute(sql)
    conn.commit()

def insert_record(name, duedate, status):
    inputdate = time.strftime("%d/%m/%Y %H:%M:%S")
    c.execute("insert into " + table_name + " (name, duedate, inputdate, status) values (?, ?, ?, ?)",
            (name, duedate, inputdate, status))
    conn.commit()

def ask(parent=None, message='', default_value=''):
    dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dlg.ShowModal()
    result = dlg.GetValue()
    dlg.Destroy()
    return result

init()

# Initialize wx App
app = wx.App()
app.MainLoop()

# Call Dialog
x = ask(message = 'Tarea')
y = ask(message = 'Due')
z = ask(message = 'Estado')
status = z
#print 'Your name was', x

if x:
   if y:
       insert_record(x, y, status)
   else:
       duetoday = time.strftime("%d/%m/%Y %H:%M:%S")
       insert_record(x, duetoday, status) 
else:
   print 'no input'
