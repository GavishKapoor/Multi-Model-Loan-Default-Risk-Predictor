import sys 

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() #exc_info() returns a tuple of three values (type, value, traceback)
    file_name = exc_tb.tb_frame.f_code.co_filename #tb_frame returns the frame object from the traceback object
    error_message = f"Error occured in script: {file_name} line number: {exc_tb.tb_lineno} error message: {str(error)}"
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        return self.error_message
    
    def __repr__(self) -> str:
        return CustomException.__name__.str() + f"({self.error_message})"