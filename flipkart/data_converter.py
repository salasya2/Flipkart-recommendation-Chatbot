import pandas as pd
from langchain_core.documents import Document

class DataConverter:

    def __init__(self, file_path:str):
        self.file_path = file_path
    
    def convert(self):

        data = pd.read_csv(self.file_path,encoding='utf-8')[['product_title','review']]

        docs =  [
                    Document(page_content = x['review'], meta_data = {"product name " : x['product_title']}) 
                    for _,x in data.iterrows()
                ]
        
        return docs