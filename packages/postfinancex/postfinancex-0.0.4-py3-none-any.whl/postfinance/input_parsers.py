import json
import re
from typing import Dict, List

NO_MATCH = "NO MATCH"

def _transcript_to_markdown(transcript: str) -> str:
    return transcript


def _transcript_markdown_to_text(markdown: str) -> str:
    # Remove Markdown bold formatting with double asterisks (**)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", markdown)
    # Remove empty lines
    text = "\n".join(
        [line.strip() for line in text.split("\n") if line.strip() != ""]
    )
    return text


def _transcript_markdown_to_json(
    markdown: str,
    dumps: bool = False,
) -> dict | str:
    # Pattern to find the title enclosed in double asterisks (**)
    title_pattern = r"\*\*(.*)\*\*\n"
    # Pattern to find the dialogue
    dialogue_pattern = r"\n\*\*(.*?):\*\* \"(.*?)\""

    title_match = re.search(title_pattern, markdown, re.DOTALL)
    dialogue = re.findall(dialogue_pattern, markdown, re.S)

    title = title_match.group(1).strip() if title_match else NO_MATCH
    dialogue = [
        {"role": role.strip(), "content": content.strip()}
        for role, content in dialogue
    ]

    data = {
        "title": title,
        "dialogue": dialogue,
    }
    return json.dumps(data, indent=4) if dumps else data

def transcript_json_input_parser(
    input: str,
    dumps: bool = False,
) -> dict | str:
    markdown = _transcript_to_markdown(input)
    data = {
        "transcript": {
            "markdown": markdown,
            "text": _transcript_markdown_to_text(markdown),
            "json": _transcript_markdown_to_json(markdown),
        },
    }
    return json.dumps(data, indent=4) if dumps else data


def messages_str_input_parser(messages: List[Dict[str, str]]) -> str:
    dialogue = []
    for message in messages:
        if message["content"] == "How could I help you?":
            continue
        if message["role"] == "assistant":
            dialogue.append(f"Assistant: {message["content"]}\n")
        elif message["role"] == "user":
            dialogue.append(f"User: {message["content"]}\n")
        else:
            raise RuntimeError
    return "\n".join(dialogue)
