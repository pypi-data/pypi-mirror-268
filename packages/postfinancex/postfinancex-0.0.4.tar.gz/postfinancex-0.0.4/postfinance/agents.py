import pathlib
from typing import Any, Dict, List, Optional

from .input_parsers import (
    messages_str_input_parser,
    transcript_json_input_parser,
)
from .models import TaskTypes, get_model
from .output_parsers import get_output_parser
from .prompts import get_prompt


def do(
    task: str | TaskTypes,
    prompt_kwargs: dict,
    api_key: str,
    model: str = "mistralai/mixtral-8x7b-instruct-v01",
    params: Optional[Dict[str, Any]] = None,
    output_parse: bool = True,
    **kwargs,
) -> dict:
    prompt = get_prompt(task, **prompt_kwargs)
    model = get_model(task, model, params, api_key)
    output = model.generate_text(prompt, **kwargs)
    if output_parse:
        output_parser = get_output_parser(task)
        output = output_parser(output, dumps=False)
    return output


class Storage(object):

    def __init__(self, uri: str) -> None:
        try:
            from pymongo import MongoClient
            from pymongo.server_api import ServerApi
        except ImportError as e:
            raise ImportError(
                "The Storage class requires the MongoDB Python Driver to be installed."
                "pip install pymongo[srv]"
            ) from e

        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi("1"))

        # Send a ping to confirm a successful connection
        # Send a ping to confirm a successful connection
        # try:
        #     self.client.admin.command("ping")
        #     print("Pinged your deployment. You successfully connected to MongoDB!")
        # except Exception as e:
        #     raise e

        database_name = "postfinance"
        collection_name = "transcripts"

        self.collection = self.client[database_name][collection_name]

    def insert_transcript(self, transcript: dict) -> None:
        self.collection.insert_one(transcript)

    def get_by_transcript_id(self, transcript_id: str) -> dict | None:
        return self.collection.find_one({"transcript_id": transcript_id})

    def list_transcripts(self) -> List[str]:
        return sorted(
            [
                transcript["transcript_id"]
                for transcript in self.collection.find()
            ]
        )


class Agent(object):

    def __init__(
        self,
        api_key: str,
        storage_uri: Optional[str] = None,
        direcory: str = ".postfinancex/transcripts",
    ) -> None:
        self.api_key = api_key
        self.storage = Storage(storage_uri) if storage_uri else None
        self.direcory = direcory
        self._run()

    def _run(self) -> None:
        """Run the agent to automatically translate and annotate the transcripts
        under the given directory.
        """
        if self.storage is None:
            return
        # TODO: Run a background thread to monitor the directory
        direcory = pathlib.Path(self.direcory)
        direcory.mkdir(parents=True, exist_ok=True)
        for markdown in pathlib.Path(direcory).iterdir():
            transcript_id = markdown.stem
            # Check if exists
            if self.storage.get_by_transcript_id(transcript_id):
                continue
            # Transcript ID
            record = {
                "transcript_id": transcript_id,
            }
            # Transcript
            with open(markdown, "r") as file:
                transcript = file.read()
            input = transcript_json_input_parser(transcript)
            record.update(input)
            # Translation
            output = self.translate(content=transcript)
            record.update(output)
            # Annotation
            output = self.annotate(content=output["translation"]["markdown"])
            record.update(output)
            # Record
            self.storage.insert(record)

    def translate(
        self,
        content: str,
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        output_parse: bool = True,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.TRANSLATION,
            {"content": content},
            api_key=self.api_key,
            model=model,
            params=params,
            output_parse=output_parse,
            **kwargs,
        )

    def annotate(
        self,
        content: str,
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        output_parse: bool = True,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.ANNOTATION,
            {"content": content},
            api_key=self.api_key,
            model=model,
            params=params,
            output_parse=output_parse,
            **kwargs,
        )

    def chat(
        self,
        content: str,
        messages: List[dict],
        model: str = "mistralai/mixtral-8x7b-instruct-v01",
        params: Optional[Dict[str, Any]] = None,
        output_parse: bool = True,
        **kwargs,
    ) -> dict:
        return do(
            TaskTypes.CHAT,
            {
                "content": content,
                "dialogue": messages_str_input_parser(messages),
            },
            api_key=self.api_key,
            model=model,
            params=params,
            output_parse=output_parse,
            **kwargs,
        )
