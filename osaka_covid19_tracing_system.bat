@echo off

rem ■ 大阪コロナ追跡システムを起動する
py osaka_covid19_tracing_system.py

rem ■ 60秒待つ
ping localhost -n 61 >NUL:

rem ■ 大阪コロナ追跡システムを起動する_マイルの取得
py osaka_covid19_tracing_system_osakamile.py

rem ■ 完了メッセージを表示する
echo.finish!

pause