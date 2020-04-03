def energy(m,i,o,**kwargs):
        matter={"fp":0,"bp":100,"cs":0.5,"cl":1,"cst":0.48,"lf":80,"ls":540}
        for n,v in kwargs.items():
            matter[n]=v
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