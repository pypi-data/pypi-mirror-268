
import gradio as gr
from app import demo as app
import os

_docs = {'VariableSlider': {'description': 'Creates a slider that ranges from {minimum} to {maximum} with a step size of {step}.\n', 'members': {'__init__': {'minimum': {'type': 'float', 'default': '0', 'description': 'minimum value for slider.'}, 'maximum': {'type': 'float', 'default': '100', 'description': 'maximum value for slider.'}, 'value': {'type': 'float | Callable | None', 'default': 'None', 'description': 'default value. If callable, the function will be called whenever the app loads to set the initial value of the component. Ignored if randomized=True.'}, 'step': {'type': 'float | None', 'default': 'None', 'description': 'increment between slider values.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'info': {'type': 'str | None', 'default': 'None', 'description': 'additional component description.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': 'if True, slider will be adjustable; if False, adjusting will be disabled. If not provided, this is inferred based on whether the component is used as an input or output.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}}, 'postprocess': {'value': {'type': 'float | None', 'description': 'Expects an {int} or {float} returned from function and sets slider value to it as long as it is within range (otherwise, sets to minimum value).'}}, 'preprocess': {'return': {'type': 'float', 'description': 'Passes slider value as a {float} into the function.'}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the VariableSlider changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'input': {'type': None, 'default': None, 'description': 'This listener is triggered when the user changes the value of the VariableSlider.'}, 'release': {'type': None, 'default': None, 'description': 'This listener is triggered when the user releases the mouse on this VariableSlider.'}}}, '__meta__': {'additional_interfaces': {}, 'user_fn_refs': {'VariableSlider': []}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_variableslider`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_variableslider/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_variableslider"></a>  
</div>

Python library for easily interacting with trained machine learning models
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_variableslider
```

## Usage

```python

import gradio as gr
from gradio_variableslider import VariableSlider

example = VariableSlider().example_value()

with gr.Blocks() as demo:
    sub_slider = gr.Slider(label="Sub-Divisions", minimum=5, maximum=1000, step=5, value=1000, info="This is the amount of values that will occur between each integer.", interactive=True)
    def slider_function(slider_val):
        step = round(1/slider_val, 3)
        slider_final = VariableSlider(minimum=0, maximum=3, value=0, step=step, interactive=True)
        return slider_final
    alpha_slider = VariableSlider(label="Alpha", minimum=0, maximum=2.99, step=0.01, interactive=True)
    sub_slider.release(fn=slider_function, inputs=sub_slider, outputs=alpha_slider)


if __name__ == "__main__":
    demo.queue().launch()

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `VariableSlider`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["VariableSlider"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["VariableSlider"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, passes slider value as a {float} into the function.
- **As output:** Should return, expects an {int} or {float} returned from function and sets slider value to it as long as it is within range (otherwise, sets to minimum value).

 ```python
def predict(
    value: float
) -> float | None:
    return value
```
""", elem_classes=["md-custom", "VariableSlider-user-fn"], header_links=True)




    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {
          VariableSlider: [], };
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
