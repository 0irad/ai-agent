import os
from config import MAX_CHARS

def get_file_content(working_directory:str, file_path:str) -> str:
    try:
        wd_full_path = os.path.abspath(working_directory)
        file_full_path = os.path.join(wd_full_path, file_path)
        target_path = os.path.normpath(file_full_path)
        valid_target_path = (
            os.path.commonpath([wd_full_path, target_path]) == wd_full_path
        )
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        if not valid_target_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        else:
            with open(target_path, "r") as f:
                content = f.read(MAX_CHARS)
                if f.read(MAX_CHARS + 1):
                    content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return content
                
    except Exception as e:
        return f"Error: {e}"