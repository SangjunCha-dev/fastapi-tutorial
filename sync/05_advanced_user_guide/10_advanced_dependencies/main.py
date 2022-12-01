from fastapi import Depends, FastAPI

app = FastAPI()


class FixedContentQueryChecker:
    # Parameterize the instance
    def __init__(self, fixed_content: str):
        self.fixed_content = fixed_content

    # A "callable" instance
    def __call__(self, q: str = ""):
        if q:
            return self.fixed_content in q
        return False


# Create an instance
checker = FixedContentQueryChecker("bar")


# Use the instance as a dependency
@app.get("/query-checker/")
def read_query_check(fixed_content_included: bool = Depends(checker)):
    return {"fixed_content_in_query": fixed_content_included}

