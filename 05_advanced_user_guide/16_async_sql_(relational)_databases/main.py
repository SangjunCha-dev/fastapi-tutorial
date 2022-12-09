from fastapi import FastAPI

from database import database, notes
from schemas import Note, NoteIn

app = FastAPI()


# Connect and disconnect
@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# Read notes
@app.get("/notes/", response_model=list[Note])
async def read_notes():
    query = notes.select()
    return await database.fetch_all(query)


# Create notes
@app.post("/notes/", response_model=Note)
async def create_note(note: NoteIn):
    query = notes.insert().values(text=note.text, completed=note.completed)
    last_record_id = await database.execute(query)
    return {
        **note.dict(),
        "id": last_record_id,
    }
