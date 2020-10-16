import tkinter

class OngletsPackets():

    def __init__(self, main_onglets):
        self.onglets_packets = tkinter.ttk.Frame(main_onglets)       
        self.onglets_packets.pack()
        main_onglets.add(self.onglets_packets, text='Packet')
        self.create_text()
        

    def create_text(self):
        self.richTextBox1= tkinter.Text(self.onglets_packets,font = '{MS Sans Serif} 10')
        self.richTextBox1.place(relx=0.05, rely=0.07, relwidth=0.85, relheight=0.75)
        #self.scrollbar = Scrollbar(self.richTextBox1)
        #self.scrollbar.pack( side = RIGHT, fill=Y)

    def print_packet(self,text):
        self.richTextBox1.insert("end",text+"\n")
        self.richTextBox1.see("end")