def add_time(t1,t2,day=""):
    output = ""
    new_Day = ""
    daysList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    #Checking if the t2 is 24:00 since it indicates that only one day has passed
    if(t2 !="24:00"):
        #having three variables containing the period (old_period), t1 hour + t2 hour (Hours) , t1 Minute + t2 Minute (Minutes)
        old_period = t1.split(" ")[1]
        Hours = int(t1.split(" ")[0].split(":")[0]) + int(t2.split(":")[0])
        Minutes = int(t1.split(" ")[0].split(":")[1]) + int(t2.split(":")[1])
        #storing the new period and new day 
        new_Period = ""
        #collecting the number of days passed
        days_passed = ""
        #if the minutes is greater than 60 , add 1 to hours and if the minutes is a single digit (e.g: 5) put a 0 at the start (e.g: 5 -> 05)
        if(Minutes >= 60):
            Hours = Hours + 1
            Minutes = Minutes-60
        if(len(str(Minutes))==1):
            Minutes = "0"+str(Minutes)
        #checking the period and changing it depending on the old period and whether or not Hours value is greater than 12
        if(old_period=="AM" and Hours >= 12):
            new_Period = "PM"
        elif(old_period=="PM" and Hours >=12):
            new_Period = "AM"
        else:
            new_Period = old_period
        #determining the number of days passed
        if(Hours < 24 and (old_period == "PM" and new_Period=="AM")):
            days_passed = "(next day)"
        elif((Hours//24)+1>1):
            days_passed = "({0} days later)".format((Hours//24)+1)
        #if day is given , get the new_day 
        if(day != ""):
            counter = 0
            i = list(map(lambda x: x.lower(),daysList)).index(day.lower())
            while(counter < ((Hours//24)+1)):
                i += 1
                if(i>6):
                    i = 0
                counter+=1
            new_Day = daysList[i]
        #if Hours is above 12 , do Hours - 12 until it is less than 12
        if(Hours > 12):
            while(Hours > 12):
                Hours = Hours - 12
                if(Hours<=12):
                    break
        #depending on if days_passed and day is empty or not , will determine the output format 
        #when there are no number of days passed
        if(len(days_passed)==0):
            #if day isn't empty
            if(day != ""):
                output = "{0}:{1} {2}, {3}".format(Hours,Minutes,new_Period,day)
            else:
            #if day is empty
                output = "{0}:{1} {2}".format(Hours,Minutes,new_Period)
        #when there are "x" number of days passed
        else:
            if(day ==""):
                output = "{0}:{1} {2} {3}".format(Hours,Minutes,new_Period,days_passed)
            else:
                output = "{0}:{1} {2}, {3} {4}".format(Hours,Minutes,new_Period,new_Day,days_passed)
    else:
        if(day==""):
            output = "{0} (next day)".format(t1)
        else:
            i = list(map(lambda x: x.lower(),daysList)).index(day.lower())
            i += 1
            new_Day = daysList[i]
            output = "{0}, {1} (next day)".format(t1,new_Day)
					
    return output

print(add_time("3:30 PM", "2:12", "Monday"))
print(add_time("8:16 PM", "466:02", "tuesday"))
print(add_time("2:59 AM", "24:00", "saturDay"))
print(add_time("3:30 PM", "2:12"))
print(add_time("9:15 PM", "5:30"))
print(add_time("11:59 PM", "24:05"))
print(add_time("8:16 PM", "466:02"))
print(add_time("11:40 AM","0:25"))
print(add_time("2:59 AM", "24:00"))
print(add_time("5:01 AM", "0:00"))