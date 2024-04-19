import json
from typing import Any, Dict, List, Optional

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM


class AilyLLM(LLM):
    user_access_token: str
    app_id: str
    skill_id: Optional[str]
    skill_input: Optional[dict]

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        from aily.openapi.assistant.beta import AssistantClient

        client = AssistantClient()
        client.use_user_access_token(self.user_access_token)
        kwargs = {
            "app_id": self.app_id,
            "content": prompt,
        }
        if self.skill_id:
            kwargs['skill_id'] = self.skill_id
            if self.skill_input:
                kwargs['skill_input'] = json.dumps(self.skill_input)

        message = client.chat_completions.create(**kwargs)
        return message.content

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Return a dictionary of identifying parameters."""
        return {
            "model_name": "AilyOpenAPIModel",
        }

    @property
    def _llm_type(self) -> str:
        """Get the type of language model used by this chat model. Used for logging purposes only."""
        return "aily-openapi"

