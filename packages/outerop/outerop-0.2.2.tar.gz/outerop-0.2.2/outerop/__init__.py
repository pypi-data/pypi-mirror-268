import re
import json
import time
from enum import Enum
from typing import List, Dict, Union
import requests
from openai import OpenAI
import openai
from anthropic import Anthropic
from mistralai.client import MistralClient


# CONSTANTS
DEFAULT_TTL = 15 * 60  # 15 minutes


class Environment(Enum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    STAGING = "staging"


class LogCollector:
    def __init__(self, config: Dict):
        self.config = {**{"isEnabled": True, "baseURL": "https://app.outerop.com"}, **config}
        self.outerop_api_key = config["outeropApiKey"]
        self.bypass_header = config.get("bypassHeader")
        self.pending_flush = False
        self.buffer = []

    @property
    def is_enabled(self):
        return self.config["isEnabled"]

    def record(self, event: Dict):
        prepared_event = self._prepare_event(event)
        self.buffer.append(prepared_event)
        self.flush()

    def flush(self):
        headers = {
            "Content-Type": "application/json",
            "Authorization": self.outerop_api_key,
        }
        if self.bypass_header:
            headers["x-vercel-protection-bypass"] = self.bypass_header

        try:
            response = requests.post(
                f"{self.config['baseURL']}/api/v1/log",
                headers=headers,
                data=json.dumps({ "logs": self.buffer }),
            )
            response.raise_for_status()
        except Exception as e:
            pass
        finally:
            self.pending_flush = False
            self.buffer = []

    def _prepare_event(self, event: Dict):
        return {**event}


class Outerop:
    def __init__(self, outerop_api_key: str, options: Dict = None):
        self.outerop_api_key = outerop_api_key
        self.options = {
            "baseURL": "https://app.outerop.com",
            "loggingEnabled": True,
            "cache": True,
            **(options or {})
        }
        self.log_collector = LogCollector({
            "isEnabled": True,
            "baseURL": self.options.get("baseURL", "https://app.outerop.com"),
            "outeropApiKey": self.outerop_api_key,
            "bypassHeader": self.options.get("bypassHeader")
        })
        self.cache = self.options.get("cache", True)

        headers = {
            "Authorization": self.outerop_api_key,
            "Content-Type": "application/json",
            **({"x-vercel-protection-bypass": self.options["bypassHeader"]} if self.options.get("bypassHeader") else {})
        }

        self.client = requests.Session()
        self.client.headers.update(headers)
        self.client.base_url = self.options["baseURL"]

        self.openai = OpenAI(api_key=self.options["openaiApiKey"]) if self.options.get("openaiApiKey") else None
        self.anthropic = Anthropic(api_key=self.options["anthropicApiKey"]) if self.options.get("anthropicApiKey") else None
        self.mistral = MistralClient(api_key=self.options["mistralApiKey"]) if self.options.get("mistralApiKey") else None

        self.prompt_cache: Dict[str, Dict] = {}
        self.prompt_cache_ttl = options.get("promptCacheTTL", DEFAULT_TTL)  # Default TTL of 15 minutes

    def get_prompt(self, team_prompt_name: str, version_name_or_environment: str):
        cache_key = f"{team_prompt_name}-{version_name_or_environment}"
        current_time = time.time()
        if self.cache and cache_key in self.prompt_cache:
            cached_prompt, timestamp = self.prompt_cache[cache_key]
            if current_time - timestamp < self.prompt_cache_ttl:
                return cached_prompt

        try:
            if version_name_or_environment in [env.value for env in Environment]:
                url = f"{self.options['baseURL']}/api/v1/prompt-by-environment/{team_prompt_name}/{version_name_or_environment}"
            else:
                url = f"{self.options['baseURL']}/api/v1/prompt-by-version-name/{team_prompt_name}/{version_name_or_environment}"

            response = self.client.get(url)
            response.raise_for_status()
            prompt_data = response.json()["prompt"]
            self.prompt_cache[cache_key] = (prompt_data, current_time)  # Update cache with timestamp
            return prompt_data
        except requests.exceptions.RequestException as e:
            status_code = e.response.status_code if e.response else "Unknown"
            response_text = e.response.text if e.response else "Unknown"
            raise Exception(f"Request failed with status code {status_code}: {response_text}")
        except Exception as e:

            raise Exception(f"Request failed: {e}")

        

    def chat(
        self,
        team_prompt_name: str,
        version_name_or_environment: str,
        variables: Dict[str, str]
    ):
        prompt = self.get_prompt(team_prompt_name, version_name_or_environment)
        messages = replace_variables_in_prompts(prompt["messages"], variables)
        messages_without_id = [
            {k: v for k, v in message.items() if k != "id"} for message in messages
        ]

        try:
            tools = prompt["tools"] if prompt["tools"] and len(prompt["tools"]) > 0 else None

            if prompt["model_config"]["provider"] == "groq":
                raise Exception("Groq is not supported yet")

            if prompt["model_config"]["provider"] == "mistral":
                if not self.mistral:
                    raise Exception("Mistral API key is not provided")

                start_time = time.perf_counter()
                result = self.mistral.chat(
                    messages=messages_without_id,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    tools=tools,
                    tool_choice=prompt.get("tool_choice", "auto"),
                )
                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)

                self.log_collector.record(
                    {
                        "team_prompt_id": prompt["team_prompt_id"],
                        "team_prompt_name": team_prompt_name,
                        "version_name": prompt['version_name'],
                        "environment": prompt["environment"],
                        "prompt_environment_id": prompt["id"],
                        "input": messages_without_id,
                        "output": result.choices[0].message.content,
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage.completion_tokens,
                        "input_tokens": result.usage.prompt_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )
                return result

            if prompt["model_config"]["provider"] == "openai":
                if not self.openai:
                    raise Exception("OpenAI API key is not provided")

                start_time = time.perf_counter()
                result = self.openai.chat.completions.create(
                    messages=messages_without_id,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    tools=tools,
                    tool_choice=prompt.get("tool_choice", "auto"),
                )
                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)


                self.log_collector.record(
                    {
                        "team_prompt_id": prompt["team_prompt_id"],
                        "team_prompt_name": team_prompt_name,
                        "version_name": prompt['version_name'],
                        "environment": prompt["environment"],
                        "prompt_environment_id": prompt["id"],
                        "input": messages_without_id,
                        "output": result.choices[0].message.content,
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage.completion_tokens,
                        "input_tokens": result.usage.prompt_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )
                return result

            if prompt["model_config"]["provider"] == "anthropic":
                if not self.anthropic:
                    raise Exception("Anthropic API key is not provided")

                if prompt.get("tool_choice") or prompt.get("tools"):
                    raise Exception("Anthropic tools are not supported yet")

                start_time = time.perf_counter()

                # Extract and combine system prompts in messages into one long string
                system_prompt = "\n".join(
                    [message["content"] for message in messages if message["role"] == "system"]
                )

                # Filter out system messages from the messages list and ensure each message has a 'role' field
                messages_without_system = [
                    {"role": message["role"], "content": message["content"]}
                    for message in messages
                    if message["role"] != "system"
                ]

                result = self.anthropic.messages.create(
                    messages=messages_without_system,
                    model=prompt["model_config"]["model_id"],
                    max_tokens=prompt["max_tokens"],
                    temperature=prompt["temperature"],
                    system=system_prompt,
                )

                end_time = time.perf_counter()
                latency_ms = round((end_time - start_time) * 1000)

                openai_result = convert_anthropic_output_to_openai(result)

                self.log_collector.record(
                    {
                        "team_prompt_id": prompt["team_prompt_id"],
                        "team_prompt_name": team_prompt_name,
                        "version_name": prompt['version_name'],
                        "prompt_environment_id": prompt["id"],
                        "environment": prompt["environment"],
                        "input": messages_without_id,
                        "output": openai_result["choices"][0]["message"]["content"],
                        "latency_ms": latency_ms,
                        "output_tokens": result.usage.output_tokens,
                        "input_tokens": result.usage.input_tokens,
                        "model_config_id": prompt["model_config_id"],
                    }
                )

                return openai_result

        except Exception as e:
            raise Exception(f"Request failed: {e}")

    def ping(self):
        try:
            url = f"{self.options['baseURL']}/ping"
            response = self.client.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            status_code = e.response.status_code if e.response else "Unknown"
            response_text = e.response.text if e.response else "Unknown"
            raise Exception(f"Request failed with status code {status_code}: {response_text}")
        except Exception as e:
            raise Exception(f"Request failed: {e}")

def extract_variables(content: str) -> List[str]:
    return [v.strip() for v in re.findall(r"{{(.*?)}}", content)]

def replace_variables(content: str, variables: Dict[str, str]) -> str:
    def replace_func(match):
        variable_name = match.group(1).strip()
        return variables.get(variable_name, match.group(0))

    return re.sub(r"{{(.*?)}}", replace_func, content)

def replace_variables_in_prompts(
    prompts: List[Dict], variables: Dict[str, str]
) -> List[Dict]:
    return [
        {**prompt, "content": replace_variables(prompt["content"], variables)} for prompt in prompts
    ]

def convert_anthropic_output_to_openai(anthropic_response):
    choices = [
        {
            "message": {"content": choice.text, "role": "assistant"},
            "index": index,
            "finish_reason": "stop",
        }
        for index, choice in enumerate(anthropic_response.content)
    ]

    return {
        "id": anthropic_response.id,
        "created": int(time.time()),
        "model": anthropic_response.model,
        "choices": choices,
        "object": "chat.completion",
        "raw": anthropic_response,
    }