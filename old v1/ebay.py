import requests
import csv
import tkinter
from bs4 import BeautifulSoup
import timeit

"""
@author Daniel Kwan
@date 12-31-2019

"""


start = timeit.default_timer()


images=[]
list1=[] #list for links
pageList=[]
priceList=[] #list for prices
nameList=[] #list for names

string1 = 'https://www.ebay.ca/sch/i.html?_nkw='
userinput = input("What product would you want to explore? : ")
finalurl = string1 + userinput
print("Searching on ebay for "+ userinput +"....")



result = requests.get(finalurl) #attempts to grab the website data
if result.status_code == 200: #check if works
    print("SUCCESSFUL ACCESS")
else:
    print("UNSUCESSFUL ACCESS")

src = result.text
soup = BeautifulSoup(src,'html.parser')


#loops through to check all of h3 tags
for h3_tag in soup.find_all("h3"):
    a_tag = h3_tag.find('a')

    if a_tag is not None and 'href' in a_tag.attrs:
        list1.append(a_tag.get('href'))

#new


#these are the links for all the pages
testpages = soup.find("td", _sp="p2045573.m1686.l1513")
linksofpages = testpages.find_all("a")

for numLink in linksofpages:
    pageList.append(numLink.attrs['href'])


for z in pageList:
    url=z
    result = requests.get(z)  # attempts to grab the website data


    src3 = result.text
    soup = BeautifulSoup(src3, 'html.parser')


    # loops through to check all of h3 tags
    for h3_tag2 in soup.find_all("h3"):
        a_tag2 = h3_tag2.find('a')

        if a_tag2 is not None and 'href' in a_tag2.attrs:
            list1.append(a_tag2.get('href'))






#redo the src for every link to get the price and name and appends the data into a list
for link in list1:
    result2=requests.get(link)
    src2 = result2.text
    soup2 = BeautifulSoup(src2,'html.parser')
    checkPrice = soup2.find("span", itemprop="price")
    print(checkPrice)

    checkName = soup2.find("span", id="vi-lkhdr-itmTitl")
    checkNamerepeat = str(checkName)


    if checkPrice is not None and 'content' in checkPrice.attrs:

        priceList.append(float(checkPrice.attrs['content']))
    else:
        priceList.append(10000000)

        print(link)

    string1=''
    for i in range(43, len(checkNamerepeat)):
        if checkNamerepeat[i] == "<":
            break
        else:
            string1 = string1 + checkNamerepeat[i]

    nameList.append(string1)



#shows all the images
for linkagain in list1:

    url2 = linkagain
    result3 = requests.get(url2) #attempts to grab the website data
    src3=result3.text
    soup3 = BeautifulSoup(src3,'html.parser')
    imagepage= soup3.find('img',itemprop="image")
    if imagepage is not None and 'src' in imagepage.attrs:



        imagelink = imagepage.attrs['src']
        images.append(imagelink)
    else:
        images.append('ebay.com')


newList=[]
for i in range(len(nameList)):
    newList.append(nameList[i])
    newList.append((priceList[i]))
    newList.append(images[i])
    newList.append(list1[i])



#checks for the lowest price
level=9000
name =''
lowest=min(priceList)
indexoflow = priceList.index(lowest)
name=nameList[indexoflow]
itemlink = list1[indexoflow]

print("The cheapest option is : "+ name +" with a US price of - $"+ str(lowest))
print("The link for the item is "+itemlink)




with open('testing.txt', 'w') as f:
    for item in newList:
        f.write("%s\n" % item)
f.close()




stop = timeit.default_timer()

print('Time: ', stop - start)


#add sorting alg
