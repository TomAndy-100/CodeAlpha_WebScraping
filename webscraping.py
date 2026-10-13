#import both modules for webscraping (beautifulsoup and requests)
import requests
from bs4 import BeautifulSoup
import pandas as pd

# since we are working with data that we have not yet gotten, we create a container list with variable called data
data = [ ]

#create a variable called 'url' which will acquire the website locally
url = 'https://scrapingsandbox.com/'  

#create another variable called response to show us the response status of the website in focus
response = requests.get(url)

#print the response status
print(response.status_code)

#create another variable called 'soup' which is gonna contain all the html structural info of the website then we start scraping from there 
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title.text)


products = soup.find_all('a', class_='product-card group block rounded-xl border border-border bg-card p-3 card-hover')
#loop through the info variable to extract the product name, price and rating of each product on the website
for product in products:
    item = product.find('h3', class_='product-name text-sm font-semibold text-card-foreground line-clamp-2 leading-snug group-hover:text-primary transition-colors')  
    rating = product.find('span', class_='rating text-[11px] font-mono text-muted-foreground')
    price = product.find('span', class_='price text-base font-bold font-mono text-primary').text
    #then print the product name, price and rating of each product on the website
    print(item.text,';', price,'_', rating.text.strip())
    #with this info, you can now fill in the data in a dictionary format and append it to the data list
    data.append({'product' : item.text.strip(), 'price': price.strip(), 'rating': rating.text})
print(data) 

df = pd.DataFrame(data)
print(df)

# df.to_excel('Scraped products.xls' , index=False)


    
   