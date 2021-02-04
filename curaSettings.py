import csv
from os import name, write
import datetime

today = datetime.datetime.now()
print('Todays date:', today.strftime('%x'))

print('Ultimaker Cura Printer Settings. Input settings below!')

def settings_name():
    print('\nType your name')
    setName = input('Name: ')

    print(f'\nThanks {setName}! Lets get started\n')

    nameDict = {}
    while True: 
        save = input('Do you want to save your name? Y or N? ')
        if save.lower() == 'y':
            nameDict['name'] = setName
            print('Name saved!\n\n')
            break
        elif save.lower() == 'n':
            print('Okay, lets continue\n\n')
            break
        else: 
            print('Please type y or n. Goodbye')
            exit()
settings_name()

print('-------Ultimaker Cura Printer Settings-------')
printTemp = input('Printing Tempterature: ')
buildPlateTmp = input('Build Plate Temperature: ')
flow = input('Flow (%): ')
printSpeed = input('Print Speed(mm/s): ')
enableRetraction = input('Enable Retraction: ')
retractLayerChange = input('Retraction at Layer Change: ')
retractDistance = input('Retraction Distance (mm): ')
retractSpeed = input('Retraction Speed (mm/s): ')
retractExtraPrimeAmt = input('Retraction Extra Prime Amount: ')
combingMode = input('Combing Mode: ')

'''writes data to .csv file'''
with open('curaSettings.csv', 'w+') as file:
    myData = csv.writer(file)
    myData.writerow([
        'Printing Temperature',
        'Build Plate Temperature',
        'Flow (%)',
        'Printing Speed (mm/s)',
        'Enable Retraction',
        'Retraction at Layer Change',
        'Retraction Distance',
        'Retraction Speed (mm/s)',
        'Retraction Extra Prime Amount (mm)',
        'Combing Mode'
    ])
    myData.writerow([
        printTemp,
        buildPlateTmp,
        flow,
        printSpeed,
        enableRetraction,
        retractLayerChange,
        retractDistance,
        retractSpeed,
        retractExtraPrimeAmt,
        combingMode
    ])
    print('\nDownloading .csv file. Enjoy!')

appendSettings = [
    'Printing Temperature',
    'Build Plate Temperature',
    'Flow (%)',
    'Printing Speed (mm/s)',
    'Enable Retraction',
    'Retraction at Layer Change',
    'Retraction Distance',
    'Retraction Speed (mm/s)',
    'Retraction Extra Prime Amount (mm)',
    'Combing Mode'
]
