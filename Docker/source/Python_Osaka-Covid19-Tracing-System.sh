#!/bin/sh
# 大阪コロナ追跡システム:起動/利用施設登録
python ./source/Python_Osaka-Covid19-Tracing-System_Registration.py
# 大阪コロナ追跡システム:処理待機()
sleep 60
# 大阪コロナ追跡システム:起動/大阪マイル取得
python ./source/Python_Osaka-Covid19-Tracing-System_OsakaMile.py
# 大阪コロナ追跡システム:完了
echo "finish!"