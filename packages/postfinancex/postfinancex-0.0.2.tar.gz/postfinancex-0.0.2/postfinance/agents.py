import pathlib
from typing import Any, Dict, Optional

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from .models import TaskTypes, get_model
from .output_parsers import get_output_parser, transcript_json_input_parser
from .prompts import get_prompt


def do(
    task: str | TaskTypes,
    api_key: str,
    model: str = "mistralai/mixtral-8x7b-instruct-v01",
    params: Optional[Dict[str, Any]] = None,
    prompt: Optional[str] = None,
    parse: bool = True,
    **kwargs,
) -> dict:
    model = get_model(task, model, params, api_key)
    prompt = prompt or get_prompt(task, **kwargs)
    output = model.generate_text(prompt)
    if parse:
        output_parser = get_output_parser(task)
        output = output_parser(output, dumps=False)
    return output


class Agent(object):

    def __init__(self, api_key: str, storage_uri: str) -> None:
        self.api_key = api_key
        self.storage = MongoClient(storage_uri, server_api=ServerApi("1"))
        self.collection = self.storage["postfinance"]["transcripts"]

    def insert(self, transcript: dict) -> None:
        self.collection.insert_one(transcript)

    def get_by_transcript_id(self, transcript_id: str) -> dict | None:
        return self.collection.find_one({"transcript_id": transcript_id})

    def run(self, direcory: str = "data/transcripts") -> None:
        for markdown in pathlib.Path(direcory).iterdir():
            transcript_id = markdown.stem
            if self.get_by_transcript_id(transcript_id):
                continue
            record = {
                "transcript_id": transcript_id,
            }
            with open(markdown, "r") as file:
                transcript = file.read()
            input = transcript_json_input_parser(transcript)
            record.update(input)
            output = self.translate(content=transcript)
            record.update(output)
            translation = output["translation"]["markdown"]
            output = self.annotate(content=translation)
            record.update(output)
            self.insert(record)

    def translate(
        self,
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        prompt: Optional[str] = None,
        parse: bool = True,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.TRANSLATION,
            self.api_key,
            model=model,
            params=params,
            prompt=prompt,
            parse=parse,
            **kwargs,
        )

    def annotate(
        self,
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        prompt: Optional[str] = None,
        parse: bool = True,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.ANNOTATION,
            self.api_key,
            model=model,
            params=params,
            prompt=prompt,
            parse=parse,
            **kwargs,
        )

    def chat(
        self,
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        prompt: Optional[str] = None,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.CHAT,
            self.api_key,
            model=model,
            params=params,
            prompt=prompt,
            parse=False,
            **kwargs,
        )
