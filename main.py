from Core import Main_Core as core
from termcolor import cprint

cprint('===== Welcome to Roblox Tycoon Killer =====', 'light_red')
print('Get updates in: https://github.com/system3600/RTK ')

def main():
    op = int(input(
        'please select an option : \n1)autoclick \n2)auto-egg \n3)anti-afk \n4)about \n5)beta features \n6)exit \n> '))
    if op == 1:
        t = input('tell time between clicks: ')
        core.auto_click(t)
    elif op == 2:
        core.auto_egg()
    elif op == 3:
        core.anti_afk()
    elif op == 4:
        cprint("Made By: exnop (discord)", 'light_magenta')
        print('Current version : 1.0')
        print('launch date: 05/08/2023')
        core.wait(2)
        main()
    elif op == 5:
        cprint('EXPERIMENTAL FEATURES', "light_red")
        warning = int(input(
            'all features on this tab are in the testing phase and may occasionally fail, are you sure you want to '
            'continue? \n1)yes \n2)no \n> '))

        if warning == 1:
            cnt = int(input('select the feature : \n1)GUI \n2)Locator \n3) back to the menu \n> '))
            if cnt == 1:
                core.interface()
            if cnt == 2:
                cprint('advanced automation using screen element recognition (BETA)', 'light_green')
                tar = input('put the full path to the image you want to locate on the screen: ')
                time = input('tell how often the program should click on the target: ')
                core.locator(tar, time)
            if cnt == 3:
                main()
        if warning == 2:
            main()
    elif op == 6:
        print('Exiting...')


main()
