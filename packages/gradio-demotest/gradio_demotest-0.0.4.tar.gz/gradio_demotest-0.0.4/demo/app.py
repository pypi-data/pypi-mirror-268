
import gradio as gr
from gradio_demotest import DemoTest


example = DemoTest().example_value()

demo = gr.Interface(
    lambda x:x,
    DemoTest(),  # interactive version of your component
    DemoTest(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
