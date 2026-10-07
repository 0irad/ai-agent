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
            return f'Success: "{directory}" is within the working directory'
    except Exception as e:
        return f"Error: {e}"
