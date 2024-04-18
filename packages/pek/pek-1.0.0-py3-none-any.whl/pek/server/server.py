from .listener import ResultsListener
from .tasks import Task
from .wss import WebSocketServer


class PEKServer:
    def __init__(self, port):
        self.name = self.__class__.__name__
        self.port = port
        self.rls = ResultsListener(self)
        self.wss = WebSocketServer(self, port=port)
        self.tasks = {}
        self.taskClients = {}

    def start(self):
        self.rls.start()
        self.wss.start()

        self.rls.join()
        self.wss.join()

    def createTask(self, clientId, taskId):
        if taskId in self.tasks:
            raise ValueError(f"The task id {taskId} is already in use.")
        task = Task(self.rls.queue, taskId=taskId)
        self.tasks[task.id] = task
        self.taskClients[task.id] = clientId
        return task

    def getTask(self, taskId):
        return self.tasks[taskId]

    def sendPartialResult(self, partialResult):
        taskId = partialResult.info.id
        clientId = self.taskClients[taskId]

        self.wss.sendPartialResult(clientId, taskId, partialResult)

        if partialResult.info.last:
            del self.tasks[taskId]
            del self.taskClients[taskId]
