import json
import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function
from config import MAX_LLM_ITERATIONS

def main():
    load_dotenv()

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    api_key = os.environ.get("OPENROUTER_API_KEY")

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt}
    ]
    for _ in range(MAX_LLM_ITERATIONS):

        response = client.chat.completions.create(
            model="openrouter/free",
            messages=messages,
            tools=available_functions
        )
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")

        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls:
            for tool_call in message.tool_calls:
                function_args = json.loads(tool_call.function.arguments or "{}")
                print(f"Calling function: {tool_call.function.name}({function_args}) - {tool_call.id}")
                result_message = call_function(tool_call, args.verbose)
                messages.append(result_message)
                if not result_message["content"]:
                    raise Exception("Empty result message content")
                if args.verbose:
                    print(f"-> {result_message['content']}")
        else:
            print(message.content)
            return

     

if __name__ == "__main__":
    main()