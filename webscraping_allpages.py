#import both modules for webscraping (beautifulsoup and requests) and the selenium for pagination handling  
from operator import ne

import requests
from bs4 import BeautifulSoup
import pandas as pd


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 

# since we are working with data that we have not yet gotten, we create a container list with variable called data
data = [ ]

#create a variable called 'url' which will acquire the website locally
url = 'https://scrapingsandbox.com/'  

#create another variable called response to show us the response status of the website in focus
  # Make sure you have the ChromeDriver installed and in your PATH
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)  # allows the webscraper to Wait for up to 10 seconds for elements to load

#handle pagination by using a for loop to iterate through the pages of the website
for page in range(1, 22):
    soup = BeautifulSoup(driver.page_source, 'html.parser')  
    products = soup.find_all('a', class_='product-card group block rounded-xl border border-border bg-card p-3 card-hover')
    print(f'scrapingpage {page}')
    for product in products:
        item = product.find('h3', class_='product-name text-sm font-semibold text-card-foreground line-clamp-2 leading-snug group-hover:text-primary transition-colors') 
        rating = product.find('span', class_='rating text-[11px] font-mono text-muted-foreground')
        price = product.find('span', class_='price text-base font-bold font-mono text-primary').text
    #then print the product name, price and rating of each product on the website
        print(item.text,';', price,'_', rating.text.strip())
    #with this info, you can now fill in the data in a dictionary format and append it to the data list
        data.append({'product' : item.text.strip(), 'price': price.strip(), 'rating': rating.text})
    print(data) 
    # moving to the next page
    if page < 21:
        next_page = wait.until(
            lambda d: d.find_element(
                By.XPATH,
                f"//button[normalize-space()='{page + 1}']"
            )
        )
        next_page.click()
driver.quit()


df = pd.DataFrame(data)
print(df)

df.to_excel('All scraped products.xlsx' , index=False)


    
   