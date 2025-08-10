from typing_extensions import Literal
import openai
from pydantic import BaseModel
import os
from typing import TypeVar

class VibeisevenResponse(BaseModel):
    result: bool

class VibeisevenRequest(BaseModel):
    value: float




Type = TypeVar("Type", bound=BaseModel)

def viberesponse(
    content: str,
    response_format: Type,
    model = os.environ.get("OPENAI_MODEL", "gpt-4.1-mini")
) -> Type:
    api_key = os.environ["OPENAI_API_KEY"]
    client = openai.OpenAI(api_key=api_key)

    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": content,
                    },
                ],
            }
        ],
        response_format=response_format,
    )
    response_model = response.choices[0].message.parsed
    return response_model


def vibeiseven(value: str | float) -> bool:
    if isinstance(value, str):
        try:
            value = float(value)
        except ValueError:
            raise ValueError("An error has occurred.")
    response = viberesponse(
        content=VibeisevenRequest(value=value).model_dump_json(),
        response_format=VibeisevenResponse,
    )
    return response.result


