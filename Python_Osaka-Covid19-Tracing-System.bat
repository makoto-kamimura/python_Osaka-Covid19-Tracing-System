@echo off

rem ■ 大阪コロナ追跡システム:起動/利用施設登録
py Python_Osaka-Covid19-Tracing-System_Registration.py

rem ■ 大阪コロナ追跡システム:処理待機()
ping localhost -n 61 >NUL:

rem ■ 大阪コロナ追跡システム:起動/大阪マイル取得
py Python_Osaka-Covid19-Tracing-System_OsakaMile.py

rem ■ 大阪コロナ追跡システム:完了
echo.finish!

pause