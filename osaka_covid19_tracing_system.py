from selenium import webdriver
from time import sleep

#logファイル名日付対応_予定
#import datetime
#now = datetime.datetime.now()

#log対応_予定
# import logging
# import logging.config
# logging.config.fileConfig('logging.conf')
# logger = logging.getLogger('root')
# logger.debug('1. This is debug.')
# logger.info('2. This is info.')
# logger.warning('3. This is warning.')
# logger.error('4. This is error.')
# logger.critical('5. This is critical.')

driver = webdriver.Chrome("./driver/chromedriver.exe")

#######################################################################
#######################################################################

#変更箇所_自身のメールアドレス
mail_address = "メールアドレス"

#######################################################################
#######################################################################


# 大阪コロナ追跡システム URL
driver.get("QRコードURL")

#メールアドレス入力ボタン押下
btn_email = driver.find_element_by_link_text('メールアドレスを入力し登録')
btn_email.click()

#メールアドレス
email = driver.find_element_by_id('email')
email.send_keys(mail_address)

#確認用メールアドレス
email_confirmation = driver.find_element_by_id('email_confirmation')
email_confirmation.send_keys(mail_address)

#利用許諾チェック
check = driver.find_element_by_id('check')
check.click()

#登録ボタン押下
submit = driver.find_element_by_id('submit')
submit.click()

#処理待機
sleep(5)

#ブラウザclose
driver.close()

#cmd画面終了対応_予定
# #import sys
# sys.exit()