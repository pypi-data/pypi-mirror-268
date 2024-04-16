import json
import re
from typing import Callable

from .models import TaskTypes

NO_MATCH = "NO MATCH"


def get_output_parser(task: str | TaskTypes) -> Callable:
    if task == TaskTypes.TRANSLATION.value or task == TaskTypes.TRANSLATION:
        return translation_json_output_parser
    if task == TaskTypes.ANNOTATION.value or task == TaskTypes.ANNOTATION:
        return annotation_json_output_parser
    raise ValueError(f'Unsupported task: "{task}"')


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


def _unblock(output: str) -> str:
    # Pattern to find the output enclosed in triple backticks (```)
    pattern = r"```(.*?)```"
    match = re.search(pattern, output, re.DOTALL)
    return match.group(1).strip() if match else NO_MATCH


def _translation_to_markdown(translation: str) -> str:
    return translation


def _translation_markdown_to_text(markdown: str) -> str:
    return _transcript_markdown_to_text(markdown)


def _translation_markdown_to_json(
    markdown: str,
    dumps: bool = False,
) -> dict | str:
    return _transcript_markdown_to_json(markdown, dumps=dumps)


def translation_json_output_parser(
    output: str,
    dumps: bool = False,
) -> dict | str:
    output = _unblock(output)

    # Pattern to find the detected language
    language_pattern = r"Language:\s*(.*?)\s*\n"
    # Pattern to find the translated transcript in English
    translation_pattern = r"Translation:\s*(.*)"

    language_match = re.search(language_pattern, output, re.DOTALL)
    translation_match = re.search(translation_pattern, output, re.DOTALL)

    language = language_match.group(1).strip() if language_match else NO_MATCH
    translation = (
        translation_match.group(1).strip() if translation_match else NO_MATCH
    )

    markdown = _translation_to_markdown(translation)
    data = {
        "language": language,
        "translation": {
            "markdown": markdown,
            "text": _translation_markdown_to_text(markdown),
            "json": _translation_markdown_to_json(markdown),
        },
    }
    return json.dumps(data, indent=4) if dumps else data


def _annotation_block_to_markdown(annotation_block: str) -> str:
    lines = annotation_block.split("\n")
    markdown = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.endswith(":"):
            markdown.append(f"**{line}**\n")
        else:
            citation_match = re.search(r"\((.+?)\)\.", line)
            if citation_match:
                citation = citation_match.group(1).strip()
                # Remove the citation from the original line
                line = line.replace(f" ({citation})", "")
                # Add the line and citation
                markdown.append(f"{line}\n")
                markdown.append(f"> {citation}\n")
            else:
                markdown.append(f"{line}\n")
    return "\n".join(markdown)


def _annotation_to_markdown(annotation: str) -> str:
    return "\n\n\n".join(
        [
            _annotation_block_to_markdown(annotation_block)
            for annotation_block in annotation.split("\n\n")
        ]
    )


def _annotation_to_json(annotation: str, dumps: bool = False) -> dict | str:
    # Pattern to find the customer's request
    request_pattern = r"Customer's Request:\n(.+?)\((.+?)\)\."
    # Pattern to find the Call-Center employee's responses
    responses_pattern = r"Call-Center Employee's Response:\n(.+?)\((.+?)\)\."
    # Pattern to find the customer's question
    question_pattern = r"Customer's Question:\n(.+?)\((.+?)\)\."
    # Pattern to find the Call-Center employee's answers
    answers_pattern = r"Call-Center Employee's Response:\n(.+?)\((.+?)\)\."
    # Pattern to find the customer's problem
    problem_pattern = r"Customer's Problem:\n(.+?)\((.+?)\)\."
    # Pattern to find the Call-Center employee's solutions
    solutions_pattern = r"Call-Center Employee's Response:\n(.+?)\((.+?)\)\."

    requests = re.findall(request_pattern, annotation, re.S)
    responses = re.findall(responses_pattern, annotation, re.S)
    questions = re.findall(question_pattern, annotation, re.S)
    answers = re.findall(answers_pattern, annotation, re.S)
    problems = re.findall(problem_pattern, annotation, re.S)
    solutions = re.findall(solutions_pattern, annotation, re.S)

    request_responding = [
        {
            "request": {
                "summary": req[0].strip(),
                "citation": req[1].strip(),
            },
            "responses": {
                "summary": res[0].strip(),
                "citation": res[1].strip(),
            },
        }
        for req, res in zip(requests, responses)
    ]
    question_answering = [
        {
            "question": {
                "summary": ques[0].strip(),
                "citation": ques[1].strip(),
            },
            "answers": {
                "summary": ans[0].strip(),
                "citation": ans[1].strip(),
            },
        }
        for ques, ans in zip(questions, answers)
    ]
    problem_solving = [
        {
            "problem": {
                "summary": prob[0].strip(),
                "citation": prob[1].strip(),
            },
            "solutions": {
                "summary": sol[0].strip(),
                "citation": sol[1].strip(),
            },
        }
        for prob, sol in zip(problems, solutions)
    ]

    data = {
        "request_responding": request_responding,
        "question_answering": question_answering,
        "problem_solving": problem_solving,
    }
    return json.dumps(data, indent=4) if dumps else data


def annotation_json_output_parser(
    output: str,
    dumps: bool = False,
) -> dict | str:
    output = _unblock(output)

    # Pattern to find the summary
    summary_pattern = r"Summary:\s*(.*?)\s*\n"
    # Pattern to find the customer's requests, questions or problems
    annotation_pattern = r"Customer\'s requests, questions or problems:\s*(.*)"

    summary_match = re.search(summary_pattern, output, re.DOTALL)
    annotation_match = re.search(annotation_pattern, output, re.DOTALL)

    summary = summary_match.group(1).strip() if summary_match else NO_MATCH
    annotation = (
        annotation_match.group(1).strip() if annotation_match else NO_MATCH
    )

    data = {
        "summary": summary,
        "annotation": {
            "markdown": _annotation_to_markdown(annotation),
            "json": _annotation_to_json(annotation),
        },
    }
    return json.dumps(data, indent=4) if dumps else data
