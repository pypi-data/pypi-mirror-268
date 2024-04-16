import json
import base64
import os
from anthropic import AnthropicBedrock
from PIL import Image

class MultimodalInputHandler:
    def __init__(self, text, image=None):
        self.text = text
        self.image = image

        self.client = AnthropicBedrock(
            aws_region='us-west-2'
        )

    async def handleInput(self):
        if self.image:

            # Determine the format of the image
            if self.image.endswith(".jpg"):
                formatType = "image/jpeg"
            elif self.image.endswith(".png"):
                formatType = "image/png"
            elif self.image.endswith(".gif"):
                formatType = "image/gif"
            elif self.image.endswith(".webp"):
                formatType = "image/webp"

            # Encode the image as base64
            b64EncodedImage = base64.b64encode(open(self.image, "rb").read())

            # Send the image and text to the Anthropic API
            with self.client.messages.stream(
                model="anthropic.claude-3-sonnet-20240229-v1:0",
                max_tokens=5000,
                messages=[{
                    'role': 'user',
                    'content': [
                        {
                            "type": "image",
                            "source": {
                                "type": "base64",
                                "media_type": formatType,
                                "data": b64EncodedImage.decode("utf-8")
                            }
                        },
                        {
                            "type": "text",
                            "text": self.text
                        }
                    ]
                }]
            ) as stream:
                for text in stream.text_stream:
                    yield text
        else:
            # Send the text to the Anthropic API
            with self.client.messages.stream(
                model="anthropic.claude-3-sonnet-20240229-v1:0",
                max_tokens=5000,
                messages=[{
                    'role': 'user',
                    'content': self.text
                }]
            ) as stream:
                for text in stream.text_stream:
                    yield text

# MultimodalInputHandler = MultimodalInputHandler("What is this image?", "path/to/my/file")
# print(MultimodalInputHandler.handleInput())