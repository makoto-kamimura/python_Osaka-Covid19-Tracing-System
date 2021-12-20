from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# WebDriverを取得
# driver = webdriver.Chrome("./driver/chromedriver.exe")

# WebDriverの最新版を取得
driver = webdriver.Chrome(ChromeDriverManager().install())

#######################################################################
# この枠内の値のみを変更して下さい！

# 利用登録完了メールに記載されているURL
URL = "利用登録完了メールに記載されているURL"

#######################################################################

# "GoogleChrome"を起動
driver.get(URL)
# 大阪コロナ追跡システム:処理待機()
sleep(5)

# "GoogleChrome"を終了
driver.close()

# work_CUI画面終了
# #import sys
# sys.exit()