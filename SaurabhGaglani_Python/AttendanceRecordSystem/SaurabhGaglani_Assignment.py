import datetime

def login():

    print("Attendance Recording")
    print("="*40)
    name_to_check = input("Name: ")
    password_to_check = input("Password: ")
    x = open("Login_data.txt", "r")
    data = x.read().split('\n')
    names = []
    passwords = []
    for i in range(0, len(data)-1,2):
        name = data[i]
        names.append(name)
        password = data[i+1]
        passwords.append(password)

    if name_to_check in names and password_to_check in passwords:
        login_status = "s"
    else:
        login_status = "f"

    return name_to_check, login_status


def next(name):
    print()
    print(f"Welcome {name}")
    print()
    choice = int(input("1) Record attendance \n2) Generate statistics \n3) Exit \n" ))
    if choice>0:
        if choice == 1:
            mod_sel(1)
        elif choice == 2:
            mod_sel(2)
        elif choice == 3:
            raise SystemExit(0)
        else:
            print("Choice should be between one and 3")
    else:
        print("positive numbers only")


def mod_sel(cho): # cho recieves the value from the first menu i.e. record attendance or generate statistics
    print()
    print("Module selection")
    print("="*40)
    y = open("modules.txt", "r")
    menu = y.read()
    ch = int(input(menu+"\n"))
    if ch == 1 and cho == 1: # ch recieves the value from the second menu, i.e. the users module selection
        prompt = "SOFT_6017.txt"
        rec_att(prompt)
    elif ch == 2 and cho==1:
        prompt = "SOFT_6018.txt"
        rec_att(prompt)
    elif ch == 1 and cho == 2:
        prompt = "SOFT_6017.txt"
        stats(prompt)
    elif ch == 2 and cho == 2:
        prompt = "SOFT_6018.txt"
        stats(prompt)

    else:
        print("invalid choice")


def rec_att(mod_name):
    n = []
    present = []
    absent = []
    excused = []
    z = open(f"{mod_name}", "r")
    zz = z.read().replace("\n",",")  # Adding a comma at the end of every line so that each student(line) can have their own array
    zz = zz.split(",")
    for j in range(0, len(zz) - 1, 4):  # iterates from 0 to 4 to 8 and so on....
        n.append(zz[j])  # 0th 4th 8th.... element added to the names array
        pr = zz[j + 1]
        present.append(pr)
        ab = zz[j + 2]
        absent.append(ab)
        ex = zz[j + 3]
        excused.append(ex)  # seperating the numbers and adding them to individual arrays
    z.close()
    va2 = open(f"{mod_name}", "w")

    for d in range(0, len(n), 1):
        print(f"Student number {d + 1} \n{n[d]} ")
        ch1 = int(input(f"1) present \n2) absent \n3) excused\n"))
        if (ch1 == 1):
            present[d] = int(present[d]) + 1
            va2.write(f"{n[d]},{present[d]},{absent[d]},{excused[d]} \n")

        elif (ch1 == 2):
            absent[d] = (int(absent[d]) + 1)
            va2.write(f"{n[d]},{present[d]},{absent[d]},{excused[d]} \n")
        elif (ch1 == 3):
            excused[d] = (int(excused[d]) + 1)
            va2.write(f"{n[d]},{present[d]},{absent[d]},{excused[d]} \n")
        else:
            print("invalid")
            break
    print()
    print(f"File {mod_name} has been updated.")



def stats(module_selection):
    n = []
    present = []
    absent = []
    excused = []
    low_attenders = []
    no_attenders = []
    max_attenders = []
    z = open(f"{module_selection}", "r")
    zz = z.read().replace("\n",",")  # Adding a comma at the end of every line so that each student(line) can have their own array
    zz = zz.split(",")
    for j in range(0, len(zz) - 1, 4):  # iterates from 0 to 4 to 8 and so on....
        n.append(zz[j])  # 0th 4th 8th.... element added to the names array
        pr = int(zz[j + 1])
        present.append(pr)
        ab = int(zz[j + 2])
        absent.append(ab)
        ex = int(zz[j + 3])
        excused.append(ex)  # seperating the numbers and adding them to individual arrays
    z.close()
    mod_name = module_selection.replace(".txt","")
    print(f"Module: {mod_name}" )
    class_total = present[0]+absent[0]+excused[0]
    print(f"Number of classes: {class_total}")
    avg = int(sum(present)/len(present))
    print(f"Average attendance: {avg}")
    thresh = int(class_total*70/100)
    maxat = max(present)
    max_attenders.append(n[present.index(maxat)])
    max_days = present[present.index(maxat)]
    for i in range(0, len(present), 1):
        if  present[i]<thresh:
            low = n[i]
            low_attenders.append(low)
        if present[i] == 0:
            no = n[i]
            no_attenders.append(no)
        if present[i] == maxat:
            eq = n[i]
            if eq not in max_attenders:
                max_attenders.append(eq)




    print(f"low attender(s): {','.join (low_attenders) }")
    print(f"non_attender(s):{','.join(no_attenders)}")
    print(f"best attender(s): {','.join(max_attenders)} \nattended {max_days} out of {class_total} days ")
    now = datetime.datetime.now()
    year = now.strftime("%Y") # finding out the date and converting it to string for the new files name
    month = now.strftime("%m")
    day = now.strftime("%d")


    newf = open(mod_name+'_'+day+month+year+'.txt',"w") #writing into the file
    newf.write(f"Module: {mod_name} \n")
    newf.write(f"Number of classes: {class_total}\n")
    newf.write(f"Average attendance: {avg}\n")
    newf.write(f"low attender(s): {','.join(low_attenders)}\n")
    newf.write(f"non_attender(s):{','.join(no_attenders)}\n")
    newf.write(f"best attender(s): {','.join(max_attenders)} \nattended {max_days} out of {class_total} days ")


def main():
    name, login_status = login()
    if login_status == 's':
        next(name)
    else:
        print("Incorrect username or password")

main()





