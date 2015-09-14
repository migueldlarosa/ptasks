import wx
import sqlite3
import time

location = 'data'
table_name = 'ptasks'

def init():
    global conn
    global c
    conn = sqlite3.connect(location)
    conn.row_factory = lambda cursor, row: row[0]
    c = conn.cursor()
    create_database()

def create_database():
    sql = 'create table if not exists ' + table_name + ' (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duedate TEXT, inputdate TEXT, status TEXT)'
    c.execute(sql)
    conn.commit()

def update_record(name):
    inputdate = time.strftime("%H:%M:%S")
    fname = int(''.join(map(str,name)))
    rname = ids[fname]
    c.execute("UPDATE "+ table_name +" SET status = 'fin' WHERE name = '"+ rname +"'")
    conn.commit()
#    c.execute("insert into " + table_name + " (name, duedate, inputdate, status) values (?, ?, ?, ?)",
#            (name, duedate, inputdate, status))
#    conn.commit()

def ask(choices, parent=None, message='', title=''):
#    dlg = wx.TextEntryDialog(parent, message, defaultValue=default_value)
    dlg = wx.MultiChoiceDialog(parent, message, title, choices)
    dlg.ShowModal()
    result = dlg.GetSelections()
    selection = result
    dlg.Destroy()
    return selection

init()

# Initialize wx App
app = wx.App()
app.MainLoop()

# Call Dialog
#conn.row_factory = lambda cursor, row: row[0]
ids = c.execute('SELECT name FROM ptasks where status<>"fin"').fetchall()
ltasks = ids
x = ask(message = 'Tarea', title='Terminar Tarea', choices = ltasks)

if x:
   update_record(x)
else:
   print 'no input'
