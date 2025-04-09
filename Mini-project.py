import requests
from bs4 import BeautifulSoup


def PE_ratio(url):
    fakeheader = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=fakeheader)

    if response.status_code != 200:
        print("Failed to fetch data.")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    
    list_elements = soup.find_all('li', class_='flex flex-space-between')

    for block in list_elements:
        name = block.find('span', class_='name')
        value = block.find('span', class_='number')
        if name and 'P/E' in name.text:
            ratio = value.text.strip()
            return ratio

    print("Could not find P/E Ratio on the page.")


def conditions():
    a = 0
    a1 = input()
    if a1 == 'yes':
        a = a+1
    a2 = input("2) Is net profit increasing ? \n")
    if a2 == 'yes':
        a = a+1
    a3 = input("3) Is the FII DII holding percentage stable or increasing ? \n")
    if a3 == 'yes':
        a = a+1

    b = 0
    b1 = input("4) Is the cash flow positive ? \n")
    if b1 == 'yes':
        b = b+1
    b2 = input("5) Check Debt to Equity ratio less than 2 \n")
    if b2 == 'yes':
        b = b+1
    b3 = input("6) Check the intrinsic value nearby it's stock price  \n")
    if b3 == 'yes':
        b = b+1

    c = 0
    c1 = input("7) Sector wise and marketcap wise, is the stock standing in top 3 ? \n")
    if c1 == 'yes':
        c = c+1
    c2 = input("8) Read pros and cons if pros maximun then type 'yes' else 'no' \n")

    if c2 == 'yes':
        c = c+1
   
    if (a == 3 and b >= 2 and c >= 1):
        print("You can add this stock in your bascket")
    else:
        print("This stock is not fundamentally strong check another one")    

print("===STOCKS ANALYSING TOOL===\n")
print("Check your fav stocks Fundamentally with zero knowlwgde\nand make your own portfolio bascket")

read = input("~~~~~~STEPS~~~~~~\n 1)Open any browser\n 2)Search 'Screener.com' and open the website\n 3)Search your fav stocks and copy the URL and paste here\n 4)Check given all conditions step by step with the help of website\n 5)If you read all then type 'start'\n")
if (read == 'start'):
    n = int(input("How many stocks u want in your portfolio\n"))
    url = input("Paste Screener.in stock URL: ").strip()
    if "https://www.screener.in/company/" in url:
        a1 = PE_ratio(url)
        print("P/E Ratio : ",a1)
        i = 1
        while i <= n :
                print("=== STOCK NO.",i,"===")
                print("Type answers only in 'yes' or 'no'")
                conditions()
                i += 1
       
    else :
        print("Invalid Screener URL. please paste it correct")

  
else :
    print("Read again")