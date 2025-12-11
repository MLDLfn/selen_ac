from DrissionPage import Chromium, ChromiumOptions
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()
co = ChromiumOptions()
co.set_argument("--no-sandbox")
browser = Chromium(co)
page = browser.latest_tab
page.get("https://batdongsan.com.vn")
print(page.html)
page.close()
display.stop()
