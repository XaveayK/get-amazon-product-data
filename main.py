import sys
import allProducts
import asyncio

if __name__ == "__main__":
    arg = sys.argv
    products = allProducts.amazonProducts()
    if arg[1].lower() == '-h':
        print("Name\n\tAmazon Tracker - To track target amazon products over time in a standardized format" + 
                    "\n\nSynopsis\n\n\tmain.py -a [TITLE] [URI]\n\tmain.py -r [TITLE]\n\tmain.py -u\n\tmain.py -h\n\n" +
                    "Description\n\n\t-a\tAdd a product with title and uri\n\t-r\tRemove a product with title\n" +
                    "\t-h\tGet the man page\n\t-u\tUpdates the prices")
    elif arg[1].lower() == "-u":
        while not (asyncio.run(products.updatePricing())): pass
    elif arg[1].lower() == "-a":
        products.addProduct(arg[2], arg[3])
    elif arg[1].lower() == "-r":
        products.remProduct(arg[2])