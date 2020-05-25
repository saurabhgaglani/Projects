#Saurabh Gaglani
#COMP 1C-X
try:
    choice=int(input("1. Add a new hero \n 2. View details of hero \n 3. Quit \n ==> "))
except ValueError:
    print("invalid input, please enter integers only")
if (choice>3):#loop terminates when user enters 3
    print("invalid, choice should be less than or equal to 3")
else:
    pass
c=0 #counter for all heroes
cm=0
cd=0
longest_hero="" #defining variable to compare lengths, this variable will store the longest name
shortest_hero="" #defining variable to compare lengths, this variable will store the shortest name
all_heroes = open("marvel.txt", "w+") #file with just the names of marvel superheroes
all_heroes.write("=" * 80)
all_heroes.write("\n")
dc_heroes = open("dc.txt", "w+") #file with just the names of dc superheroes
dc_heroes.write("=" * 80)
dc_heroes.write("\n")
mar = open("marvell.txt", "w+") #file with names and powers
mar.write("Name \t\t\t\t AKA \t\t\t\t Power ")
mar.write("\n")
mar.write("=" * 80)
dc= open("dcc.txt", "w+")
dc.write("Name \t\t\t\t aka \t\t\t\t Power \n")
dc.write("=" * 80)

max_len_name = 20
while choice!=3:
    if mar.closed== True: #if user wants to enter values after looking at their descriptions, this opens up the file for them
        mar=open("marvell.txt", "a")
    elif all_heroes.closed==True:
        all_heroes=open("marvel.txt", "a")
    else:
        pass
    if dc.closed== True:
        dc=open("dcc.txt", "a")
    elif dc_heroes.closed==True:
        dc_heroes=open("dc.txt", "a")
    else:
        pass


    if choice==1:
        hero= input("What is your hero name? \n ==> ")
        c += 1
        if(len(longest_hero)<len(hero)): #finding longest name
            longest_hero=hero
        elif(len(longest_hero)==len(hero)):
            longest_hero+= longest_hero+" and "+hero
        else:
            pass

        if (len(shortest_hero) > len(hero)) or not shortest_hero: #or not shortest hero is used so that "" can be replaced in shortest_hero
            shortest_hero = hero
        elif (len(shortest_hero)==len(hero)):
            shortest_hero = shortest_hero + " and "+ hero
        else:
            pass


        hero = hero + ' ' * (max_len_name - len(hero)) #longer the name, lesser the number of spaces in the file or vice versa
        aka= input("Also known as? \n ==> ")
        aka = aka + ' ' * (max_len_name - len(aka))
        pow= input("Describe your power- \n ==>")
        pow = pow + ' ' * (max_len_name - len(pow))
        choice_planet= int(input("Are you- \n 1.From earth? \n 2. Not from earth? \n ==>"))
        try:
            if choice_planet==1:
                planet="from earth"
            elif choice_planet==2:
                planet="Not from earth"
            else:
                print("invalid choice, please try again") #if choice is not 1 or 2
                continue
            choice_world= int(input("Are you- \n 1.Marvel? \n 2. DC \n ==> " ))
            if choice_world==1:
                world="marvel"
            elif choice_world==2:
                world="DC"
            else:
                print("invalid choice please try again")
                continue
            s= hero.rstrip()
            s= s.replace(" ", "_") #creating file in snake format
            name= open(f"{s}.txt", "w+")
            name.write(f"Name- {hero} \n")
            name.write(f"Also know as- {aka} \n")
            name.write(f"Planet- {planet} \n")
            name.write(f"World- {world} \n")
            name.write(f"Power- {pow} \n")
            name=""
            if choice_world==1:
                cm+=1
                mar.write("\n")
                mar.write(f"{hero} \t\t {aka} \t\t {pow}")
                all_heroes.write(f">>\t {hero}\n")
            else:
                cd+=1
                dc.write("\n")
                dc.write(f"{hero} \t\t {aka} \t\t {pow}")
                dc_heroes.write(f">>\t {hero}\n")
        except:
            print("invalid input, please enter an integer")
    try:
        choice = int(input("1. Add a new hero \n 2. View details of hero \n 3. Quit \n ==> "))
    except ValueError:
        print("invalid input, please enter integers only")
        continue
    if choice==2:
        mar.close() #closing files to read them
        all_heroes.close()
        dc_heroes.close()
        read_choice= int(input("1. Marvel \n 2. DC"))
        if read_choice==1:
            read_marvel = open("marvel.txt", "r")
            contents=read_marvel.read()
            print("Please choose from the following heroes: \n" )
            print(contents)
            chosen_hero= input("which hero?")
            if(chosen_hero in contents):
                chosen_hero = chosen_hero.replace(" ", "_")
                read_now= open(f"{chosen_hero }.txt")
                now= read_now.read()
                print(now)
            else:
                print("not found")

        else:

            read_dc = open("dc.txt", "r")
            contentss=read_dc.read()
            print("Please choose from the following heroes: \n" )
            print(contentss)
            chosen_hero_dc= input("which hero?")
            if(chosen_hero_dc in contentss):
                chosen_hero_dc = chosen_hero_dc.replace(" ", "_")
                read_now_dc= open(f"{chosen_hero_dc}.txt")
                now= read_now_dc.read()
                print(now)
            else:
                print(f"{chosen_hero_dc} not found, please check and input again.")










print("Number of superheroes=", c)
print("Marvel Superheroes- ", cm)
print("DC Superheroes- ", cd)
print("longest name= "+ longest_hero)
print("shortest name= "+ shortest_hero)
print(f"Percentage of superheroes from Marvel= {(cm/c)*100: .2f}%")
print(f"Percentage of superheroes from DC= {(cd/c)*100: .2f}%")
print(f"Thank you \U0001f600")

