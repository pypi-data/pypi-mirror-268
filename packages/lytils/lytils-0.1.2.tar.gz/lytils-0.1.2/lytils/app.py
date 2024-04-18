import subprocess
from .input import cinput
from .print import cprint


def kill_process(process_name):
    try:
        subprocess.run(
            ["taskkill", "/F", "/IM", process_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        cprint(f'<g>Terminated process "{process_name}"')
    except subprocess.CalledProcessError as e:
        cprint(f'<r>Error: "{e}"')
        cprint(f'<y>Failed to terminate process "{process_name}"')
        if "Access is denied." in e.stderr.decode("utf-8"):
            cprint("<y>Access was denied. Try running with admin privileges.")
            raise
        else:
            cprint(f"<y>Process potentially not found.")


def start_process(process_path):
    try:
        # Redirect standard output and standard error to subprocess.PIPE to suppress logs
        subprocess.Popen(
            process_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            shell=True,  # Use shell=True for Windows paths
        )
        cprint(f'<g>Started process "{process_path}"')
    except FileNotFoundError:
        cprint(f"<r>Failed to start process.")
        cprint(f"<y>File not found at path: {process_path}")
    except Exception as e:
        cprint(f"<r>An error occurred: {e}")


# Return true if process is running, else return false
def is_process_running(process_name):
    try:
        # Run the tasklist command and search for the process name
        output = subprocess.check_output(["tasklist"], text=True)
        # Check if the process name is in the output
        return process_name in output
    except subprocess.CalledProcessError:
        return False


# Function to stop a Windows service
def kill_service(service_name):
    try:
        subprocess.run(
            ["net", "stop", service_name], stderr=subprocess.PIPE, check=True
        )
        cprint(f'<g>Stopped the service "{service_name}".')
    except subprocess.CalledProcessError as e:
        cprint(f'<r>Error: "{e}"')
        cprint(f'<y>Failed to terminate service "{service_name}"')
        if "Access is denied." in e.stderr.decode("utf-8"):
            cprint("<y>Access was denied. Try running with admin privileges.")
            raise
        else:
            cprint(f"<y>Service potentially not found.")


# Function to start a Windows service
def start_service(service_name):
    try:
        subprocess.run(["net", "start", service_name], check=True)
        cprint(f'<g>Started the service "{service_name}".')
    except subprocess.CalledProcessError as e:
        cprint(f"<r>Error starting the service: {e}")
