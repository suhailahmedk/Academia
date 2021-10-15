!pip install gradio -q
import gradio as gr
title = "Akadimia Ai Demo"
description = "Akadimia Ai is the worlds largest Ai Library, here is a demonstration of its predictive ABILITY!!! To use it, simply add your text, or click one of the examples to load them. Read more at the links below."
article = "<p style='text-align: center'><a href='https://instagram.com/akadimiaai/'>AKADIMIA AI WORLDS FIRST AI LIBRARY - Mohammed Makki</a></p>"
examples = [
    ['The tower is 324 metres (1,063 ft) tall,'],
    ['Nikola Tesla was known for'],
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"]
]
gr.Interface.load("huggingface/EleutherAI/gpt-j-6B", inputs=gr.inputs.Textbox(lines=5, label="Input Text"),title=title,description=description,article=article, examples=examples,enable_queue=True).launch()