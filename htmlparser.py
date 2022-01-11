from bs4 import BeautifulSoup

html_report_part1 = open("Homegate_3001611096.html", 'r')
soup = BeautifulSoup(html_report_part1,'html.parser')
headlines = soup.find('title')

#print(soup.text)

div = {"class":"ContactForm_sellerLeadsCheckbox_2EqJD"}
div2 = {"class":"Description_descriptionBody_2wGwE"}
div_anbieter = {"class":"ListingDetails_column_2asKt"}
script_info = {"type":"application/ld+json"}
script_info_immobile = {"class":"CoreAttributes_coreAttributes_2UrTf"}
picture = {"img":"CoreAttributes_coreAttributes_2UrTf"}

print("Title  von HTML")
print(soup.title.string)
print("\n")


#print("Gemeinde-Ratgeber")
#print(soup.p)
#print("\n")

print("Telefonnummer in HTML")
for link in soup.find_all('a'):
    try:
        if "tel:" in link.get("href"):
            print(link.get('href'))
        else:
            continue
    except:
        print("Error")
print("\n")

print("Bilder")
print(soup.find('img',attrs=div2))
print("\n")




print("Beschreibung")
print(soup.find('div',attrs=div2))
print("\n")


print("Anbieter")
print(soup.find('div',attrs=div_anbieter))
print("\n")

print("Infos")
print(soup.find('script',attrs=script_info))
print("\n")

print("Infos über immobilie")
print(soup.find('div',attrs=script_info_immobile))
print("\n")

print("ALL Links")
soup.find_all('a')

for link in soup.find_all('a'):
    print(link.get('href'))
print("\n")








