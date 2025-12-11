import sys
import io

# 设置标准输出为 utf-8 编码
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from DrissionPage import Chromium, ChromiumOptions
co = ChromiumOptions()
co.set_argument("--no-sandbox")
browser = Chromium(co)
page = browser.latest_tab
page.get("https://batdongsan.com.vn/nha-dat-cho-thue")
# print(page.html)
# 或者直接在打印时指定编码（如果仅是某个打印语句需要处理）
print(page.html)
page.close()
