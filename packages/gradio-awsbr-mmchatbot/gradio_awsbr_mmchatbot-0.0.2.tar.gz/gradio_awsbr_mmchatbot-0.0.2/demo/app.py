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