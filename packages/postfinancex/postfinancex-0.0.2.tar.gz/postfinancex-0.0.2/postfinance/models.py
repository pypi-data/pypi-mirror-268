from enum import Enum
from typing import Any, Dict, List, Optional

from ibm_watsonx_ai.foundation_models import Model
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames


class TaskTypes(Enum):

    TRANSLATION = "translation"
    ANNOTATION = "annotation"
    CHAT = "chat"


def get_model(
    task: str | TaskTypes,
    model: str,
    params: Optional[Dict[str, Any]] = None,
    api_key: str = "lHMtCMCF5jiwPqgFPeOCDsqoUU4Rm_vIuqSXJmjgIXSQ",
    url: str = "https://us-south.ml.cloud.ibm.com",
    project_id: str = "38a37d7d-4ab7-4349-935c-936add66c7f5",
) -> Model:
    if model not in list_supported_models(task):
        raise ValueError(f'Unsupported model: "{model}" for task "{task}"')
    params = params or get_default_params()
    return Model(
        model_id=model,
        params=params,
        credentials={
            "apikey": api_key,
            "url": url,
        },
        project_id=project_id,
    )


def list_supported_models(task: str | TaskTypes) -> List[str]:
    """List supported models for a specific task.

    Reference:
        [1] https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#ibm_watsonx_ai.foundation_models.utils.enums.ModelTypes
        [2] https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-models.html?context=wx&audience=wdp
    """
    if task == TaskTypes.TRANSLATION.value or task == TaskTypes.TRANSLATION:
        return [
            # "ibm/granite-20b-multilingual",
            "mistralai/mixtral-8x7b-instruct-v01",
            ModelTypes.MIXTRAL_8X7B_INSTRUCT_V01_Q.value,
        ]
    if task == TaskTypes.ANNOTATION.value or task == TaskTypes.ANNOTATION:
        return [
            "mistralai/mixtral-8x7b-instruct-v01",
            ModelTypes.MIXTRAL_8X7B_INSTRUCT_V01_Q.value,
            # ModelTypes.LLAMA_2_70B_CHAT.value,
        ]
    if task == TaskTypes.CHAT.value or task == TaskTypes.CHAT:
        return [
            "mistralai/mixtral-8x7b-instruct-v01",
            ModelTypes.MIXTRAL_8X7B_INSTRUCT_V01_Q.value,
            # ModelTypes.LLAMA_2_70B_CHAT.value,
        ]
    raise ValueError(f'Unsupported task: "{task}"')


def get_default_params() -> Dict[str, Any]:
    """Get default model parameters.

    >>> GenTextParamsMetaNames().show()
    >>> ---------------------  -----  --------
        META_PROP NAME         TYPE   REQUIRED
        DECODING_METHOD        str    N
        LENGTH_PENALTY         dict   N
        TEMPERATURE            float  N
        TOP_P                  float  N
        TOP_K                  int    N
        RANDOM_SEED            int    N
        REPETITION_PENALTY     float  N
        MIN_NEW_TOKENS         int    N
        MAX_NEW_TOKENS         int    N
        STOP_SEQUENCES         list   N
        TIME_LIMIT             int    N
        TRUNCATE_INPUT_TOKENS  int    N
        RETURN_OPTIONS         dict   N
        ---------------------  -----  --------

    Reference:
        [1] https://ibm.github.io/watsonx-ai-python-sdk/fm_model.html#metanames.GenTextParamsMetaNames
        [2] https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/fm-model-parameters.html?context=wx
    """
    return {
        GenTextParamsMetaNames.DECODING_METHOD: "sample",
        GenTextParamsMetaNames.TEMPERATURE: 0.1,
        GenTextParamsMetaNames.TOP_P: 1.0,
        GenTextParamsMetaNames.TOP_K: 50,
        GenTextParamsMetaNames.RANDOM_SEED: 42,
        GenTextParamsMetaNames.REPETITION_PENALTY: 1.0,
        GenTextParamsMetaNames.MIN_NEW_TOKENS: 0,
        GenTextParamsMetaNames.MAX_NEW_TOKENS: 1000,
    }
