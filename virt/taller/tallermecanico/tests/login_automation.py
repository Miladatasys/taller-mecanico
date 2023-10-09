from selenium import webdriver

# Set the path to the downloaded Microsoft Edge WebDriver
webdriver_path = 'C:\Users\cmora\OneDrive\Documentos\GitHub\automatizacion\virt\taller\edgedriver_win64\msedgedriver.exe'

# Create a new instance of the Microsoft Edge driver
driver = webdriver.Edge(executable_path=webdriver_path)

# Navigate to the login page
driver.get('http://127.0.0.1:8000/login/')

# Find the username and password input fields and enter the credentials
username_input = driver.find_element_by_id('username')
password_input = driver.find_element_by_id('password')
username_input.send_keys('camila')
password_input.send_keys('holamundo')

# Find the login button and click it
login_button = driver.find_element_by_id('login-button')
login_button.click()

# Wait for the page to load or perform any necessary assertions
# ...

# Close the browser
driver.quit()