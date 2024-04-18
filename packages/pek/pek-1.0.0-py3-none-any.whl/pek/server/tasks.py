import uuid
from abc import ABC
from enum import Enum

from ..clustering import ProgressiveEnsembleKMeansProcess


class TaskStatus(Enum):
    pending = "pending"
    running = "running"
    paused = "paused"
    killed = "killed"
    completed = "completed"


class Task:
    def __init__(self, queue, taskId=None):
        self.id = str(uuid.uuid4()) if taskId is None else taskId
        self.queue = queue
        self.status = TaskStatus.pending

        self.args = None
        self.process = None

    def start(self, args):
        if self.status != TaskStatus.pending:
            raise RuntimeError(f"Task {self.id} has already been started.")
        self.args = args
        self.process = ProgressiveEnsembleKMeansProcess(resultsQueue=self.queue, **self.args)
        self.process.start()
        self.status = TaskStatus.running

    def pause(self):
        if self.status != TaskStatus.running:
            raise RuntimeError(f"Task {self.id} is not running.")
        self.process.pause()
        self.status = TaskStatus.paused

    def resume(self):
        if self.status != TaskStatus.paused:
            raise RuntimeError(f"Task {self.id} is not paused.")
        self.process.resume()
        self.status = TaskStatus.running

    def kill(self):
        if self.status != TaskStatus.running:
            raise RuntimeError(f"Task {self.id} is not running.")
        self.process.kill()
        self.status = TaskStatus.killed

    def killRun(self, runId):
        if self.status != TaskStatus.running:
            raise RuntimeError(f"Task {self.id} is not running.")
        self.process.killRun(runId)


"""class ProgressiveEnsembleKMeansTask(_Task):
    def __init__(self, args, queue):
        super().__init__(queue)
        args["resultsQueue"] = queue
        args["id"] = self.id
        self.process = ProgressiveEnsembleKMeansProcess(**args)

    def killRun(self, runId):
        if self.status != TaskStatus.running:
            raise RuntimeError(f"Task {self.id} is not running.")
        self.process.killRun(runId)"""
