import tkinter as tk
import pywhatkit

root = tk.Tk()
root.title("ChatBot for WhatsApp")
root.geometry("600x408+20+20")
root.configure(bg = 'Light grey')
phone_var = tk.StringVar()
message_var = tk.StringVar()
hours_var = tk.IntVar()
minutes_var = tk.IntVar()
def submit():
    phone_num = phone_var.get()
    message = message_var.get()
    hours = hours_var.get()
    minutes = minutes_var.get()

    pywhatkit.sendwhatmsg(phone_num, message, hours, minutes)

name_label = tk.Label(root, text = "Phone Number: ", font = ('JetBrains Mono NL', 18, 'bold'))
name_entry = tk.Entry(root, textvariable = phone_var, font = ('JetBrains Mono NL', 14, 'italic'), width = 34)

message_label = tk.Label(root, text = "Message: ", font = ('JetBrains Mono NL', 18, 'bold'))
message_entry = tk.Entry(root, textvariable = message_var, font = ('JetBrains Mono NL', 14, 'italic'), width = 34)

hours_label = tk.Label(root, text = "Hours: ", font = ('JetBrains Mono NL', 18, 'bold'))
hours_entry = tk.Entry(root, textvariable = hours_var, font = ('JetBrains Mono NL', 14, 'italic'), width = 34)

minutes_label = tk.Label(root, text = "Minutes: ", font = ('JetBrains Mono NL', 18, 'bold'))
minutes_entry = tk.Entry(root, textvariable = minutes_var, font = ('JetBrains Mono NL', 14, 'italic'), width = 34)

send_btn = tk.Button(root, text = "Send message", command  = submit, width = 14, height = 1, font = ('JetBrains Mono NL', 14))

name_label.grid(row = 3, column = 2)
name_entry.grid(row = 3, column = 3, pady = 15)

message_label.grid(row = 5, column = 2)
message_entry.grid(row = 5, column = 3, pady = 15)

hours_label.grid(row = 7, column = 2)
hours_entry.grid(row = 7, column = 3, pady = 15)

minutes_label.grid(row = 9, column = 2)
minutes_entry.grid(row = 9, column = 3, pady = 15)

send_btn.grid(row = 11, column = 2, pady = 15)
root.mainloop()
