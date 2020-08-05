from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    # 啟動無頭模式
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 規避google bug
    chrome_options.add_argument('--disable-gpu')
    # Chrome 驅動程式
    executable_path = 'D:\\9.workspace\\02.PYTHON\\chromedriver.exe'
    # 啟動
    driver = webdriver.Chrome(executable_path=executable_path,
                              chrome_options=chrome_options)
    # 設置等待時間
    driver.implicitly_wait(30)

    url = 'https://forum.gamer.com.tw/C.php?bsn=31066&snA=1510&tnum=1386'
    driver.get(url)
    a_href = driver.find_element_by_xpath('//div[@class="c-reply__head nocontent"]/a')
    print(a_href)
    a_href.click()
except:
    print("發生錯誤")