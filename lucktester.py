import random

def main():
    print("Welcome to the Vesteria Luck Tester!")
    print("You might even get your first green tier weapon!")
    wpn = []
    wpnp = 0
    ctr_c = 0
    ctr_h = 0

    while True:
        print("")
        print("Your current weapon status:")
        print("Weapon: ", " ".join(wpn))
        print("Weapon Points: ", wpnp, tier(wpnp))
        print("Cursed Scrolls used: ", ctr_c)
        print("Holy Scrolls used: ", ctr_h)
        print("")
        print("1: Cursed ATK Scroll")
        print("2: Holy Scroll")
        print("3: Reset Scroll")
        print("4: Exit")
        inp = input("Select your choice (1-4): ")

        if inp == "1":

            if len(wpn) == 7:
                print("You cannot use the scroll anymore. Your weapon is already maxed out.")
                continue

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
            
            ctr_c += 1

        elif inp == "2":
            if "FAIL" in wpn:
                wpn.remove("FAIL")
                ctr_h += 1
            else:
                print("You cannot use the Holy Scroll. No failed attempts found.")
                
        elif inp == "3":
            print("Your weapon has been reset to its original state.")
            wpn.clear()
            wpnp = 0
        
        elif inp == "4":
            print("Exiting the Luck Tester. Goodbye!")
            break
            
        else:
            print("Invalid input. Please select a valid option (1-4).")

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
    
if __name__ == "__main__":
    main()