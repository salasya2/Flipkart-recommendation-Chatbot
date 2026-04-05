import sys

class CustomException(Exception):

    def __init__(self,message:str,error_detail:Exception):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)
    
    @staticmethod
    def get_detailed_error_message(message,error_detail):
        _,_,exc_tb = sys.exc_info()

        filename = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknow File name"
        linenumber = exc_tb.tb_lineno if exc_tb else "Unknown Line no"

        return  f"{message} | Error_detail : {error_detail} | file name : {filename} | line number : {linenumber}"
    
    def __str__(self):
        return self.error_message
