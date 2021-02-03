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

# 大阪コロナ追跡システム URL
# 大阪マイル_創造社一階
driver.get("受信メール記載URL")

#処理待機
sleep(5)

#ブラウザclose
driver.close()

#cmd画面終了対応_予定
# #import sys
# sys.exit()