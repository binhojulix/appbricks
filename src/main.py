from src.databricksprop import DataBricksProp
from fastapi import FastAPI
from databricks_cli.runs.api import RunsApi
from databricks_cli.jobs.api import JobsApi
import redis

r = redis.Redis(host="redis123", port=6379)
app = FastAPI()

# import debugpy

# debugpy.listen(("0.0.0.0", 5678))
# print("Waiting for client to attach...")
# debugpy.wait_for_client()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/hits")
def read_root():
    r.set("foo", "bar")
    r.incr("hits")
    return {"Number of hits:": r.get("hits"), "foo": r.get("foo")}


@app.get("/cluster")
def lista_cluster():
    token = DataBricksProp()
    return token.lista_cluster()

def execute_job(self):
    runApi = RunsApi()
    