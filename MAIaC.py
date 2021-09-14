from tkinter import *
import yaml
from tkinter import messagebox
import subprocess
import socket
from ssh2.session import Session
    
    
def clicked():
    
    a = click1.get()
    b = click2.get()

    def clicked1():
        res = entry1.get()
        res1 = entry2.get()
        res2 = entry3.get()
        ymlfile(res,res1,res2)
        
        messagebox.showinfo('MAIaC', 'Playbook Generated')
        subprocess.call('echo Copying file to control node', shell= True)
        subprocess.call('pscp -pw wamsHIYLdiT9oE output.yml student1@18.156.91.154:/home/student1', shell=True)
        subprocess.call('echo File copied', shell= True)
        top.destroy()

    if tmp == "Services" and a == "Firewall" and b == "Cisco":
        
        top = Toplevel()
        top.title('Enter parameters')   

        myLabel1 = Label(top, text =" Enter access list number: ")
        myLabel1.grid(row=0, column=0)

        myLabel2 = Label(top, text =" Enter IP address: ")
        myLabel2.grid(row=1, column=0)

        myLabel3 = Label(top, text =" Enter a sequence number: ")
        myLabel3.grid(row=2, column=0)

        entry1 = Entry(top, width= 50, borderwidth= 5)
        entry1.grid(row=0, column=1)

        entry2 = Entry(top, width= 50, borderwidth= 5)
        entry2.grid(row=1, column=1)

        entry3 = Entry(top, width= 50, borderwidth= 5)
        entry3.grid(row=2, column=1)

        button = Button(top, text="ok", bg= "#ffEEAA", fg= "#000000", command=clicked1)
        button.grid(row=3, column=1)
    elif tmp == "Network":
        messagebox.showinfo('MAIaC', 'Component is under development...')
    elif tmp == "IAM":
        messagebox.showinfo('MAIaC', 'Component is under development...')
    elif tmp == "Basic Configuration":
        messagebox.showinfo('MAIaC', 'Component is under development...')
    elif tmp == "Monitoring":
        messagebox.showinfo('MAIaC', 'Component is under development...')
    elif tmp == "Security Controls" and a == "PCI DSS Benchmark" and b == "Linux" :
        messagebox.showinfo('MAIaC', 'Component will be develped soon..')
    elif tmp == "Security Controls" and a == "CIS Benchmark" and b == "Linux" :
        messagebox.showinfo('MAIaC', 'Component will be develped soon..')
    elif tmp == "Maintenance":
        messagebox.showinfo('MAIaC', 'Component will be developed soon..')
    else:
        messagebox.showwarning('Error', 'Select a valid combination')

def ymlfile(res,res1,res2):

    li = str(res)
    ip = str(res1)
    se = str(res2)
    
    value = 'access-list ' + li + ' ' + se + ' deny host ' + ip
    first = {'name': 'create an access list','hosts': 'dc1','connection': 'network_cli','gather_facts': 'false'}
    second = {'name': 'load new acl in interface','ios_config':{'lines': [value]}}
    third = {'tasks':[second]}
    first.update(third)
    stream = open('output.yml', 'w',encoding="utf-8")
    stream.write('---\n')
    yaml.dump([first],stream,sort_keys=False)
    stream.close()

def execute():
    host = "18.156.91.154"
    user = "student1"
    password = "wamsHIYLdiT9oE"

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((host, 22))

    session = Session()
    session.handshake(soc)
    session.userauth_password(user, password)

    channel = session.open_session()
    channel.execute("ansible-playbook output.yml")

    size, data = channel.read()
    while size >0:
        print(data.decode())
        size, data = channel.read()
    channel.close()
    subprocess.call('echo Playbook executed', shell= True)
    



def rbclick(value):

    global tmp, val, val1, click1, click2
    tmp = value
    val1 = ['Windows', 'Linux', 'Mac OS X']
  
    if tmp == "IAM":
        val = ['User', 'User groups']
        
    elif tmp == "Basic Configuration":
        val = ['Hostname', 'Date', 'Time']
        
    elif tmp == "Network":
        val = ['IP addressing', 'DNS', 'DHCP']
        
    elif tmp == "Services":
        val = ['Firewall', 'Router', 'Switch']
        val1 = ['Cisco', 'Palo Alto', 'Fortinet','Juniper']
        
    elif tmp == "Security Controls":
        val = ['CIS Benchmark','PCI DSS Benchmark']
        
    elif tmp == "Maintenance":
        val = ['Start a system','Stop a system','Restart a system','Other']
        
    else:
        val = ['SNMP', 'Syslog']

    click1= StringVar()
    drop1 = OptionMenu(frame,click1,*val)
    drop1.grid(row=2, column=1, padx=10, pady=10)

    click2= StringVar()
    drop2= OptionMenu(frame,click2,*val1)
    drop2.grid(row=3, column=1, padx=10, pady=10)    

# Title for GUI
root = Tk()
root.title("MAIaC")
root.geometry("1000x700")

#frame for the GUI page
frame = LabelFrame(root, text= "Network Automation with Ansible", padx =50, pady =50)
frame.pack(padx=10, pady=10)

#GUI options frame1
frame1 = LabelFrame(frame, text= "Select a component", padx= 25, pady= 25)
frame1.grid(row=0, column= 0, padx =5, pady=5)

click = StringVar()
click.set("IAM")

rbutton1 = Radiobutton(frame1,text = "IAM", variable = click, value = "IAM", command =lambda: rbclick(click.get()))
rbutton2 = Radiobutton(frame1,text = "Basic Configuration", variable = click, value = "Basic Configuration", command = lambda: rbclick(click.get()))
rbutton3 = Radiobutton(frame1,text = "Network", variable = click, value = "Network", command = lambda: rbclick(click.get()))
rbutton4 = Radiobutton(frame1,text = "Services", variable = click, value = "Services", command = lambda: rbclick(click.get()))
rbutton5 = Radiobutton(frame1,text = "Monitoring", variable = click, value = "Monitoring", command = lambda: rbclick(click.get()))
rbutton6 = Radiobutton(frame1,text = "Security Controls", variable = click, value = "Security Controls", command = lambda: rbclick(click.get()))
rbutton7 = Radiobutton(frame1,text = "Maintenance", variable = click, value = "Maintenance", command = lambda: rbclick(click.get()))
rbutton1.pack(padx=5, pady=5, anchor= W)
rbutton2.pack(padx=5, pady=5, anchor= W)
rbutton3.pack(padx=5, pady=5, anchor= W)
rbutton4.pack(padx=5, pady=5, anchor= W)
rbutton5.pack(padx=5, pady=5, anchor= W)
rbutton6.pack(padx=5, pady=5, anchor= W)
rbutton7.pack(padx=5, pady=5, anchor= W)

myLabel2 = Label(frame, text ="Select a category")
myLabel2.grid(row=2, column=0, padx =10, pady=10)

myLabel3 = Label(frame, text ="Select a vendor")
myLabel3.grid(row=3, column=0, padx =10, pady=10)

#GUI buttons frame4
frame4 = LabelFrame(frame, text= "Options", padx= 25, pady= 25)
frame4.grid(row=4, column= 0, padx =5, pady=5)

button1 = Button(frame4, text="Generate Playbook", bg= "#ffEEAA", fg= "#000000", command = clicked)
button1.grid(row=1, column=0, padx=10, pady=10)

button4 = Button(frame4, text="Execute Playbook", bg= "#A2C8C4", fg="#000000", command= execute)
button4.grid(row=1, column=1, padx=10, pady=10)

button2 = Button(frame4, text="Exit", bg= "#a2c8c4", fg= "#000000", command= root.quit)
button2.grid(row=1, column=2, padx=10, pady=10)    
        
root.mainloop()

