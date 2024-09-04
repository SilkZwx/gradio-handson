import gradio as gr
import re


def main_func(message, history):
    # 天気に関数する質問かどうかを判定
    if re.search(r"天気", message):
        return "晴れです！"
    else:
        return "天気に関する質問をしてください！"


demo = gr.ChatInterface(
    fn=main_func,
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="天気を聞いてください！", scale=7),
    title="天気予報",
    description="天気の質問に答えます！",
    # theme="soft",
    # examples=["今日の天気は？", "明日の天気を教えてください"],
    # retry_btn=None,
)

if __name__ == "__main__":
    demo.launch()
