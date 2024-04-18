from multiprocessing import Process, Queue

from ..utils.process import (
    ProcessControlMessage,
    ProcessControlMessageType,
    ProcessStatus,
)
from .ensemble import ProgressiveEnsembleKMeans


class ProgressiveEnsembleKMeansProcess(Process):
    def __init__(
        self,
        resultsQueue=None,
        **kwargs,
    ):
        super().__init__()

        self._ensemble = ProgressiveEnsembleKMeans(**kwargs)

        self._verbose = False
        self._status = ProcessStatus.PENDING
        self._resultsQueue = resultsQueue
        self._controlsQueue = Queue()

    def _waitForResume(self):
        while True:
            msg = self._controlsQueue.get(block=True)
            if (
                msg.messageType == ProcessControlMessageType.RESUME
                or msg.messageType == ProcessControlMessageType.START
            ):
                self._status = ProcessStatus.RUNNING
                return

    def _readControlMessage(self):
        try:
            msg = self._controlsQueue.get(block=False)
            if msg.messageType == ProcessControlMessageType.PAUSE:
                self._status = ProcessStatus.PAUSED
                self._waitForResume()
            elif msg.messageType == ProcessControlMessageType.KILL_RUN:
                runId = msg.messageData.runId
                self._ensemble.killRun(runId)
            elif msg.messageType == ProcessControlMessageType.KILL:
                self._status = ProcessStatus.KILLED
                self._ensemble.kill()
        except:
            pass

    def run(self):
        self._status = ProcessStatus.RUNNING
        while self._ensemble.hasNextIteration():
            r = self._ensemble.executeNextIteration()
            if self.resultQueue is not None:
                self._resultsQueue.put(r)
            if self._verbose:
                print(r.info)
            if self._ensemble.hasNextIteration():
                self._readControlMessage()
        self._status = ProcessStatus.COMPLETED
        exit()

    @property
    def controlsQueue(self):
        return self._controlsQueue

    @property
    def resultQueue(self):
        return self._resultsQueue

    def pause(self):
        msg = ProcessControlMessage.PAUSE()
        self._controlsQueue.put(msg)

    def resume(self):
        msg = ProcessControlMessage.RESUME()
        self._controlsQueue.put(msg)

    def kill(self):
        msg = ProcessControlMessage.KILL()
        self._controlsQueue.put(msg)

    def killRun(self, runId):
        msg = ProcessControlMessage.KILL_RUN(runId)
        self._controlsQueue.put(msg)
