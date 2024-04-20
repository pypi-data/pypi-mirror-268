#!/usr/bin/env python
import sys
import os
import requests
import json
import pathlib
import re

def get_response(
    user_access_token,
    message_thread,
    maxTokens=256,
    temperature=1.0,
    frequencyPenalty=0,
    presencePenalty=0,
):
    """
    Function to get a response from the OpenAI API, given a message thread.

    Args:
    message_thread (list of dict): A list of messages, each containing a role and a content field.
    maxTokens (int): The maximum number of tokens to generate.
    temperature (float): The sampling temperature.
    frequencyPenalty (float): Proportional penalty to the appearance of already generated tokens.
    presencePenalty (float): Flat penalty to the appearance of already generated tokens.

    Returns:
    str: The response from the OpenAI API.
    """
    # If the message thread is empty, return an empty string
    if len(message_thread) == 0:
        raise ValueError("Message thread is empty")

    # If the message thread is not empty, make a request to the OpenAI API
    url = "https://api.openai.com/v1/chat/completions"
    model = "gpt-3.5-turbo"

    # Make the request with timeout
    response = requests.post(
        url,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {user_access_token}",
        },
        data=json.dumps(
            {
                "model": model,
                "messages": message_thread,
                "max_tokens": maxTokens,
                "temperature": temperature,
                "frequency_penalty": frequencyPenalty,
                "presence_penalty": presencePenalty,
            }
        ),
        timeout=10,  # Set the timeout value in seconds
    )

    # Return the response
    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Error: {e}: {repr(e)}")
        print(f"Response: {response.text}")
        return "An error occurred while processing the request."

def thread_add_message(message_content, thread=None):
    """
    Function to append a message to a message thread.
    Message thread is a list of dict, containing some messages assigned to different roles.
    The role of the new message is inferred from the last message in the thread.
    If the thread is empty, the role is assumed to be "system".

    Args:
    message_content (str): The content of the message to be added.
    thread (list of dict): The message thread to which the message should be added.

    Returns:
    list of dict: The updated message thread.
    """
    if thread is None:
        thread = [{"role": "system", "content": message_content}]
    else:
        if thread[-1]["role"] == "system":
            thread.append({"role": "user", "content": message_content})
        elif thread[-1]["role"] == "user":
            thread.append({"role": "assistant", "content": message_content})
        elif thread[-1]["role"] == "assistant":
            thread.append({"role": "user", "content": message_content})
        else:
            raise ValueError("Invalid role in message thread")
    return thread

def filter_output(output_str):
    """
    Filters the output string. For example, code is often enclosed in triple quotes:
    ```programming_language
    some command to execute
    ```
    """
    # Regex to grab the command from the code block
    # Make sure to discard the language part of the code block
    output_str = output_str.strip()
    if "```" in output_str:
        output_str = re.sub(r"```.*\n", "", output_str)
        output_str = output_str.replace("```", "")
    return output_str

def main():
    """
    Main function to run the shell command assistant.
    """
    # Read OpenAI API key from file. First line of file should contain the raw API key.
    package_directory = pathlib.Path(__file__).parent.absolute()
    env_path = package_directory / "openai_api_key.env"
    user_access_token = ""
    try:
        with env_path.open("r") as f:
            lines = f.readlines()
            if lines:
                user_access_token = lines[0].strip()
    except FileNotFoundError:
        print(f"Good-gpt: OpenAI API key file not found at {env_path}")

    # Check for the presence of the OpenAI API key
    if user_access_token == "":
        print("OpenAI API key not found. Please provide a working API key:")
        user_access_token = input().strip()
        system_message = "You respond with pong"
        thread = thread_add_message(system_message)
        thread = thread_add_message("ping", thread)
        try:
            response = get_response(user_access_token, thread)
            assert "pong" in response
        except Exception as e:
            print(f"Error: {e}: {repr(e)}")
            print("Cannot verify the OpenAI API key.")
            return
        else:
            print("OpenAI API key is valid.")
            
            # Save the API key to a file
            with env_path.open("w") as f:
                f.write(user_access_token)
                print(f"OpenAI API key saved to {env_path}")

    # Process the input command
    user_command = " ".join(sys.argv[1:])
    if user_command == "":
        print("No command provided to good-gpt. Returning.")
        return

    # Send the command to the assistant
    system_message = "You are a shell command assistant. A desired command is specified using natural language. You provide directly a corresponding single-line command, raw, without any additional explanation."
    system_message += "# USER_SYSTEM_PLATFORM: " + sys.platform
    thread = thread_add_message(system_message)
    thread = thread_add_message(user_command, thread)
    suggested_command = get_response(user_access_token, thread)

    # Filter the output
    suggested_command = filter_output(suggested_command)

    print(f"Do you want to execute this suggested command for {sys.platform}? [y/n]")
    print(f"--> {suggested_command}")

    try:
        choice = input().lower()
    except (EOFError, KeyboardInterrupt):
        choice = "n"

    if choice in ['y', 'yes', 'ok', 'good', '']:
        # Execute the command for Unix-like systems
        if sys.platform in ["linux", "darwin"]:
            os.system(f"{suggested_command}")
        # For Windows, you might need to adjust commands or use a translation layer
        elif sys.platform == "win32":
            os.system(f"{suggested_command}")
        else:
            print("Unsupported OS.")
    else:
        print(" Command not executed.")

if __name__ == "__main__":
    main()
