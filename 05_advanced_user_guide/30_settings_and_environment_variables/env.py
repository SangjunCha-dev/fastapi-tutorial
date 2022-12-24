# Read env vars in Python
import os

name = os.getenv("MY_NAME", "World")
print(f"Hello {name} from Python")
