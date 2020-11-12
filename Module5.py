"""
Bridget D. Harrell
Agile UNO Module 5
Strings and Lists
"""

from sys import exit       #from the system, import function exit; if condition is met,exit out of loop

import requests            #send HTTP requests
import time

site_data = {}   #variable for file name 

with open("sites.csv", "r") as infile:   #open sites file; infile is open file to read from
    data = infile.read()   #reading data from file in a variable called data
    sites = data.split(",")  #split string into a list

print(len(sites))


for site in sites:   #for each site
    site_data[site] = requests.get(site) #get info from a specific server
    print(site_data[site])

for key, value in site_data.items(): #using site_data items, get the key and value
    print(site_data[site])
    print(f"\n{key}:{value}")  #response code


#1 Using string slicing, print out each URL extension below
for site in sites:
    print(site[-3:])




#2 Print out any sites that end with .com below
for site in sites:
    if ".com" in site:
        print(site)
      


#3 Convert all sites to upper case and print each below
for site in sites:
    print(site.upper())


#4 Using a list of sites, add a new site to it, using the input() method to get the name of the site from the user
#then reverse the order of the list
#print it out
print(f"sites are {sites}")


new_site = input("enter site\n")
sites.append(new_site)
sites.reverse()
print(sites)


#5 print out the 'server' of the response of the URL request of the items from your list


for site in sites:
    print(requests.get(site).headers["server"])


#6 Exit the program using the sys module's exit function we imported at the beginn ing of the code
exit()




    
