import gradio as gr


def main_func(message, history):
    # 天気に関数する質問かどうかを判定
    return ""


demo = gr.ChatInterface(
    fn=main_func,
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="天気を聞いてください！", scale=7),
)

if __name__ == "__main__":
    demo.launch()
