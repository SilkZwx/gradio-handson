import gradio as gr
import requests
import os
import dotenv

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.weatherapi.com/v1"


def format_response(response):
    location_name = response["location"]["name"]
    region = response["location"]["region"]
    country = response["location"]["country"]
    last_updated = response["current"]["last_updated"]
    temp_c = response["current"]["temp_c"]
    condition_text = response["current"]["condition"]["text"]

    response_text = (
        f"こんにちは！{location_name}の現在の天気情報です。\n\n"
        f"- 都市名: {location_name}, {region}, {country}\n"
        f"- 最新更新日時: {last_updated}\n"
        f"- 現在の気温: {temp_c}°C\n"
        f"- 天気の状態: {condition_text}\n\n"
        f"今日も一日頑張りましょう！"
    )
    return response_text


def main_func(message, history):
    # 天気に関数する質問かどうかを判定
    params = {
        # APIキー
        "key": API_KEY,
        # 都市名
        "q": message,
        # 天気情報の言語
        "lang": "ja",
    }
    responce = requests.get(f"{BASE_URL}/current.json", params=params)
    # レスポンスのステータスコードによって処理を分岐
    if responce.status_code == 200:
        # レスポンスのJSONデータを取得
        response_json = responce.json()
        # JSONデータからCbatbotのレスポンスメッセージを生成
        responce_message = format_response(response_json)
    elif responce.status_code == 400:
        code = responce.json()["code"]
        if code == 1006:
            responce_message = (
                "都市名が見つかりませんでした。もう一度入力してください。"
            )
        else:
            responce_message = (
                "エラーが発生しました。しばらくしてからもう一度お試しください。"
            )
    return responce_message


demo = gr.ChatInterface(
    fn=main_func,
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="英語で都市名を入力してください！", scale=7),
    title="現在の天気",
    description="天気の情報を答えます！",
    # theme="soft",
    examples=["Osaka", "hirakata", "Tokyo", "London"],
    # retry_btn=None,
    undo_btn="Delete Previous",
    clear_btn="Clear",
)

if __name__ == "__main__":
    dotenv.load_dotenv()
    demo.launch()
