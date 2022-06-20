
import xml.etree.ElementTree as ET
import os
def appMenu(appTask, role):
    # only show what the user's role allows
    itemnumber = 1;
    for item in appTask:
        if itemnumber == 1:
            if role == "Administrator":
                print(itemnumber," - ",item.attrib['Name'])
                itemnumber += 1
            else:    
                itemnumber += 1
        elif itemnumber == 2:
            if role == "Security Officer" or role == "Administrator":
                print(itemnumber," - ",item.attrib['Name'])
                itemnumber += 1
            else:
                itemnumber += 1
        else:
            print(itemnumber," - ",item.attrib['Name'])
            itemnumber += 1
    selection = int(input("Please Select:"))
    if selection == 1: print("Admin access granted.")
    if selection == 2: print("Welcome, Security Officer!")
    if selection == 3: print("Welcome! You have no authority.")
    if selection == 4: print("Command 'Help' is not working. Please press 'Help' for help with this issue.")
    if selection == 5: 
        print("Exiting! Goodbye.")
        quit()
	
    return
    
def parseRBAC(theuser):
    mytree = ET.parse('rmmanager.xml')
    myroot = mytree.getroot()

    rmapptask = list(mytree.iter("RMAppTask"))

    rmrole = list(mytree.iter("RMRole"))
     
    role = myroot.findtext('./RMApplication/RMRole/RMTaskLink')

    res = []
    for child in myroot:
        r = []
      
    for element in child:
        
        new = element.tag 
        r.append(new)
        for subelement in element:
            #print("          ",subelement.tag,subelement.text)
            if theuser == subelement.text:
                role = text
            tag = subelement.tag
            text = subelement.text

    res.append(r)
    
    print("[    Menu    ]")
    print("User: ", theuser)
    appMenu(rmapptask,role)
    return;
    
def main():
    theuser =  os.getlogin() 
    parseRBAC(theuser)

if __name__ == "__main__":
     main()


