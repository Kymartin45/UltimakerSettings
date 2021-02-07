import csv
import os
from os import name, read, write
import datetime as dt
from datetime import date
from typing import Counter

today = date.today()
print('Todays date:', today.strftime('%x'))

print('Ultimaker Cura Printer Settings. Input settings below!')

print('-------Ultimaker Cura Printer Settings-------\n')
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

counter = 0 
fileName = 'settings_{}'
while os.path.isfile(fileName.format(counter)):
    counter += 1
fileName = fileName.format(counter)

if os.path.exists(fileName):
    append_newFile = 'a' #append if exists
else:
    append_newFile = 'w' #make new file

'''writes data to .csv file'''
with open('{}.csv'.format(fileName), 'w') as file:
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

    print('\nDownloading {}. Enjoy!'.format(fileName))