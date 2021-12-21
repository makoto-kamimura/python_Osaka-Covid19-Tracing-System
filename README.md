# Python_Osaka-Covid19-Tracing-System
当ツールは  
大阪府が運営/開発をしている"大阪コロナ追跡システム"のサードパーティーツールです。  
下記プロセスにより、利用施設の登録及び大阪マイル取得をワンクリックで可能とするツールとなります。  
※1 利用施設がある程度決まっており、その都度のQR読込作業の簡略化を目的として制作しております。  
※2 "※1" の目的に沿わないご利用や、その他のご利用における責任等は一切負いかねますので、予めご了承下さい。

# DEMO
![Python_Osaka-Covid19-Tracing-System](/README_img/Python_Osaka-Covid19-Tracing-System.gif)

# Requirement
※後程バージョン等記載予定
* Windows10
    * Python
        * Selenium
        * Chrome Webdriver

# Installation
## Windows_CommandPrompt
0. 事前準備
    1. git clone https://github.com/makoto-kamimura/Python_Osaka-Covid19-Tracing-System.git
1. 事前準備_REGISTRATION
    1. 利用する施設に配置されているQRコードを読み取る
    2. QRコードにより取得をしたWEBサイトのURLをコピー
    3. 対象のソースコードに "2." で取得をした情報等を記述
        1. "0-1" で取得したリポジトリにおける対象ファイル"CommandPrompt/Python_Osaka-Covid19-Tracing-System_Registration.py"をテキストエディッタ等で開く
        2. 対象ソースコードにおける"施設情報"を以下のように変更/入力  
        * Before
            ```python
            10 # 利用登録する利用施設のURL
            11 URL = "利用する施設のQRコードにより取得したURL"
            ```
        * After
            ```python
            10 # 利用登録する利用施設のURL
            11 URL = "https://www.google.com/"
            ```
        3. 対象ソースコードにおける"その他情報"を以下のように変更/入力  
        * Before
            ```python
            10 # 利用登録完了メールに記載されているURL
            11 URL = "利用登録完了メールに記載されているURL"
            ```
        * After
            ```python
            10 # 利用登録完了メールに記載されているURL
            11 URL = "https://www.google.com/"
            ```
        4. 対象のファイルを保存
2. 事前準備_OSAKAMILE
    1. 利用後に送信されてきたメールに記載されている"大阪マイルを取得する"を押下
    2. 表示されているWEBサイトのURLをコピー
    3. 対象のソースコードに "2." で取得をした情報等を記述
        1. "0-i" で取得したリポジトリにおける対象ファイル"CommandPrompt/Python_Osaka-Covid19-Tracing-System_OsakaMile.py"をテキストエディッタ等で開く
        2. 対象ソースコードにおける"施設情報"を以下のように変更/入力
        ```python
        ※後程更新予定
        ```
        4. 対象のファイルを保存
3. 利用方法
    1. コマンドプロンプトにて対象ファイル"CommandPrompt/Python_Osaka-Covid19-Tracing-System_Registration.bat" を実行

## Docker_[準備中]
```bash
git clone https://github.com/makoto-kamimura/Python_Osaka-Covid19-Tracing-System.git
cd Docker/
docker-compose up -d --build
docker-compose exec python3 bash
bash source/Python_Osaka-Covid19-Tracing-System.sh
exit
docker-compose down -v
```

# Note
* 大阪府／大阪コロナ追跡システムについて
    * http://www.pref.osaka.lg.jp/smart_somu/osaka_covid19/index.html
* 参考サイト様  
    * https://qiita.com/memakura/items/20a02161fa7e18d8a693
    * https://yuki.world/python-selenium-chromedriver-auto-update/

# License
"Python_Osaka-Covid19-Tracing-System" is Confidential.