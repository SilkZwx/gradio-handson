import gradio as gr


def main_func(message, history):
    # 天気に関数する質問かどうかを判定
    return ""


demo = gr.ChatInterface(
    fn=main_func,
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(placeholder="xxx", scale=7),
)

if __name__ == "__main__":
    demo.launch()
