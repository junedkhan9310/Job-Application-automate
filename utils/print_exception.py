import time
import sys
import os 
from datetime import datetime


def print_exception_details(e):
    exc_type, exc_obj, exc_tb = sys.exc_info()
    # Extract relevant information
    Exception_Type = exc_type.__name__
    Line_No = exc_tb.tb_lineno
    Error_Message = str(e)
    if '(Session info:' in Error_Message:
        Error_Message = Error_Message.partition('(Session info:')[0].strip()
    Error_Message = Error_Message.replace('\n',', ')
    Function_name = exc_tb.tb_frame.f_code.co_name
    File_Name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    Timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Timestamp of the error occurrence
    # Construct the error message with all relevant details
    Error_Final = (
        f"Timestamp: {Timestamp} | Error_Message: {Error_Message} | "
        f"Function: {Function_name} | Exception_Type: {Exception_Type} | "
        f"File_Name: {File_Name} | Line_No: {Line_No} "
    )
    # Print the error message
    print(Error_Final)
    # Optionally, sleep to allow for error inspection (can be removed if not needed)
    time.sleep(10)