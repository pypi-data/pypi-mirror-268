import os
import datetime


def log_message(filename: str, log_type: str, message: str):
    """
    Function for logging messages to a text file.
    :param filename: Name of log file or auto
    :param log_type: Type of log (info, error, warning, etc.)
    :param message: Message to be logged
    :return: None

    Example of use:
    log_message("logfile", "info", "This is an information message.")
    log_message("logfile", "error", "This is an error message.")

    If the file does not exist, it will be created. Otherwise, the message will be added to the end of the file.
    """
    timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if filename == "auto":
        filename = f"log_{datetime.datetime.now().strftime('%d%m%Y_%H%M%S')}"
    try:
        if not os.path.exists(filename + ".txt"):
            with open(filename + ".txt", "w") as file:
                file.write(f"[{timestamp}] [{log_type.upper()}] {message}\n")
        else:
            with open(filename + ".txt", "a") as file:
                file.write(f"\n[{timestamp}] [{log_type.upper()}] {message}")
    except Exception as e:
        raise Exception(f"Error occurred while logging: {e}")
