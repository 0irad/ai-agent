import os
import subprocess


def run_python_file(working_directory:str, file_path:str, args:list[str]|None=None) -> str:
    try:
        wd_full_path = os.path.abspath(working_directory)
        file_full_path = os.path.join(wd_full_path, file_path)
        target_path = os.path.normpath(file_full_path)
        valid_target_path = (
            os.path.commonpath([wd_full_path, target_path]) == wd_full_path
        )
        if not valid_target_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        else: 
            command = ["python", target_path]
            if args:
                command.extend(args)
            command_execution = subprocess.run(
                command,
                cwd=wd_full_path,
                text=True,
                timeout=30,
                capture_output=True
            )
            result = f"Process exited with code {command_execution.returncode}"
            if not command_execution.stderr and not command_execution.stdout:
                result += "\nNo output produced"
            else:
                result += f"\nSTDOUT: {command_execution.stdout}\nSTDERR: {command_execution.stderr}"
            return result

    except Exception as e:
        return f"Error executing python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python file relative to the working directory and returns its exit code, stdout and stderr",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional list of command-line arguments to pass to the Python file",
                },
            },
            "required": ["file_path"],
        },
    },
}
