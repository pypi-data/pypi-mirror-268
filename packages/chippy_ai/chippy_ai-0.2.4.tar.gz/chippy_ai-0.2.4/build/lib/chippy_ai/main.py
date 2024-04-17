import os
import sys
import textwrap
import subprocess
import configparser
from openai import OpenAI


#old config
# Read configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Configurations for ERROR and QUESTION
ERROR_CONFIG = config['ERROR']
QUESTION_CONFIG = config['QUESTION']
mode = ERROR_CONFIG.get('Default', 'HardcoreMode')
hardcore_mode = config['DEFAULT'].get('Hardcore', 'no').lower()





#test change




#new config
import configparser
import importlib.resources as pkg_resources

def load_configuration():
    # Use the 'open_text' method from 'importlib.resources' to access the 'config.ini' within the package
    with pkg_resources.open_text('chip', 'config.ini') as config_file:
        config = configparser.ConfigParser()
        config.read_file(config_file)
        return config

# Load the configuration when the module is loaded
config = load_configuration()

# Access the specific configuration sections
ERROR_CONFIG = config['ERROR']
QUESTION_CONFIG = config['QUESTION']

# Assuming 'Default' is a section in your config.ini, and 'HardcoreMode' is a key within that section
mode = config.get('Default', 'HardcoreMode', fallback='HardcoreModeDefault')
hardcore_mode = config.get('DEFAULT', 'Hardcore', fallback='no').lower()
















#read .env
from dotenv import load_dotenv
import os

load_dotenv()  # load all the environment variables from a .env file

api_key = os.getenv("TOGETHER_API_KEY")





def format_in_rectangle(text, width=65, color_code='\033[94m'):
    padding = 2
    padded_width = width - 4
    lines = []
    reset_color = '\033[0m'  # Define reset_color at the beginning

    for paragraph in text.split('\n'):
        wrapped_lines = textwrap.wrap(paragraph, width=padded_width)
        lines.extend(wrapped_lines if wrapped_lines else [''])

    top_left = f'{color_code}╭{reset_color}'
    top_right = f'{color_code}╮{reset_color}'
    bottom_left = f'{color_code}╰{reset_color}'
    bottom_right = f'{color_code}╯{reset_color}'
    horizontal = f'{color_code}─{reset_color}'
    reset_color = '\033[0m'

    box = f"{top_left}{horizontal * (width - 2)}{top_right}\n"
    for line in lines:
        box += f"{color_code}│ {line.ljust(padded_width)} │{reset_color}\n"
    box += f"{bottom_left}{horizontal * (width - 2)}{bottom_right}"

    return box

# In the main function, adjust the call to format_in_rectangle
# to pass the preresponse1_color for both text and border.






def get_last_command_and_run(history_file='~/.zsh_history'):
    history_path = os.path.expanduser(history_file)
    last_command = None

    try:
        with open(history_path, 'r', encoding='latin-1', errors='ignore') as file:
            # Reverse read the file to get the last relevant command
            for line in reversed(file.readlines()):
                if 'chip' not in line:
                    # zsh history format: ': [timestamp]:[session];command'
                    # Extracting the actual command part
                    last_command = line.split(';', 1)[-1].strip()
                    if last_command:
                        break

        if not last_command:
            return None, "No valid previous command found."
        #print(format_in_rectangle((f"Chippy is executing the last command: {last_command}")))
        # Execute the last command and capture the output
        result = subprocess.run(last_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        return last_command, result.stdout

    except FileNotFoundError:
        return None, f"History file not found: {history_path}"
    except Exception as e:
        return None, f"Error reading history file: {e}"



def analyze_error(context):
    TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
    if not TOGETHER_API_KEY:
        print("TOGETHER_API_KEY environment variable is not set")
        sys.exit(1)

    client = OpenAI(
        api_key=TOGETHER_API_KEY,
        base_url='https://api.together.xyz/v1',
    )
    model = ERROR_CONFIG.get('Model', 'default_model')
    detailed_response_length = int(ERROR_CONFIG.get('ResponseLength', 100))

    # Detailed error analysis
    detailed_prompt = f"Context: \n{context}\nWhat could be the reason for the error? Simplify the explanation."
    detailed_analysis = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an expert and technically adept at analyzing errors and suggesting fixes. If the user appears to be mistyping common terminal commands, suggest commands that might be the correct option"},
            {"role": "user", "content": detailed_prompt}
        ],
        model=model,
        max_tokens=detailed_response_length
    ).choices[0].message.content.strip()

    # Enhance context with the detailed analysis for the pre-responses
    enhanced_context = f"{context}\n\nDetailed Analysis: {detailed_analysis}"

    # Initial error check with structured prompt
    initial_prompt = "Based on the enhanced context and detailed analysis, is this an error? Respond with 'Yes' or 'No' only."
    preresponse1 = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Based on the analysis, respond with 'Yes' or 'No' only."},
            {"role": "user", "content": enhanced_context+initial_prompt}
        ],
        model=model,
        max_tokens=1
    ).choices[0].message.content.strip()

    # Error type determination
    preresponse2 = "N/A"
    if preresponse1.lower() == 'yes':
        type_prompt = "Return Error type. NOTHING ELSE."
        preresponse2 = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Provide just the error type. DO NOT WRITE A SENTENCE"},
                {"role": "user", "content": enhanced_context+type_prompt}
            ],
            model=model,
            max_tokens=6
        ).choices[0].message.content.strip()

    return preresponse1, preresponse2, detailed_analysis





def ask_gpt(question):
    TOGETHER_API_KEY = os.environ.get("TOGETHER_API_KEY")
    if not TOGETHER_API_KEY:
        print("TOGETHER_API_KEY environment variable is not set")
        sys.exit(1)

    client = OpenAI(
        api_key=TOGETHER_API_KEY,
        base_url='https://api.together.xyz/v1',
    )
    model = QUESTION_CONFIG.get('Model', 'default_model')
    max_tokens = int(QUESTION_CONFIG.get('ResponseLength', 200))  # Default to 200 if not set

    formatted_question = f"You are an expert developer. {question} Be concise and clear."
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": formatted_question,
            }
        ],
        model=model,
        max_tokens=max_tokens
    )
    return chat_completion.choices[0].message.content



def read_shell_file():
    try:
        with open('shell.txt', 'r') as file:
            shell_content = file.read()
            return shell_content
    except FileNotFoundError:
        print("File not found: shell.txt")
    except Exception as e:
        print(f"Error reading file: {e}")

def read_git_file():
    try:
        with open('git.txt', 'r') as file:
            git_content = file.read()
            return git_content
            #formatted_content = format_in_rectangle(content)
            #print(formatted_content)
    except FileNotFoundError:
        print("File not found: shell.txt")
    except Exception as e:
        print(f"Error reading file: {e}")

def main():
    red_color_code = '\033[91m'  # ANSI color code for red
    green_color_code = '\033[92m'  # ANSI color code for green
    reset_color = '\033[0m'  # Resets the color to default
    if hardcore_mode.lower() != 'yes':
        if len(sys.argv) > 1:
            if sys.argv[1] == "error":
                command, output = get_last_command_and_run()
                if not command:
                    print(format_in_rectangle(output))
                    return
                
                context = f"Last command: {command}\nOutput:\n{output}"
                commander = f"Chippy is executing the last command: {command}"
                command_color = '\033[36m'  # light blue
                print(format_in_rectangle(commander, color_code=command_color))


                preresponse1, preresponse2, detailed_analysis = analyze_error(context)
                
                if preresponse1.lower() == 'yes':
                    preresponse1_color = '\033[91m'  # red
                else:
                    preresponse1_color = '\033[92m'  # green

                # Then, use this color when calling format_in_rectangle
                initial_analysis_output = f"Error detected: {preresponse1}\nType: {preresponse2}"
                print(format_in_rectangle(initial_analysis_output, color_code=preresponse1_color))
                #if detailed_analysis:
                if preresponse1.lower() == 'yes':
                    print(format_in_rectangle("△ Chippy Detailed Error Analysis △"))
                    print(format_in_rectangle(detailed_analysis))
            elif sys.argv[1] == "shell":
                text = read_shell_file()
                print(format_in_rectangle(text))
            elif sys.argv[1] == "git":
                text = read_git_file()
                print(format_in_rectangle(text))
            elif sys.argv[1] == "-q" and len(sys.argv) > 2:
                question = " ".join(sys.argv[2:])
                answer = ask_gpt(question)
                print(format_in_rectangle("△ Chippy Q&A △"))
                print(format_in_rectangle(f"Q: {question}\n\nA: {answer}"))
            else:
                print(format_in_rectangle("Usage: chip error"))
                print(format_in_rectangle("or: chip -q <question>"))
                print(format_in_rectangle("or: chip shell"))
                print(format_in_rectangle("or: chip git"))
        else:
            print(format_in_rectangle("Usage: chip error"))
            print(format_in_rectangle("or: chip -q <question>"))
            print(format_in_rectangle("or: chip shell"))
            print(format_in_rectangle("or: chip git"))
    else:
        if hardcore_mode.lower() == 'yes':
            if len(sys.argv) > 1:
                if sys.argv[1] == "error":
                    command, output = get_last_command_and_run()
                    if not command:
                        print(output)
                        return
                    
                    context = f"Last command: {command}\nOutput:\n{output}"
                    commander = f"Chippy is executing the last command: {command}"
                    command_color = '\033[36m'  # light blue
                    print(commander)
                    preresponse1, preresponse2, detailed_analysis = analyze_error(context)         
                    initial_analysis_output = f"Error detected: {preresponse1}\nType: {preresponse2}"
                    print(initial_analysis_output)
                    #if detailed_analysis:
                    if preresponse1.lower() == 'yes':
                        print("△ Chippy Detailed Error Analysis △")
                        print(detailed_analysis)
                elif sys.argv[1] == "shell":
                    text = read_shell_file()
                    print(text)
                elif sys.argv[1] == "git":
                    text = read_git_file()
                    print(text)
                elif sys.argv[1] == "-q" and len(sys.argv) > 2:
                    question = " ".join(sys.argv[2:])
                    answer = ask_gpt(question)
                    print("△ Chippy Q&A △")
                    print(f"Q: {question}\n\nA: {answer}")
                else:
                    print("Usage: chip error")
                    print("or: chip -q <question>")
                    print("or: chip shell")
                    print("or: chip git")
            else:
                print("Usage: chip error")
                print("or: chip -q <question>")
                print("or: chip shell")
                print("or: chip git")


if __name__ == "__main__":
    main()