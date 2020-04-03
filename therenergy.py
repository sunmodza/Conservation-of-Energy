from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
def energy(i,o):
        m=1
        matter={"fp":0,"bp":100,"cs":0.5,"cl":1,"cst":0.48,"lf":80,"ls":540}
        if i>o:
            temp=[i,o]
            o,i=temp[0],temp[1]
        if i<matter["fp"] and o<matter["fp"]:
            dta,dtb,dtc = abs(o-i),0,0
            pa,pb,pc,pd,pf = 1,0,0,0,0
        elif i<matter["fp"] and (o in range(matter["fp"],matter["bp"]) or o==matter["bp"]):
            dta,dtb,dtc = abs(i),abs(o),0
            pa,pb,pc,pd,pf = 1,1,1,0,0
        elif i<matter["fp"] and o>matter["bp"]:
            dta,dtb,dtc = abs(i),abs(matter["bp"]),abs(o-matter["bp"])
            pa,pb,pc,pd,pf = 1,1,1,1,1
        elif (i in range(matter["fp"],matter["bp"]) or i==matter["fp"]) and (o in range(matter["fp"],matter["bp"]) or o==matter["bp"]):
            dta,dtb,dtc = 0,abs(o-i),0
            pa,pb,pc,pd,pf = 0,0,1,0,0
        elif (i in range(matter["fp"],matter["bp"]) or i==matter["fp"]) and (o>matter["bp"]):
            dta,dtb,dtc = 0,abs(matter["bp"]-i),abs(o-matter["bp"])
            pa,pb,pc,pd,pf = 0,0,1,1,1
        elif (i>matter["bp"]  and o>matter["bp"]) or (i==matter["bp"] and matter["bp"]):
            dta,dtb,dtc = 0,0,abs(o-i)
            pa,pb,pc,pd,pf = 0,0,0,0,1
        return (m*matter["cs"]*dta*pa+m*matter["lf"]*pb+m*matter["cl"]*dtb*pc+m*matter["ls"]*pd+m*matter["cst"]*pf)
class gridd(GridLayout):
    def __init__(self, **kwargs):
        super(gridd,self).__init__(**kwargs)
        self.frameout=GridLayout()
        self.frameout.cols=2
        self.frameout.rows=2
        self.ans=GridLayout()
        self.ans.cols=2
        self.ans.rows=1
        self.cols=1
        self.rows=2
        self.add_widget(self.frameout)
        self.add_widget(self.ans)
        self.frameout.add_widget(Label(text="start temp"))
        self.i=TextInput()
        self.frameout.add_widget(self.i)
        self.frameout.add_widget(Label(text="want temp"))
        self.o=TextInput()
        self.frameout.add_widget(self.o)
        self.boolbutton = Button(text="Go")
        self.boolbutton.bind(on_press=self.pressit)
        self.ans.add_widget(self.boolbutton)
        self.out=TextInput()
        self.ans.add_widget(self.out)
        
    def pressit(self,*instance):
        if self.i.text!="" and self.o.text!="":
            self.out.text=str(energy(float(self.i.text),float(self.o.text)))
            
        
    
    
            

class main(App):
    def build(self):
        return gridd()

if __name__ == "__main__":
    main().run()