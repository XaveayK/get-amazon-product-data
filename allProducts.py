import product
from os.path import exists
from product import webdriver
from datetime import date

class amazonProducts:
    def __init__(self, fileName="products.xlsx"):
        self.fileName = fileName
        self.products = {}
        if exists(self.fileName):                                   # Loads spreadsheet
            self.wb = product.openpyxl.load_workbook(self.fileName)
            self.__loadExcel__()
        else:                                                       # Creates workbook and spreadsheet filling it with format
            self.wb = product.openpyxl.Workbook()
            self.wb.worksheets[0].title = "Products"
            self.wb.worksheets[0].cell(2,1).value = "Names: "
            self.wb.worksheets[0].cell(3,1).value = "URI: "
            self.wb.worksheets[0].cell(1,2).value = "Dates: "
            self.wb.save(filename=self.fileName)

    def __loadExcel__(self):
        lis = [list(r) for r in self.wb.worksheets[0].iter_rows(values_only=True, min_col=3, max_row=2, min_row=2)]
        for column in self.wb.worksheets[0].iter_cols(min_row=2, min_col=3):
            self.addProduct(column[0].value, column[1].value, lis)

    def addProduct(self, title, uri, keys=None):
        if title not in self.products.keys():
            item = product.product(title, uri, self.wb.worksheets[0], keys)
            self.products[title] = item
            self.wb.save(filename=self.fileName)

    def remProduct(name):
        pass

    async def updatePricing(self):
        opts = webdriver.chrome.options.Options()
        opts.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        opts.add_argument('--ignore-certificate-errors')
        opts.add_argument("--disable-extensions")
        opts.add_argument("--headless")
        opts.add_argument("--disable-webgl")
        opts.add_argument("--disable-gpu")
        #Gets the page open
        driver = webdriver.Chrome(executable_path = "chromedriver", options = opts)

        for product in self.products.values():
            await product.getPriceFromPage(driver)
        
        self.wb.save(filename=self.fileName)
        self.wb.worksheets[0].cell(self.wb.worksheets[0].max_row + 1, 2).value = date.today()       # Sets the date for today in excel
    
    def __str__(self):
        string = ""
        for product in self.products.values():
            string += str(product)
            string += "\n"
        return string

    
if __name__ == "__main__":
    x = amazonProducts()
    x.addProduct("Samsung 49\" Odyssey Neo g9", "https://www.amazon.ca/SAMSUNG-5120x1440-Adjustable-FreeSync-LS49AG952NNXZA/dp/B096YNP6ZR/ref=sr_1_2?crid=KUUFTHC5SA5R&keywords=samsung+odyssey+g9+neo&qid=1663031908&sprefix=samsung+odyssey+g9+neo%2Caps%2C107&sr=8-2")
    x.addProduct("Vivo Premium Heavy Duty Monitor Arm", "https://www.amazon.ca/VIVO-Premium-Aluminum-Pneumatic-STAND-V101G1/dp/B07L8MLTGS/ref=sr_1_5?keywords=vivo+pneumatic+monitor+arm&qid=1663031948&sprefix=vivo+pneumat%2Caps%2C130&sr=8-5")
    print(x)
    import asyncio
    asyncio.run(x.updatePricing())