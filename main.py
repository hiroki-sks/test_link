from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

# Selenium WebDriverを設定する
def get_driver():
    options = Options()
    #options.headless = True  # ヘッドレスモード（GUIなし）
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

@app.route('/start-selenium', methods=['POST'])
def start_selenium():
    # フロントエンドからのリンク一覧を受け取る
    data = request.get_json()  # JSONデータを取得
    links = data.get('links', [])  # 'links'データを取得
    
    driver = get_driver()
    results = []

    for link in links:
        url = link['url']
        driver.get(url)
        
        # ページが正常に読み込まれるか確認（例: ステータスコードが200か）
        time.sleep(2)  # 少し待機
        
        if "404" in driver.title or "500" in driver.title:
            # 404や500エラーの場合
            results.append({"url": url, "status": "failed"})
        else:
            # 正常にページが表示された場合
            results.append({"url": url, "status": "success"})
    
    driver.quit()
    return jsonify(results)  # 結果をJSON形式で返す

if __name__ == '__main__':
    app.run(debug=True)




# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# import openpyxl
# import time

# # WebDriverのパスを指定
# CHROMEDRIVER_PATH = r'C:\Users\user01\Documents\selenium\chromedriver.exe'

# # Excelファイルのパスを指定
# EXCEL_FILE = "urls.xlsx"

# # Excelファイルを読み込む
# wb = openpyxl.load_workbook(EXCEL_FILE)
# ws = wb.active

# # B列のURLを取得（2行目から読み込む）
# urls = [row[0].value for row in ws.iter_rows(min_row=2, max_col=1)]

# # Chromeブラウザのオプション設定
# chrome_options = Options()
# #chrome_options.add_argument("--headless")  # ヘッドレスモード（画面を表示しない）
# #chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox")  # 必要に応じて追加

# # WebDriverを初期化
# service = Service(CHROMEDRIVER_PATH)
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # 結果を書き込む列を指定（例: C列に書き込む）
# result_column = 3  # C列

# # URLを順にチェック
# for i, url in enumerate(urls, start=2):  # 2行目から開始
#     try:
#         # URLを開く
#         driver.get(url)
#         time.sleep(3)  # ページ読み込みを待機（適宜調整）

#         # ページのタイトルを取得
#         page_title = driver.title

#         # 404やエラーページの可能性を判定
#         if "404" in page_title or "Not Found" in page_title:
#             ws.cell(row=i, column=result_column).value = "リンク切れ"
#         else:
#             ws.cell(row=i, column=result_column).value = "正常"
#     except Exception as e:
#         # エラーが発生した場合は結果に記録
#         ws.cell(row=i, column=result_column).value = f"エラー: {e}"
#     finally:
#         print(f"{i - 1}: {url} - チェック完了")

# # 結果を保存
# wb.save("urls_checked.xlsx")

# # WebDriverを終了
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
# import pickle  # クッキーの保存と読み込みに使用

# # ドライバの設定
# service = Service(executable_path="chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# driver = webdriver.Chrome(service=service, options=options)

# # Google アカウントのログインページにアクセス
# driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AcMMx-eah9_uCIZk0Svb5JXy5l_0Jok0DMy3hWS8-24YFxrFaSulUfN8a59JacoWXZQzws0KzAwh&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1393457770%3A1731225947207107&ddm=1')
# driver.maximize_window()

# # 手動でメールアドレスとパスワードを入力してログイン
# # ログイン後のクッキーを保存
# time.sleep(30)  # ログインするために十分な時間を与える（手動入力後に次に進む）

# # ログイン後のクッキーを保存
# pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

# # ドライバを終了する
# driver.quit()

# # 次回の自動化を再開する
# # クッキーを読み込んでセッションを再利用
# driver = webdriver.Chrome(service=service, options=options)

# # Gmail にアクセス
# driver.get('https://mail.google.com')

# # クッキーを読み込み
# cookies = pickle.load(open("cookies.pkl", "rb"))
# for cookie in cookies:
#     driver.add_cookie(cookie)

# # クッキーを読み込んだ後に再度Gmailにアクセス
# driver.get('https://mail.google.com')

# # メール操作を自動化したい場合はここに続けて操作を追加
# time.sleep(10)  # 例えばGmailが完全に読み込まれるまで待機
# driver.quit()







# from selenium import webdriver
# from selenium.webdriver.edge.service import Service  # Edge用のServiceをインポート
# from selenium.webdriver.common.by import By
# import time

# # Edge WebDriverのパスを指定（msedgedriver.exeの場所を指定）
# service = Service(executable_path="msedgedriver.exe")

# # Edgeのオプションを設定
# options = webdriver.EdgeOptions()  # EdgeOptionsに変更
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

# # Edge WebDriverを起動
# driver = webdriver.Edge(service=service, options=options)

# # Googleのログインページにアクセス
# driver.get("https://www.google.com")
# driver.maximize_window()
# driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=AcMMx-eah9_uCIZk0Svb5JXy5l_0Jok0DMy3hWS8-24YFxrFaSulUfN8a59JacoWXZQzws0KzAwh&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S1393457770%3A1731225947207107&ddm=1')

# # メールアドレスを入力して次へ進む
# input_element = driver.find_element(By.ID, "identifierId")
# input_element.send_keys("sakasaih@systena.co.jp")
# next_button = driver.find_element(By.ID, "identifierNext")
# next_button.click()

# # 少し待機してからブラウザを閉じる
# time.sleep(40)
# driver.quit()


# ※良く使用するメソッド
# get(url)：指定したURLを開く
# find_element_by_*：ページ内の要素を検索
# click()：要素をクリック
# send_keys()：入力ボックスにテキストを入力
# submit()：フォームの送信


# バージョン 131.0.2903.99 (公式ビルド) (64 ビット)
