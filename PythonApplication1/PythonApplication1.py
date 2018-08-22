import sys
import nmap
import tkinter as tk

#Application Class
class Application(tk.Frame):             
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  
        self.scanner = nmap.PortScanner()
        self.grid()       
        self.createWidgets()


    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit',                                      #Quit button 
            command=self.quit)            
        self.quitButton.grid(row=0, column=0)  
        self.scanButton = tk.Button(self, text='Scan:',command=self.startScan)              #Scan button
        self.scanButton.grid(row=1, column=0)
        self.IPLabel = tk.Label(self, text='IP and Port Range (optional):')                 #IP label
        self.IPLabel.grid(row=6, column=7)
        self.entryField = tk.Entry(width=15)                                                #IP Entry field
        self.entryField.grid(row=0, column=3)
        self.portEntry = tk.Entry(width=8)                                                  #Ports Entry
        self.portEntry.grid(row=0, column=4)                
        self.hostListTextBox = tk.Text(self,state=tk.NORMAL, height=5, width=40)            #Host List text box
        self.hostListTextBox.grid(row=10, column=1)                         

    def startScan(self):
        address = self.entryField.get()
        if len(self.portEntry.get()) != 0:                                                  #Port range was provided
            thePorts = self.portEntry.get()
            print('With ports' + thePorts)
            self.scanner.scan(hosts=address,ports=thePorts)
            hostList= self.scanner.all_hosts()
            for host in hostList:
                hostInfo = host + " Name: " + self.scanner[host].hostname()
                for protocol in self.scanner[host].all_protocols():
                    hostInfo += " Protocol: " + protocol + " Ports:"
                    for key in self.scanner[host][protocol].keys():
                        hostInfo += str(key) + ", "
                self.hostListTextBox.insert(tk.INSERT, hostInfo + "\n")
        else:                                                                               
            self.scanner.scan(address)
            hostList = self.scanner.all_hosts()
            for host in hostList:
                hostInfo = host + " Name: " + self.scanner[host].hostname()
                for protocol in self.scanner[host].all_protocols():
                    hostInfo += " Protocol: " + protocol + " Ports:"
                    for key in self.scanner[host][protocol].keys():
                        hostInfo += str(key) + ", "
                self.hostListTextBox.insert(tk.INSERT, hostInfo + "\n")


#Run Application
app = Application()                       
app.master.title('Nmap Applicaton') 
app.mainloop()                            
