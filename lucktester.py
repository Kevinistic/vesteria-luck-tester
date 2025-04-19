import random

def main():
    print("Welcome to the Vesteria Luck Tester!")
    print("You might even get your first green tier weapon!")
    global wpn, wpnp, wpnu, ctr_c, ctr_a, ctr_h, ctr_r, money, scrollsel

    wpn = []
    wpnp = 0
    wpnu = 0
    ctr_c = 0
    ctr_a = 0
    ctr_h = 0
    ctr_r = 0
    money = 0
    scrollsel = "Cursed"

    MenuMain()

def tier(p):
    if p < 1:
        return "Grey"
    elif p <= 10:
        return "Blue"
    elif p <= 20:
        return "Deep Blue"
    elif p <= 40:
        return "Purple"
    elif p <= 60:
        return "Red"
    elif p <= 80:
        return "Orange"
    elif p <= 95:
        return "Gold"
    elif p <= 110:
        return "Aquamarine"
    else:
        return "Green"

def MenuMain():    
    global wpn, wpnp, wpnu, ctr_c, ctr_a, ctr_h, ctr_r, money, scrollsel
    while True:
        print("")
        print("Your current weapon status:")
        print("Weapon: ", " ".join(wpn))
        print("Weapon Points: ", wpnp, tier(wpnp))
        print("Money: ", money, " golds")
        print("Weapons thrown away/exploded: ", wpnu)
        print("")
        print("Selected scroll: ", scrollsel)
        print("1: Apply Scroll")
        print("2: Select Scroll")
        print("3: View Stats")
        print("4: Sell Weapon")
        print("5: Reset Session")
        print("6: Exit")
        inp = input("Select your choice (1-6): ")

        if inp == "1":
            if scrollsel == "Cursed":
                ScrollCursed()
            elif scrollsel == "Ancient":
                ScrollAncient()
            elif scrollsel == "Holy":
                if "FAIL" in wpn:
                    wpn.remove("FAIL")
                    ctr_h += 1
                else:
                    print("You cannot use the Holy Scroll. No failed attempts found.")
            elif scrollsel == "Reset":
                print("Your weapon has been reset to its original state.")
                wpn.clear()
                wpnp = 0

        elif inp == "2":
            MenuSelect()

        elif inp == "3":
            MenuStats()

        elif inp == "4":
            if len(wpn) == 0:
                print("You have no weapons to sell.")
            else:
                try:
                    val = int(input("How much do you want to sell your weapons for (golds): "))
                    if val < 0:
                        print("Invalid input. Please enter a positive number.")
                        return
                    elif val == 0:
                        print("Weapon successfully thrown away.")
                        wpnu += 1
                        continue

                    money += val
                    wpn.clear()
                    wpnp = 0
                    
                    print("You sold your weapons for ", money, " golds.")

                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif inp == "5":
            print("Resetting session...")
            wpn.clear()
            wpnp = 0
            wpnu = 0
            ctr_c = 0
            ctr_a = 0
            ctr_h = 0
            ctr_r = 0
            money = 0
            scrollsel = ""
            print("Session reset successfully.")

        elif inp == "6":
            print("Exiting the Luck Tester. Goodbye!")
            break
            
        else:
            print("Invalid input. Please select a valid option (1-6).")

def MenuStats():
    print("Cursed Scrolls used: ", ctr_c)
    print("Ancient Scrolls used: ", ctr_a)
    print("Holy Scrolls used: ", ctr_h)
    print("Reset Scrolls used: ", ctr_r)

def MenuSelect():
    global scrollsel
    print("1: Cursed Scroll")
    print("2: Ancient Scroll")
    print("3: Holy Scroll")
    print("4: Reset Scroll")

    inp = input("Select your scroll (1-4): ")
    if inp == "1":
        scrollsel = "Cursed"
        print("Cursed Scroll selected.")
    elif inp == "2":
        scrollsel = "Ancient"
        print("Ancient Scroll selected.")
    elif inp == "3":
        scrollsel = "Holy"
        print("Holy Scroll selected.")
    elif inp == "4":
        scrollsel = "Reset"
        print("Reset Scroll selected.")
    else:
        print("Invalid input. Please select a valid scroll (1-4).")
        return
    
def ScrollCursed():
    global wpn, wpnp, wpnu, ctr_c
    if len(wpn) == 7:
        print("You cannot use the scroll anymore. Your weapon is already maxed out.")
        return

    print("Rolling...")
    result = random.randint(1, 100)
    if result <= 60:
        result2 = random.randint(1, 1000)
        if result2 <= 45:
            print("GREEN!")
            wpn.append("GREEN")
            wpnp += 14
        elif result2 <= 45+91:
            print("AQUAMARINE!")
            wpn.append("AQUAMARINE")
            wpnp += 12
        elif result2 <= 45+91+136:  
            print("GOLD!")
            wpn.append("GOLD")
            wpnp += 10
        elif result2 <= 45+91+136+172:
            print("ORANGE!")
            wpn.append("ORANGE")
            wpnp += 8
        elif result2 <= 45+91+136+172+227:
            print("RED!")
            wpn.append("RED")
            wpnp += 6
        else:
            print("PURPLE!")
            wpn.append("PURPLE")
            wpnp += 4

    elif result <= 80:
        print("POOF! The magic scroll vanishes into thin air.")
        wpn.append("FAIL")
    else:
        print("BOOM! The magic scroll's curse destroys your equipment.")
        wpn.clear()
        wpnp = 0
        wpnu += 1
    
    ctr_c += 1

def ScrollAncient():
    global wpn, wpnp, ctr_a
    if len(wpn) == 7:
        print("You cannot use the scroll anymore. Your weapon is already maxed out.")
        return

    print("Rolling...")
    result = random.randint(1, 100)
    if result <= 20:
        print("ANCIENT!")
        wpn.append("ANCIENT")
        wpnp += 10
    else:
        print("POOF! The magic scroll vanishes into thin air.")
        wpn.append("FAIL")
    
    ctr_a += 1
    
if __name__ == "__main__":
    main()