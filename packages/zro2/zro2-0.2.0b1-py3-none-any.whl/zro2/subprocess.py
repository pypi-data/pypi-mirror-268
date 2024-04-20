import platform
import subprocess
from typing import List, Union


def exec_command(path: str, *args) -> None:
    """
    Execute a subprocess with the given arguments.

    Args:
        path: The executable path.
        *args: Variable length argument list.

    Returns:
        None
    """
    subprocess.Popen(
        [path, *(str(arg) for arg in args)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        creationflags=(
            subprocess.DETACHED_PROCESS |
            subprocess.CREATE_NEW_PROCESS_GROUP |
            subprocess.CREATE_BREAKAWAY_FROM_JOB
        )
    )

def query_raw(path: str, *args, timeout: int = 5) -> bytes:
    """
    Executes a raw query using the specified arguments and a timeout.

    Args:
        path: The executable path.
        *args: Any additional arguments for the query.
        timeout (int): The maximum time to wait for the query to complete (default is 5).

    Returns:
        bytes: The output of the query execution.
    """
    try:
        command = [path, *(str(arg) for arg in args)]
        proc = subprocess.run(
            command,
            capture_output=True,
            timeout=timeout
        )
        return proc.stdout
    except subprocess.TimeoutExpired as e:
        raise e
    except subprocess.CalledProcessError as e:
        raise e
    
def query(path: str, *args, timeout: int = 5, raw: bool = False, decode_order: List[str] = ["utf-8", "gbk"], to_list: bool = False, strip_null_lines: bool = False) -> Union[str, List[str]]:
    """
    Perform a query with optional parameters for timeout, raw output, return context, decoding order, conversion to list, and stripping null lines.

    Args:
        path: The executable path.
        *args: Variable length argument list.
        timeout (int): Timeout duration in seconds (default is 5).
        raw (bool): Flag to indicate whether to return raw output (default is False).
        decode_order (List[str]): List of encoding orders to decode raw output (default is ["utf-8", "gbk"]).
        to_list (bool): Flag to indicate whether to convert the output to a list (default is False).
        strip_null_lines (bool): Flag to indicate whether to strip null lines from the output (default is False).

    Returns:
        Union[str, List[str]]: The processed query output
    """
    raw_output = query_raw(path, *args, timeout=timeout)
    if raw:
        return raw_output

    for decoder in decode_order:
        try:
            decoded = raw_output.decode(decoder)
            break
        except UnicodeDecodeError:
            continue
    else:
        raise UnicodeDecodeError("Failed to decode output using provided decode orders.")

    if to_list:
        decoded = decoded.strip().split("\r\n")
        if strip_null_lines:
            decoded = [line.strip() for line in decoded if line]

    return decoded

def check_is_installed(app_name):
    """
    Check if an application is installed on the operating system.
    
    Args:
    app_name (str): The name of the application to check.
    
    Returns:
    bool: True if the application is installed, False otherwise.
    """
    os_type = platform.system()

    try:
        if os_type == 'Windows':
            # On Windows, use 'where' command to check for the app existence
            subprocess.check_call(['where', app_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_type == 'Darwin':
            # On macOS, use 'type' command or 'which'
            subprocess.check_call(['type', app_name], shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os_type == 'Linux':
            # On Linux, use 'which' command
            subprocess.check_call(['which', app_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        else:
            return False
    except subprocess.CalledProcessError:
        # The command failed, the application is not installed
        return False

    # The command succeeded, the application is installed
    return True
