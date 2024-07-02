import re

def readandaverage():

    # Using readlines() 
    file1 = open('meeting.json', 'r') 
    Lines = file1.readlines() 
  
    count = 0
    numberoflines = 0
    # Strips the newline character 
    for line in Lines: 
        #print("Line{}: {}".format(count, line.strip()))
        list = line.split (",")
        #print(list[-1 ])
        list2 = list[-1].split (":")
        #print(list2[-1])
        list3 = list2[-1].split ("}")
        #print(list3[0])

        count += int(list3[0])
        numberoflines += 1
    print(count)
    print(numberoflines)
    print(count/numberoflines)

#readandaverage()

def uniqueip():
    # Using readlines() 
    file1 = open('meeting.json', 'r') 
    Lines = file1.readlines() 
  
    count = 0
    numberoflines = 0
    my_list = []
    count2 = 0
    list2 = []
    # Strips the newline character 
    for line in Lines: 
        #print("Line{}: {}".format(count, line.strip())
        #print(line)
        #print(re.findall(r'"ip":"(.+?)"', line))
        m = re.search(r'"ip"', line)
        if m:
            myip = re.sub(r'.*"ip":"([.0-9]*)".*',r"\1",line)
            #print(myip)
            my_list.append(myip)
    for item in my_list:
            if item not in list2:
                    count2 += 1
                    list2.append(item)
    print("number of unique ips are:", count2)

    
      
uniqueip()    
