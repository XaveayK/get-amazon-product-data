import openpyxl

class product:
    # Defines perameters necessary for searching in API
    def __init__(self, title, ASIN, excelSheet):
        self.title = title
        self.sheet = excelSheet
        self.ASIN = ASIN
        self.col = self.sheet.max_column+1
        self.sheet.cell(2, self.col).value = self.title
        self.sheet.cell(3, self.col).value = self.ASIN

    # Incase you need to update the ASIN
    def setASIN(self, ASIN):
        self.ASIN = ASIN
        self.sheet.cell(3, self.col).value = ASIN
    
    # Calls the amazon API to get the price with the ASIN
    def currPrice(self, price):
        self.sheet.cell(self.sheet.max_row, self.col).value = price

    # Returns title and ASIN
    def __str__(self):
        return "Name: " + self.title, "ASIN: " + self.ASIN + "\n"


if __name__ == "__main__":
    excelBook = openpyxl.Workbook()
    excelBook.worksheets[0].title = "Data"
    excelBook.worksheets[0].cell(2,1).value = "Titles: "
    excelBook.worksheets[0].cell(3,1).value = "ASIN: "
    excelBook.worksheets[0].cell(1,2).value = "Dates"
    print(excelBook.worksheets[0].max_column)
    p1 = product("AHHHHHHH", excelBook.worksheets[0])
    p1.setASIN("baltimores")
    
    excelBook.save(filename="aTest.xlsx")