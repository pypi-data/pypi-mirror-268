import uvicorn
import os
from fastapi import BackgroundTasks, FastAPI
from dbt.cli.main import dbtRunner, dbtRunnerResult
from pydantic import BaseModel
import multiprocessing

app = FastAPI()

class DbtRunConfig(BaseModel):
    cmd: str
    # Here we should define a object with usefull propoerties. like profile, parameters, tags, what else?

    def prepare_command(self):
        return self.cmd.split(" ")[1:] # handle parameters, tags etc... 


def dbt_task(cmd_list):
    dbt = dbtRunner()
    dbt.invoke(cmd_list)
    # check if we can configure hooks/callbacks which call our @app.post('/callback') endpiont


def run_dbt(runConfig: DbtRunConfig):
    cmd = runConfig.prepare_command()
    proc = multiprocessing.Process(
        target=dbt_task,
        args=(cmd,))
    proc.start()
    
    return { 'pid' : proc.pid }


@app.get('/callback')
def root():
    return {'message': 'This endpoint works!'}


@app.post("/dbt")
async def run_dbt_command_endpoint(runConfig: DbtRunConfig, background_tasks: BackgroundTasks):
    return run_dbt(runConfig)