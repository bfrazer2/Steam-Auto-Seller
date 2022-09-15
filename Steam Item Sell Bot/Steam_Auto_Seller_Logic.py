from Objects import Steam_Auto_Seller_Objects

class Sell:

	driver = webdriver.Firefox()
	augmented_steam = driver.install_addon(r'C:\Users\bfraz\Desktop\Steam Item Sell Bot\augmented_steam-2.3.3.xpi')
	action = ActionChains(driver) 

	Ben = LogIn(driver)
	Ben.navigate()
	Ben.login()

	MyInventory = Inventory(driver)
	MyInventory.expand()
	MyInventory.filters("Type","wearable","bundle","loading_screen")
	MyInventory.filters("misc","marketable")
	MyInventory.sell_items()

if __name__ == "__main__":
	Sell()