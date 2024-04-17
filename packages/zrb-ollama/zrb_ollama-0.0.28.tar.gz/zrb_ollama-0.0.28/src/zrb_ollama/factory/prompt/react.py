import os
from langchain.prompts import PromptTemplate
from langchain_core.prompts import BasePromptTemplate

from ...config import SYSTEM_PROMPT
from ...task.any_prompt_task import AnyPromptTask
from ..schema import PromptFactory


def react_prompt_factory(system_prompt: str = SYSTEM_PROMPT) -> PromptFactory:
    current_dir = os.path.dirname(__file__)
    with open(os.path.join(current_dir, "react-prompt.txt"), "r") as f:
        react_prompt = f.read()

    def create_prompt(task: AnyPromptTask) -> BasePromptTemplate:
        return PromptTemplate.from_template(
            "\n".join([
                task.render_str(system_prompt),
                "",
                react_prompt,
            ])
        )

    return create_prompt
