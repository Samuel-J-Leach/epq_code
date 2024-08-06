import tkinter as tk
import time
from RSA import ENCRYPT, DECRYPT, BFPK, VIEWLOG

#encryption tool GUI
class APP(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("encryption tool")
        self.configure(background = "black")
        #self.geometry("500x500")

        frame1 = tk.Frame(self)
        frame1.configure(background = "black")
        frame2 = tk.Frame(self)
        frame2.configure(background = "black")
        frame3 = tk.Frame(self)
        frame3.configure(background = "black")
        frame4 = tk.Frame(self)
        frame4.configure(background = "black")
        
        frame1.pack()
        frame2.pack()
        frame3.pack()
        frame4.pack()
        
        self.greeting = tk.Label(frame1,
                                 text = "RSA encryption and decryption",
                                 fg = "#5afc03",
                                 bg = "black")
        self.original = tk.Label(frame2,
                                 text = "number to encrypt/decrypt: ",
                                 fg = "#5afc03",
                                 bg = "black")
        self.n = tk.Label(frame3,
                          text = "N: ",
                          fg = "#5afc03",
                          bg = "black")
        self.ed = tk.Label(frame3,
                           text = "E/D: ",
                           fg = "#5afc03",
                           bg = "black")
        self.entry1 = tk.Entry(frame2,
                               fg = "black",
                               bg = "#5afc03",
                               width = 25)
        self.entry2 = tk.Entry(frame3,
                               fg = "black",
                               bg = "#5afc03",
                               width = 25)
        self.entry3 = tk.Entry(frame3,
                               fg = "black",
                               bg = "#5afc03",
                               width = 25)
        self.encrypt = tk.Button(frame4,
                                 text = "encrypt",
                                 fg = "black",
                                 bg = "#5afc03",
                                 command = self.on_encrypt)
        self.decrypt = tk.Button(frame4,
                                 text = "decrypt",
                                 fg = "black",
                                 bg = "#5afc03",
                                 command = self.on_decrypt)
        self.bfpk = tk.Button(frame4,
                              text = "brute force",
                              fg = "black",
                              bg = "#5afc03",
                              command = self.on_bfpk)
        self.viewlog = tk.Button(frame4,
                                 text = "view log",
                                 fg = "black",
                                 bg = "#5afc03",
                                 command = self.on_viewlog)
        self.textbox = tk.Text(self,
                               fg = "black",
                               bg = "#5afc03",
                               width = 50)
        self.statustext = tk.StringVar()
        self.statustext.set("")
        self.status = tk.Label(self,
                               textvariable = self.statustext,
                               fg = "#5afc03",
                               bg = "black")
        
        self.greeting.pack()
        self.original.pack(side = tk.LEFT)
        self.entry1.pack(side = tk.LEFT)
        self.n.pack(side = tk.LEFT)
        self.entry2.pack(side = tk.LEFT)
        self.ed.pack(side = tk.LEFT)
        self.entry3.pack(side = tk.LEFT)
        self.encrypt.pack(side = tk.LEFT)
        self.decrypt.pack(side = tk.LEFT)
        self.bfpk.pack(side = tk.LEFT)
        self.viewlog.pack(side = tk.LEFT)
        self.status.pack()
        self.textbox.pack()

    #encrypts input number and displays the result   
    def on_encrypt(self):
        start = time.time()
        self.statustext.set("loading...")
        self.status.update_idletasks()
        self.statustext.set("")
        if self.entry1.get() == "":
            return
        if self.entry2.get() == "" and self.entry3.get() == "":
            result = ENCRYPT(int(self.entry1.get()), "empty")
            self.textbox.insert(tk.END, str(time.ctime())+"\n")
            self.textbox.insert(tk.END, "encrpted number: "+str(result[0])+"\ndecrypted number: "+self.entry1.get()+"\npublic key: "+str(result[1])+"\nprivate key: "+str(result[2])+"\n\n\n")
        elif self.entry2.get() != "" and self.entry3.get() != "":
            result = ENCRYPT(int(self.entry1.get()), (int(self.entry2.get()), int(self.entry3.get())))
            self.textbox.insert(tk.END, str(time.ctime())+"\n")
            self.textbox.insert(tk.END, "encrpted number: "+str(result[0])+"\ndecrypted number: "+self.entry1.get()+"\npublic key: "+str(result[1])+"\n\n\n")
        self.textbox.see("end")
        print(time.time()-start)

    #decrypts input number and displays the result
    def on_decrypt(self):
        start = time.time()
        self.statustext.set("loading...")
        self.status.update_idletasks()
        self.statustext.set("")
        if self.entry1.get() == "" or self.entry2.get() == "" or self.entry3.get() == "":
            return
        result = DECRYPT(int(self.entry1.get()), (int(self.entry2.get()), int(self.entry3.get())))
        self.textbox.insert(tk.END, str(time.ctime())+"\n")
        self.textbox.insert(tk.END, "decrypted number: "+str(result)+"\nencrypted number: "+self.entry1.get()+"\nprivate key: ("+self.entry2.get()+", "+self.entry3.get()+")"+"\n\n\n")
        self.textbox.see("end")
        print(time.time()-start)

    #brute force attack to decrypt the input number without the private key
    def on_bfpk(self):
        start = time.time()
        self.statustext.set("loading...")
        self.status.update_idletasks()
        if self.entry1.get() == "" or self.entry2.get() == "" or self.entry3.get() == "":
            return
        result = BFPK(self.entry1.get(), (self.entry2.get(), self.entry3.get()))
        original = result[0]
        private = result[1]
        self.textbox.insert(tk.END, str(time.ctime())+"\n")
        self.textbox.insert(tk.END, "encrypted number: "+self.entry1.get()+"\npublic key: ("+self.entry2.get()+", "+self.entry3.get()+")\nprivate key: ("+str(private[0])+","+str(private[1])+")\ndecrypted number: "+str(original)+"\n\n\n")
        self.textbox.see("end")
        self.statustext.set("")
        print(time.time()-start)

    #displays all previously generated encryption keys
    def on_viewlog(self):
        start = time.time()
        self.statustext.set("loading...")
        self.status.update_idletasks()
        self.textbox.insert(tk.END, str(time.ctime())+"\n")
        log = VIEWLOG()
        for i in log:
            self.textbox.insert(tk.END, i)
        self.textbox.insert(tk.END, "\n\n")
        self.textbox.see("end")
        self.statustext.set("")
        print(time.time()-start)


app = APP()
app.mainloop()
