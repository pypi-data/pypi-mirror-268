
import gradio as gr
from app import demo as app
import os

_docs = {'MultiModalChatbot': {'description': 'Creates a chatbot that displays user-submitted messages and responses. Supports a subset of Markdown including bold, italics, code, tables.\nAlso supports audio/video/image files, which are displayed in the MultiModalChatbot, and other kinds of files which are displayed as links. This\ncomponent is usually used as an output component.\n', 'members': {'__init__': {'value': {'type': 'list[\n        list[\n            str\n            | tuple[str]\n            | tuple[str | pathlib.Path, str]\n            | None\n        ]\n    ]\n    | Callable\n    | None', 'default': 'None', 'description': 'Default value to show in chatbot. If callable, the function will be called whenever the app loads to set the initial value of the component.'}, 'label': {'type': 'str | None', 'default': 'None', 'description': 'The label for this component. Appears above the component and is also used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.'}, 'every': {'type': 'float | None', 'default': 'None', 'description': "If `value` is a callable, run the function 'every' number of seconds while the client connection is open. Has no effect otherwise. The event can be accessed (e.g. to cancel it) via this component's .load_event attribute."}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': 'if True, will display label.'}, 'container': {'type': 'bool', 'default': 'True', 'description': 'If True, will place the component in a container - providing some extra padding around the border.'}, 'scale': {'type': 'int | None', 'default': 'None', 'description': 'relative size compared to adjacent Components. For example if Components A and B are in a Row, and A has scale=2, and B has scale=1, A will be twice as wide as B. Should be an integer. scale applies in Rows, and to top-level Components in Blocks where fill_height=True.'}, 'min_width': {'type': 'int', 'default': '160', 'description': 'minimum pixel width, will wrap if not sufficient screen space to satisfy this value. If a certain scale value results in this Component being narrower than min_width, the min_width parameter will be respected first.'}, 'visible': {'type': 'bool', 'default': 'True', 'description': 'If False, component will be hidden.'}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': 'An optional string that is assigned as the id of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': 'An optional list of strings that are assigned as the classes of this component in the HTML DOM. Can be used for targeting CSS styles.'}, 'render': {'type': 'bool', 'default': 'True', 'description': 'If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.'}, 'height': {'type': 'int | str | None', 'default': 'None', 'description': 'The height of the component, specified in pixels if a number is passed, or in CSS units if a string is passed.'}, 'latex_delimiters': {'type': 'list[dict[str, str | bool]] | None', 'default': 'None', 'description': 'A list of dicts of the form {"left": open delimiter (str), "right": close delimiter (str), "display": whether to display in newline (bool)} that will be used to render LaTeX expressions. If not provided, `latex_delimiters` is set to `[{ "left": "$$", "right": "$$", "display": True }]`, so only expressions enclosed in $$ delimiters will be rendered as LaTeX, and in a new line. Pass in an empty list to disable LaTeX rendering. For more information, see the [KaTeX documentation](https://katex.org/docs/autorender.html).'}, 'rtl': {'type': 'bool', 'default': 'False', 'description': 'If True, sets the direction of the rendered text to right-to-left. Default is False, which renders text left-to-right.'}, 'show_share_button': {'type': 'bool | None', 'default': 'None', 'description': 'If True, will show a share icon in the corner of the component that allows user to share outputs to Hugging Face Spaces Discussions. If False, icon does not appear. If set to None (default behavior), then the icon appears if this Gradio app is launched on Spaces, but not otherwise.'}, 'show_copy_button': {'type': 'bool', 'default': 'False', 'description': 'If True, will show a copy button for each chatbot message.'}, 'avatar_images': {'type': 'tuple[\n        str | pathlib.Path | None, str | pathlib.Path | None\n    ]\n    | None', 'default': 'None', 'description': 'Tuple of two avatar image paths or URLs for user and bot (in that order). Pass None for either the user or bot image to skip. Must be within the working directory of the Gradio app or an external URL.'}, 'sanitize_html': {'type': 'bool', 'default': 'True', 'description': 'If False, will disable HTML sanitization for chatbot messages. This is not recommended, as it can lead to security vulnerabilities.'}, 'render_markdown': {'type': 'bool', 'default': 'True', 'description': 'If False, will disable Markdown rendering for chatbot messages.'}, 'bubble_full_width': {'type': 'bool', 'default': 'True', 'description': 'If False, the chat bubble will fit to the content of the message. If True (default), the chat bubble will be the full width of the component.'}, 'line_breaks': {'type': 'bool', 'default': 'True', 'description': 'If True (default), will enable Github-flavored Markdown line breaks in chatbot messages. If False, single new lines will be ignored. Only applies if `render_markdown` is True.'}, 'likeable': {'type': 'bool', 'default': 'False', 'description': 'Whether the chat messages display a like or dislike button. Set automatically by the .like method but has to be present in the signature for it to show up in the config.'}, 'layout': {'type': '"panel" | "bubble" | None', 'default': 'None', 'description': 'If "panel", will display the chatbot in a llm style layout. If "bubble", will display the chatbot with message bubbles, with the user and bot messages on alterating sides. Will default to "bubble".'}}, 'postprocess': {'value': {'type': 'list[\n        list[str | tuple[str] | tuple[str, str] | None]\n        | tuple\n    ]\n    | None', 'description': 'expects a `list[list[str | None | tuple]]`, i.e. a list of lists. The inner list should have 2 elements: the user message and the response message. The individual messages can be (1) strings in valid Markdown, (2) tuples if sending files: (a filepath or URL to a file, [optional string alt text]) -- if the file is image/video/audio, it is displayed in the MultiModalChatbot, or (3) None, in which case the message is not displayed.'}}, 'preprocess': {'return': {'type': 'list[MultimodalMessage] | None', 'description': "The preprocessed input data sent to the user's function in the backend."}, 'value': None}}, 'events': {'change': {'type': None, 'default': None, 'description': 'Triggered when the value of the MultiModalChatbot changes either because of user input (e.g. a user types in a textbox) OR because of a function update (e.g. an image receives a value from the output of an event trigger). See `.input()` for a listener that is only triggered by user input.'}, 'select': {'type': None, 'default': None, 'description': 'Event listener for when the user selects or deselects the MultiModalChatbot. Uses event data gradio.SelectData to carry `value` referring to the label of the MultiModalChatbot, and `selected` to refer to state of the MultiModalChatbot. See EventData documentation on how to use this event data'}, 'like': {'type': None, 'default': None, 'description': 'This listener is triggered when the user likes/dislikes from within the MultiModalChatbot. This event has EventData of type gradio.LikeData that carries information, accessible through LikeData.index and LikeData.value. See EventData documentation on how to use this event data.'}}}, '__meta__': {'additional_interfaces': {'MultimodalMessage': {'source': 'class MultimodalMessage(GradioModel):\n    text: Optional[str] = None\n    files: Optional[List[FileMessage]] = None', 'refs': ['FileMessage']}, 'FileMessage': {'source': 'class FileMessage(GradioModel):\n    file: FileData\n    alt_text: Optional[str] = None'}}, 'user_fn_refs': {'MultiModalChatbot': ['MultimodalMessage']}}}

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
# `gradio_awsbr_mmchatbot`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_awsbr_mmchatbot/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_awsbr_mmchatbot"></a>  
</div>

This component enables multi-modal input for the Anthropic Claude v3 suite of models available from Amazon Bedrock
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_awsbr_mmchatbot
```

## Usage

```python
import gradio as gr
from gradio_awsbr_mmchatbot import MultiModalChatbot
from gradio.data_classes import FileData
from bedrock_utils import MultimodalInputHandler


# A function to call the multi-modal input for Anthropic Claude v3 sonnet using Bedrock boto3
async def get_response(text, file):
    # If there is a file uploaded, then we will send it to Anthropic Claude v3 sonnet.
    # If there is no file uploaded, then we will send the text to Anthropic Claude v3 sonnet.
    try:
        userMsg = {
            "text": text,
            "files": [{"file": FileData(path=file)}]
        }
    except:
        userMsg = {
            "text": text,
            "files": []
        }
    # Define a variable to store the response from the Anthropic Claude v3 sonnet
    llmResponse = ""
    handler = MultimodalInputHandler(text, file)
    # Loop through the response from Anthropic Claude v3 sonnet, and append it to our llmResponse variable.
    async for x in handler.handleInput():
        llmResponse += x
        yield [[userMsg, {"text": llmResponse, "files": []}]]
    # Yield the response from Anthropic Claude v3 sonnet. This is unecessary as we can just yield the llmResponse variable in an iterative fashion as above.
    # But just in case.... let's yield the entire response object as well and overwrite the messages in the Chatbot.
    response = {
        "text": llmResponse,
        "files": []
    }
    yield [[userMsg, response]]

# Defining Gradio Interface using Blocks Structure
with gr.Blocks() as demo:
    # Give it a Title
    gr.Markdown("## Gradio - MultiModal Chatbot")
    # Define the Chat Tab
    with gr.Tab(label="Chat"):
        with gr.Row():
            with gr.Column(scale=3):
                # Set a variable equal to our MultiModalChatBot class
                chatBot = MultiModalChatbot(height=700, render_markdown=True, bubble_full_width=True)
        with gr.Row():
            with gr.Column(scale=3):
                # Set a variable equal to our user message
                msg = gr.Textbox(placeholder='What is the meaning of life?', show_label=False)
            with gr.Column(scale=1):
                # Set a variable equal to our file upload
                fileInput = gr.File(label="Upload Files")
            with gr.Column(scale=1):
                # Define our submit button and invoke our 'get_response' function when it's clicked.
                gr.Button('Submit', variant='primary').click(get_response, inputs=[msg,fileInput], outputs=chatBot)
                # Same function as above, but with the 'enter' key being pressed inside the gr.Textbox() component instead of the 'submit' button.
                msg.submit(get_response, inputs=[msg, fileInput], outputs=chatBot)


if __name__ == '__main__':
    demo.queue().launch()
```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `MultiModalChatbot`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["MultiModalChatbot"]["members"]["__init__"], linkify=['MultimodalMessage', 'FileMessage'])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["MultiModalChatbot"]["events"], linkify=['Event'])




    gr.Markdown("""

### User function

The impact on the users predict function varies depending on whether the component is used as an input or output for an event (or both).

- When used as an Input, the component only impacts the input signature of the user function.
- When used as an output, the component only impacts the return signature of the user function.

The code snippet below is accurate in cases where the component is used as both an input and an output.

- **As input:** Is passed, the preprocessed input data sent to the user's function in the backend.
- **As output:** Should return, expects a `list[list[str | None | tuple]]`, i.e. a list of lists. The inner list should have 2 elements: the user message and the response message. The individual messages can be (1) strings in valid Markdown, (2) tuples if sending files: (a filepath or URL to a file, [optional string alt text]) -- if the file is image/video/audio, it is displayed in the MultiModalChatbot, or (3) None, in which case the message is not displayed.

 ```python
def predict(
    value: list[MultimodalMessage] | None
) -> list[
        list[str | tuple[str] | tuple[str, str] | None]
        | tuple
    ]
    | None:
    return value
```
""", elem_classes=["md-custom", "MultiModalChatbot-user-fn"], header_links=True)




    code_MultimodalMessage = gr.Markdown("""
## `MultimodalMessage`
```python
class MultimodalMessage(GradioModel):
    text: Optional[str] = None
    files: Optional[List[FileMessage]] = None
```""", elem_classes=["md-custom", "MultimodalMessage"], header_links=True)

    code_FileMessage = gr.Markdown("""
## `FileMessage`
```python
class FileMessage(GradioModel):
    file: FileData
    alt_text: Optional[str] = None
```""", elem_classes=["md-custom", "FileMessage"], header_links=True)

    demo.load(None, js=r"""function() {
    const refs = {
            MultimodalMessage: ['FileMessage'], 
            FileMessage: [], };
    const user_fn_refs = {
          MultiModalChatbot: ['MultimodalMessage'], };
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
