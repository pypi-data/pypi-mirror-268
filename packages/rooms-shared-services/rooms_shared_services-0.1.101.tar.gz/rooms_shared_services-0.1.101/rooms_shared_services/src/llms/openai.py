import os

from openai import OpenAI
from yaml import load as yaml_load

from rooms_shared_services.src.models.texts.languages import Language
from rooms_shared_services.src.models.texts.variants import TextVariant

try:
    from yaml import CLoader as Loader  # noqa: WPS433
except ImportError:
    from yaml import Loader  # noqa: WPS440, WPS433


class OpenaiQueryClient(object):
    def __init__(self, prompt_filename: str = "rooms_shared_services/src/llms/prompts.yaml"):
        """Set attributes.

        Args:
            prompt_filename (str): _description_. Defaults to "rooms_shared_services/src/llms/prompts.yaml".
        """
        self.openai_client = OpenAI()
        cwd = os.getcwd()
        prompt_full_path = os.path.join(cwd, prompt_filename)
        with open(prompt_full_path) as prompt_obj:
            self.prompt_templates = yaml_load(prompt_obj.read(), Loader=Loader)
            print(self.prompt_templates)

    def retrieve_system_message(self, text_variant: TextVariant):
        for prompt_template in self.prompt_templates["system_messages"]:
            if text_variant.value.lower() in prompt_template["text_variants"]:
                return prompt_template["text"]
        return None

    def request_translation(self, text_variant: TextVariant, text: str, target_language: Language):
        system_message = self.retrieve_system_message(text_variant=text_variant)
        if not system_message:
            raise ValueError("Provided null system message")
        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_message},
                {
                    "role": "user",
                    "content": '"""{}""". This text in triple quotes is a furniture {}. Translate it to {}. Remove any quotes.'.format(
                        text,
                        text_variant.readable,
                        target_language.value,
                    ),
                },
            ],
        )
        return response.choices[0].message.content
