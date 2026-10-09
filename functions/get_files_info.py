import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        wd_full_path = os.path.abspath(working_directory)
        dir_full_path = os.path.join(wd_full_path, directory)
        target_dir = os.path.normpath(dir_full_path)
        valid_target_dir = (
            os.path.commonpath([wd_full_path, target_dir]) == wd_full_path
        )
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        else:
            stats = ""
            for rel_path in os.listdir(target_dir):
                abs_path = os.path.join(target_dir, rel_path)
                stats += f"- {rel_path}: file_size={os.path.getsize(abs_path)} bytes, is_dir={os.path.isdir(abs_path)}\n"
            return stats
    except Exception as e:
        return f"Error: {e}"

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}
