from tkinter import *
import mainn
import washscr
import ironscr
import washandironnscr
import transaction_slip

class orderscr:
    
        def ord(self):
            self.root71 = Tk()
            self.root71.geometry('500x500')
            
            def washh():
                self.root71.destroy()
                a=washscr.w__s()
                a.washingscreen()
                
            def ironn():
                self.root71.destroy()
                b=ironscr.i__s()
                b.ironingscreen()
                
            def washairon():
                self.root71.destroy()
                c=washandironnscr.wi__s()
                c.wash_ironscreen()

            def trans_id():
                        
                trans = transaction_slip.Trans_id()    # calling the class user_slip
                trans.slip()     # calling the function trans from transaction_slip
                
                
            self.wbutton= Button(self.root71, text='WASHING', font=("gotham", 16, "bold"), width=22,height=2, bd=0,fg='red',bg='black',command=washh)
            self.wbutton.place(x=120,y=100)

            self.ibutton= Button(self.root71, text='IRONING', font=("gotham", 16, "bold"), width=22,height=2, bd=0,fg='red',bg='black',command=ironn)
            self.ibutton.place(x=120,y=200)
        
            self.wandibutton= Button(self.root71, text='WASHING & IRONING', font=("gotham", 16, "bold"), width=22,height=2, bd=0,fg='red',bg='black',command=washairon)
            self.wandibutton.place(x=120,y=300)

            self.obutton= Button(self.root71, text='ORDER', font=("gotham", 16, "bold"), width=10,height=1, bd=0,fg='red',bg='black' , command = trans_id)
            self.obutton.place(x=220,y=410)

            
        
