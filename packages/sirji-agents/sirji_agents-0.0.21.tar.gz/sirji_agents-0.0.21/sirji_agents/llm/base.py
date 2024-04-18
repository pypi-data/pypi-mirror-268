from openai import OpenAI
import os

from sirji_messages import AgentSystemPromptFactory, message_parse, MessageParsingError, MessageValidationError
from .model_providers.factory import LLMProviderFactory 

class SingletonMeta(type):
    """Singleton Meta Class for ensuring one instance creation."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class LLMAgentBase(metaclass=SingletonMeta):
    def __init__(self, agent_enum, logger):
        
        self.agent_enum = agent_enum
        self.logger = logger

    def message(self, input_message, history=[]):
        conversation = self.__prepare_conversation(input_message, history)

        self.logger.info(f"Incoming: \n{input_message}")
        self.logger.info("Calling OpenAI Chat Completions API\n")

        response_message, prompt_tokens, completion_tokens = self.__get_response(conversation)

        return response_message, conversation, prompt_tokens, completion_tokens

    def __prepare_conversation(self, input_message, history):
        conversation = []

        if not history:
            prompt_class = AgentSystemPromptFactory[self.agent_enum.name]
            conversation.append(
                {"role": "system", "content": prompt_class().system_prompt()})
        else:
            conversation = history

        parsed_input_message = message_parse(input_message)
        conversation.append({"role": "user", "content": input_message, "parsed_content": parsed_input_message})

        return conversation

    def __get_response(self, conversation):
        
        retry_llm_count = 0
        response_message = ''
        prompt_tokens = 0
        completion_tokens = 0

        while(True):
            response_message, current_prompt_tokens, current_completion_tokens = self.__call_llm(conversation)
            
            prompt_tokens += current_prompt_tokens
            completion_tokens += current_completion_tokens
            try:
                # Attempt parsing
                parsed_response_message = message_parse(response_message)
                conversation.append({"role": "assistant", "content": response_message, "parsed_content": parsed_response_message})
                break
            except (MessageParsingError, MessageValidationError) as e:
            # Handling both MessageParsingError and MessageValidationError similarly
                self.logger.info("Error while parsing the message.\n")
                retry_llm_count += 1
                if retry_llm_count > 2:
                    raise e
                self.logger.info(f"Requesting LLM to resend the message in correct format.\n")
                conversation.append({"role": "assistant", "content": response_message, "parsed_content": {}})
                conversation.append({"role": "user", "content": "The last message was not as per the allowed message formats. Please resend it with proper formatting."})
            except Exception as e:
                self.logger.info(f"Generic error while parsing message. Error: {e}\n")
                raise e
            
            
        return response_message, prompt_tokens, completion_tokens
    
    def __call_llm(self, conversation):
        history = []

        for message in conversation:
            history.append({"role": message['role'], "content": message['content']})

        model_provider = LLMProviderFactory.get_instance()

        return model_provider.get_response(history, self.logger)
