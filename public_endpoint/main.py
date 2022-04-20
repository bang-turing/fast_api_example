from fastapi import FastAPI

from rest_api import simple_entities_extraction

app = FastAPI()


# @app.on_event("startup")
# async def on_startup():
#     """This function is responsible for load the model and any external connections."""
#     nlp = spacy.load("en_core_web_sm")
#     doc = nlp("COVID has trickled back into China. Beijing is responding with a tsunami of containment measures.")

#     for ent in doc.ents:
#         print(ent.text, ent.label_)
@app.get("/ping")
def pong():
    return {"ping": "pong!"}


app.include_router(simple_entities_extraction.router, tags=["simple_search_entities"])
