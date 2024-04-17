# Meet Chippy

![License](https://img.shields.io/badge/license-MIT-green.svg)
![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)
![Platform](https://img.shields.io/badge/platform-ZSH%20|%20Bash-lightgrey.svg)

<p align="center">
  <img src="images/chip1.png" width="250px">
</p>

Chippy serves as your command-line companion, offering quick fixes, error analyses, and cheat sheets directly in your terminal environment. It bridges the gap between encountering an error and finding the solution, saving you the hassle of manual searches or sifting through documentation. To make things easier, Chippy goes by their nickname `chip` in the commmand line.

Gif placeholder

## Features

- **Error Analysis**: Understand and fix common programming errors with detailed, context-aware suggestions.
- **Cheat Sheets**: Instant access to condensed, essential commands for Shell, Git, Python, JavaScript, and more.
- **Model Testing**: Experiment with various language models to find the one that best suits your needs.
- **Customizable Appearance**: Choose from default themes or customize the colors to match your style.
- **Environment and Configuration Management**: Easily manage your settings and environmental variables to streamline your workflow.
- **Local and Remote Model Support**: Whether you prefer cloud-based solutions or local installations, Chippy adapts to your setup.

## Quick Start

1. **Installation**

    Install Chippy using pip:
    ```bash
    pip install chippy
    ```

    Install Chippy using Homebrew:
    ```bash
    brew install chippy
    ```

2. **Configuration**

    Set up your together.ai key:
    - Save API keys in your environment variables for secure access.
    - Enter keys via command ```bash chip api "YOUR_KEY_HERE"``` 
    - or via the `config.ini` file
    - Configure Chippy to your liking through the `config.ini` file or via command-line options.

3. **Usage**


    **Error Analysis**
    Encounter an error? Let chippy do the initial diagnosis!
    
    >It is important to note the program captures the error by rerunning the last terminal command. This operation is not reccomendable if the compile/runtime? is long or costly.


    `input`
    ```bash
    chip error
    ```

    
    `output`
    ```txt
    ╭───────────────────────────────────────────────────────────────╮
    │ Chippy is executing the last command: list                    │
    ╰───────────────────────────────────────────────────────────────╯
    ╭───────────────────────────────────────────────────────────────╮
    │ Error detected: Yes                                           │
    │ Type: CommandNotFoundError | NoSuch                           │
    ╰───────────────────────────────────────────────────────────────╯
    ╭───────────────────────────────────────────────────────────────╮
    │ △ Chippy Detailed Error Analysis △                            │
    ╰───────────────────────────────────────────────────────────────╯
    ╭───────────────────────────────────────────────────────────────╮
    │ The error message "command not found" typically means that    │
    │ the command you entered cannot be located in your system's    │
    │ PATH. In this case, "list" is not a recognized command in     │
    │ your current shell environment.                               │
    │                                                               │
    │ A more common command that serves a similar purpose is "ls",  │
    │ which is used to list the contents of a directory. It's       │
    │ possible that the user may have accidentally typed "list"     │
    │ instead of "ls".                                              │
    ╰───────────────────────────────────────────────────────────────╯
    ```

    **Q&A**
    Have a quick question? Too lazy to switch windows? Chippy can easily answer any of programming questions straight from the commandline.
        
    ```bash
    chip -q "how do I convert an integer to a string in python?"
    ```


    ```txt
    ╭───────────────────────────────────────────────────────────────╮
    │ △ Chippy Q&A △                                                │
    ╰───────────────────────────────────────────────────────────────╯
    ╭───────────────────────────────────────────────────────────────╮
    │ Q: how do I convert an integer to a string in python?         │
    │                                                               │
    │ A:  In Python, you can convert an integer to a string using   │
    │ the `str()` function. Here's an example:                      │
    │ ```python                                                     │
    │ num = 123                                                     │
    │ num_str = str(num)                                            │
    │ print(type(num_str))  # <class 'str'>                         │
    │ ```                                                           │
    │ In this example, the integer `123` is converted to a string   │
    │ `'123'` using the `str()` function. The `type()` function is  │
    │ then used to confirm that the result is indeed a string.      │
    ╰───────────────────────────────────────────────────────────────╯
     ```

     **Cheatsheets**
    Forget a basic command? Chippy has you covered with cheatsheets for shell commands, git, python, and javascript
        
    ```bash
    chip git
    ```

   ```txt
    ╭───────────────────────────────────────────────────────────────╮
    │ git init - Initialize a new git repository.                   │
    │ $ git init                                                    │
    │                                                               │
    │ git clone - Clone a repository into a new directory.          │
    │ $ git clone https://github.com/user/repo.git                  │
    │                                                               │
    │ git add - Add file contents to the index.                     │
    │ $ git add .                                                   │
    │                                                               │
    │                           ....                                │
    ╰───────────────────────────────────────────────────────────────╯
    ```

## Roadmap
- Bash/Windows support - currently optimized for ZSH on mac
- Modular LLM support - switch between local and other hosted models
- Opt-in perpetual logging - always-on terminal logging unlocks new debugging potential
- Adding files/functions into context from error message
- Internet connectivity


## Background and Rationale

Why Chippy? In a world where quick access to information is crucial, Chippy aims to reduce the friction experienced by programmers when switching context between coding and searching for solutions or command syntax.

Read more about the development and philosophy behind Chippy in our blog posts:
- [Introducing Chippy: Your CLI Sidekick](https://chippy.io/blog/introducing-chippy)
- [How Chippy Simplifies Programming Workflow](https://chippy.io/blog/simplifying-workflow)

## Community and Contributions

Join our community on [Discord](https://chippy.io/discord) to discuss features, share feedback, and help shape the future of Chippy.

Interested in contributing? Check out our [contribution guidelines](https://chippy.io/contributing).

## License

Chippy is open-source software licensed under the [MIT license](https://chippy.io/license).

---

<p align="center">
  <img src="images/chip2.png" width="100px">
</p>

> "Chippy: the friendly CLI assistant, because even small seconds saved make a big difference."
