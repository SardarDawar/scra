import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

def search_amazon(product_name):
    # Set up the webdriver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    # Navigate to Amazon
    driver.get("https://www.amazon.com/")

    # Find the search box element and enter the product name
    search_box = driver.find_element_by_id("twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(5)

    # Your additional code to work with search results

    # Close the browser
    driver.close()

    # Return a message for now, replace this with your search result handling code
    return "Search completed for " + product_name

# Streamlit app
st.title("Amazon Product Search")
product_name = st.text_input("Enter a product name to search on Amazon:", "")

if st.button("Search"):
    result = search_amazon(product_name)
    st.write(result)
