from selenium import webdriver
from time import sleep

# WebDriverを取得
driver = webdriver.Chrome("./driver/chromedriver.exe")

#######################################################################
# この枠内の値のみを変更して下さい！

# 利用登録する利用施設のURL
URL = "利用する施設のQRコードにより取得したURL"

# 利用登録をする自身のメールアドレス
mailAddress = "sample@gmail.com"

#######################################################################

# "GoogleChrome"を起動
driver.get(URL)

# work_クラス対応
# 大阪コロナ追跡システム:メールアドレス入力ボタンを押下
btn_email = driver.find_element_by_link_text('メールアドレスを入力し登録')
btn_email.click()
# 大阪コロナ追跡システム:メールアドレスを入力
email = driver.find_element_by_id('email')
email.send_keys(mailAddress)
# 大阪コロナ追跡システム:確認用メールアドレスを入力
email_confirmation = driver.find_element_by_id('email_confirmation')
email_confirmation.send_keys(mailAddress)
# 大阪コロナ追跡システム:利用許諾のチェックを入力
check = driver.find_element_by_id('check')
check.click()
# 大阪コロナ追跡システム:登録ボタンを押下
submit = driver.find_element_by_id('submit')
submit.click()
# 大阪コロナ追跡システム:処理待機()
sleep(5)

# "GoogleChrome"を終了
driver.close()

# work_CUI画面終了
# #import sys
# sys.exit()