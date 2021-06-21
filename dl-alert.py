import urllib.request
import re
import time
from bs4 import BeautifulSoup
from datetime import datetime
import os
import sys


loc_dict = {#'Bakers Basin ': '186',
			 'Bayonne ': '187',
			 #'Camden ': '189',
			 #'Cardiff ': '208',
			# 'Delanco ': '191',
			# 'Eatontown ': '192',
			 'Edison ': '194',
			# 'Flemington ': '195',
			# 'Freehold ': '197',
			 'Lodi ': '198',
			 'Newark ': '200',
			 'North Bergen ': '201',
			 'Oakland ': '203',
			 'Paterson ': '204',
			 'Rahway ': '206',
			# 'Randolph ': '207',
			 #'Rio Grande ': '188',
			# 'Salem ': '190',
			 'South Plainfield ': '193',
			# 'Toms River ': '196',
			# 'Vineland ': '199',
			# 'Wayne ': '202',
			# 'West Deptford ': '205'
			}
# location_arr = ['101','102','103','104','105','106','107','108','109','110','111','112','113','114','115','116','117','118','119','120','121','122','123']
# locationname_arr = ['Lawrenceville','Bayonne','North Cape May','Camden','Cardiff','Salem','Delanco','Eatontown','SouthPlainfield','Edison','Flemington','Toms River','Freehold','Lodi','Vineland','Newark','North Bergen','Wayne','Oakland','Paterson','Thorofare','Rahway','Randolph']
base_url_link='https://telegov.njportal.com/njmvc/AppointmentWizard/15/'
required_months = ['June','July']

def beep():
    os.system( "say beep" )



def job():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print("\n\n\nDate Time: ", dt_string, "\n\n")
    i=0
    found=0
    
    
    for key,val in loc_dict.items():
        with urllib.request.urlopen(base_url_link+val) as response:
            page_html = response.read()
        soup = BeautifulSoup(page_html ,'lxml')
        unavailable=soup.find('div',attrs={'class': 'alert-danger'})
        if unavailable is not None :
            #print('No appointments are available in '+locationname_arr[i])
            dt_string=""
        else:
            dates_html = soup.find('div',attrs={'class': 'col-md-8'})
            date_string = dates_html.find('label',attrs={'class': 'control-label'})
            if set(required_months) & set(date_string.text.split()):
                #print("Matching required months")
                date_string=re.sub('Time of Appointment for ', '', date_string.text)
                date_string=re.sub(':', '', date_string)
                message = 'Initial Permit Dates: '+key+' / ('+ val +') : '+date_string
                print(message)
                beep()
                found=1
        
while True :
    try:
        job()
    except Exception as e:
        print(e)
        time.sleep(60)
    else:
        time.sleep(60)
    
