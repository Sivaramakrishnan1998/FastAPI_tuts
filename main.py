from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
from ml import nlp

app = FastAPI()

@app.get('/')
def read_main():
    return {"message":"hello world"}

class Article(BaseModel):
    content:str
    comment:List[str]=[]

@app.post('/article/')
def display_main(articles:List[Article]):
    ents = []
    comments = []
    for article in articles:
        for comment in article.comment:
            comments.append(comment.    upper())

        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text" : ent.text, "label": ent.label_})

    return {
        "comments": comments,
        "entities": ents
    }