from typing import Union

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


# Import File
@app.post("/files/")
def create_file(file: bytes = File()):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# Optional File Upload
@app.post("/files2/")
def create_file2(file: Union[bytes, None] = File(default=None)):
    if file:
        return {"file_size": len(file)}
    else:
        return {"message": "No file sent"}


@app.post("/uploadfile2/")
def create_upload_file2(file: Union[UploadFile, None] = None):
    if file:
        return {"filename": file.filename}
    else:
        return {"message": "No upload file sent"}


# UploadFile with Additional Metadata
@app.post("/files3/")
def create_file3(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/uploadfile3/")
def create_upload_file3(
    file: UploadFile = File(description="A file read as UploadFile"),
):
    return {"filename": file.filename}


# Multiple File Uploads
@app.post("/files4/")
def create_files4(files: list[bytes] = File()):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles4/")
def create_upload_files4(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


@app.get("/4")
def main4():
    content = """
        <body>
        <form action="/files4/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        <form action="/uploadfiles4/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)


# Multiple File Uploads with Additional Metadata
@app.post("/files5/")
def create_files5(
    files: list[bytes] = File(description="Multiple files as bytes"),
):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/uploadfiles5/")
def create_upload_files5(
    files: list[UploadFile] = File(description="Multiple files as UploadFile"),
):
    return {"filenames": [file.filename for file in files]}


@app.get("/5")
def main5():
    content = """
        <body>
        <form action="/files5/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        <form action="/uploadfiles5/" enctype="multipart/form-data" method="post">
            <input name="files" type="file" multiple>
            <input type="submit">
        </form>
        </body>
    """
    return HTMLResponse(content=content)
