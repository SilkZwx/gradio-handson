import gradio as gr


def main_func(name):
    return "Hello, " + name + "!"


demo = gr.Interface(
    inputs=xxx,
    fn=main_func,
    outputs=gr.Textbox(label="Greeting"),
)

if __name__ == "__main__":
    demo.launch()
