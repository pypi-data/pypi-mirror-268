Aina Theme is a custom Gradio theme. Feel free to use this theme to create Gradio apps that have a visual connection to the world of cloud technology.

### How to edit Aina Gradio Theme colors and properties?

In case you would like to change theme properties, just edit ```AinaTheme/aina_class.py``` file.

There are custom colors that you can set at ```utils/custom_colors.py```. And if you would like to include extra colors on the theme set them at ```AinaTheme/__init__.py```

### How to use this theme in my Gradio app?
First install the theme package.
```bash
pip install aina-gradio-theme
```
Once you have installed it, add it to the interface/block parameters.
```
...
from AinaTheme import theme
with gr.Blocks(theme=theme) as demo:
    ...
```
