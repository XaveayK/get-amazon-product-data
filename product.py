import openpyxl
from selenium import webdriver
class product:
    
    def __init__(self, title, URI, excelSheet, keys=None):
        self.title = title
        self.sheet = excelSheet
        self.URI = URI
        self.col = self.sheet.max_column+1
        print(keys)
        if keys == None or title not in keys[0]:
            self.sheet.cell(2, self.col).value = self.title
            self.sheet.cell(3, self.col).value = self.URI

    # Purpose: Sets URI in case it must be updated\
    # Params:  URI - The uri of the of the item
    def setURI(self, URI):
        self.URI = URI
        self.sheet.cell(3, self.col).value = URI
    
    # Purpose: To input a price directyl
    # Usage:   Used when recreating already existing entries from excel
    def setPrice(self, price):
        self.price = price

    # Gets the price in the excel sheet
    def currPrice(self):
        return self.price

    async def getPriceFromPage(self, driver=webdriver):
        driver.get(self.URI)
        result = None
        while result == None:
            try:
                self.price = driver.find_element(webdriver.common.by.By.CLASS_NAME, "a-price-whole").text
                result = 1
            except: pass
        self.price+= "."
        while result == 1:
            try:
                self.price+= driver.find_element(webdriver.common.by.By.CLASS_NAME, "a-price-fraction").text
                result = 2
            except: pass
        self.sheet.cell(self.sheet.max_row, self.col).value = self.price
        return

    # Returns title and URI
    def __str__(self):
        string = "Title: "
        string+= self.title
        string+= "\nURI: "
        string+= self.URI
        string+= "\n"
        return string


if __name__ == "__main__":
    excelBook = openpyxl.Workbook()
    excelBook.worksheets[0].title = "Data"
    excelBook.worksheets[0].cell(2,1).value = "Titles: "
    excelBook.worksheets[0].cell(3,1).value = "URI: "
    excelBook.worksheets[0].cell(1,2).value = "Dates"
    print(excelBook.worksheets[0].max_column)
    p1 = product("AHHHHHHH", excelBook.worksheets[0])
    p1.setURI("baltimores")
    excelBook.save(filename="aTest.xlsx")

    options = webdriver.Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--window-size=200,200")
    #Gets the page open
    driver = webdriver.Chrome(executable_path = "chromedriver", chrome_options = options)
    driver.get(URI)