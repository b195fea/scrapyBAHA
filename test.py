from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    # executable_path = 'D:\\9.workspace\\02.PYTHON\\chromedriver.exe'
    executable_path = 'D:\\driver\\chromedriver.exe'

    # 啟動無頭模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 規避google bug
    chrome_options.add_argument('--disable-gpu')
    # Chrome 驅動程式
    # 啟動
    # driver = webdriver.Chrome(executable_path=executable_path,chrome_options=chrome_options)
    driver = webdriver.Chrome(executable_path=executable_path)
    # 設置等待時間
    driver.implicitly_wait(30)

    url = 'https://forum.gamer.com.tw/C.php?bsn=31066&snA=1510&tnum=1386'
    driver.get(url)
    # a_href = driver.find_element_by_xpath('//a[@class="more-reply"]')
    # driver.execute_script("arguments[0].click();", a_href)

    a_href = driver.find_elements_by_css_selector('a.more-reply')
    for a in a_href:
        driver.execute_script("arguments[0].click();", a)
        # a.click()

    pageSource = driver.page_source

    print(pageSource)
    filename = 'quotes-aa.html'
    with open(filename, 'wb') as f:
        f.write(str(pageSource))
    # driver.execute_script("arguments[0].click();", a_href)
    print("click")
except Exception as e:
    print("發生錯誤：" + e)