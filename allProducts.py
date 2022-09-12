import product
from os.path import exists


class amazonChecking:
    def __init__(self, fileName="products.xlsx"):
        self.fileName = fileName
        if exists(self.fileName):                                   # Loads spreadsheet
            self.wb = product.openpyxl.load_workbook(self.fileName)
        else:                                                       # Creates workbook and spreadsheet filling it with format
            self.wb = product.openpyxl.Workbook()
            self.wb.worksheets[0].title = "Products"
            self.wb.worksheets[0].cell(2,1).value = "Names: "
            self.wb.worksheets[0].cell(3,1).value = "ASIN: "
            self.wb.worksheets[0].cell(1,2).value = "Dates: "
        self.wb.save(filename=self.fileName)

    def addProduct(self, name, asin):
        product.product(name, asin, self.wb.worksheets[0])
        self.wb.save(filename=self.fileName)

    def remProduct(name):
        pass

    def updatePricing(self):
        ASINs = self.wb.worksheets[0].iter_cols(min_row=3, max_row=3, min_col=3, values_only=True)
        for ASIN in ASINs:
            print(ASIN)

    def __str__(self):
        products = self.wb.worksheets[0].iter_cols(min_row=2, max_row=3, min_col=3, values_only=True)
        for product in products:
            print(product)
        return ""

    
if __name__ == "__main__":
    x = amazonChecking()
    x.addProduct("Samsung", "22fd2")
    x.addProduct("Vivo", "3fd5")
    print(x)
    x.updatePricing()