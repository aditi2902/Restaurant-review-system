import pandas as pd
from langchain_core.documents import Document

def load_reviews(csv_path):
    df=pd.read_csv(csv_path)
    docs=[]

    for _,row in df.iterrows():

        content=f"""
        Restaurant Review
        Title: {row['Title']}
        Rating: {row['Rating']}
        Review: {row['Review']}
        """

        docs.append(Document(page_content=content,
                    metadata={
                    "date": row["Date"]
                }
        ))  
    return docs