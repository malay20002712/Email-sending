from smtplib import *
from tkinter import *

# my_email = 'malaykumarpurohit@gmail.com'
# password = 'very secret password'
#
# connection = SMTP('smtp.gmail.com')
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs='mkp777222@gmail.com',
#                     msg='hello Malay')
# connection.close()

window = Tk()
window.title('email sending app')
window.minsize(width=1000, height=1000)


def command_send():
    subject = t.get()
    from_email = t1.get()
    to_email = t2.get()
    text_data = te.get("1.0","end")
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=from_email, password='*********')
        message = 'Subject: ' + subject + '\n\n' + text_data
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=message)


t = Entry(master=window, fg='red')
t.insert(END, 'Subject')
t.pack()

t1 = Entry(master=window, fg='red')
t1.insert(END, 'FROM')
t1.pack()

t2 = Entry(master=window, fg='red')
t2.insert(END, 'TO')
t2.pack()

te = Text(master=window, width=50, height=30, fg='red', bg='violet')
te.insert(END, 'body')
te.pack()

b = Button(text='send', command=command_send, fg='red', bg='black')
b.pack()
mainloop()
