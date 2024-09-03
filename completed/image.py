import gradio as gr


def main_func(image):
    return image


demo = gr.Interface(
    inputs=gr.Image(),
    fn=main_func,
    outputs=gr.Textbox(label="Greeting"),
    title="画像分類デモ",
    description="このデモでは、画像をアップロードすると画像の内容を表示します",
)

if __name__ == "__main__":
    demo.launch()
