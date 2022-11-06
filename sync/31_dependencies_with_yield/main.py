from fastapi import Depends


# A database dependency with yield
# A dependency with yield and try
def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()


# Sub-dependencies with yield
def dependency_a():
    dep_a = generate_dep_a()
    try:
        yield dep_a
    finally:
        dep_a.close()


def dependency_b(dep_a=Depends(dependency_a)):
    dep_b = generate_dep_b()
    try:
        yield dep_b
    finally:
        dep_b.close(dep_a)


def dependency_c(dep_b=Depends(dependency_b)):
    dep_c = generate_dep_c()
    try:
        yield dep_c
    finally:
        dep_c.close(dep_b)


# Using context managers in dependencies with yield
class MySuperContextManager:
    def __init__(self):
        self.db = DBSession()
    
    def __enter__(self):
        return self.db
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db():
    with MySuperContextManager() as db:
        yield db
