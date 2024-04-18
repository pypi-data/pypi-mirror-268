import json
import traceback
from threading import Thread

from flask import Flask
from flask_cors import CORS
from flask_socketio import SocketIO, join_room
from sklearn.utils import Bunch

from ..data import DatasetLoader
from ..utils.encoding import NumpyEncoder
from ..version import __version__
from .log import Log

"""
When creating an ensemble task or elbow task, the client is added to a room named as the taskId.
This speed up the sending of partial results because they are sent to the room that contain a single client.
"""

BUFFER_SIZE = 2 * 1024 * 1024 * 1024  # two gigabytes
PING_TIMEOUT = 120


class _WebSocketServerResponse(Bunch):
    def __init__(self, data=None, error=False, errorMessage=None):
        super().__init__(data=data, error=error, errorMessage=errorMessage)


def _handleException(error):
    # Extract information from the exception
    """details = {
        # "message": str(error),  # Convert the exception to a string
        # "type": type(error).__name__,  # Get the type of the exception
        "details": repr(error),  # Get detailed information about the exception
        "stack_trace": traceback.format_exc(),
    }"""
    traceback.print_exc()
    return _WebSocketServerResponse(error=True, errorMessage=repr(error))


class WebSocketServer(Thread):
    def __init__(self, server, port=21000):
        super().__init__()
        self.server = server
        self.port = port

        self.app = None
        self.socketio = None
        self._loadedDatasets = {}

    def run(self) -> None:
        app = Flask(self.server.name)
        app.config["MAX_CONTENT_LENGTH"] = BUFFER_SIZE
        CORS(app, resources={r"/*": {"origins": "*"}})
        socketio = SocketIO(app, cors_allowed_origins="*", max_http_buffer_size=BUFFER_SIZE, ping_timeout=PING_TIMEOUT)

        self.app = app
        self.socketio = socketio

        ############ STATIC DATA ###############

        @socketio.on("info")
        def handle_info(_):
            data = Bunch(serverVersion=__version__, datasets=DatasetLoader.allNames())
            return _WebSocketServerResponse(data=data)

        @socketio.on("dataset")
        def handle_dataset(payload):
            # {'name': '...', features: False, original=False, scaled=False, isomap=False, mds=False, pca=False, tsne=False, umap=False} -> set bool items to True to get the projection
            d = Bunch(**json.loads(payload))
            if d.name not in self._loadedDatasets:
                self._loadedDatasets[d.name] = DatasetLoader.load(d.name)
            dataset = self._loadedDatasets[d.name]
            if dataset is None:
                return None

            def _check(key):
                return key in d and d[key] == True

            obj = Bunch(
                name=d.name,
                features=dataset.features if _check("features") else None,
                original=dataset.data if _check("original") else None,
                scaled=dataset.datasc if _check("scaled") else None,
                isomap=dataset.isomap if _check("isomap") else None,
                mds=dataset.mds if _check("mds") else None,
                pca=dataset.pca if _check("pca") else None,
                tsne=dataset.tsne if _check("tsne") else None,
                umap=dataset.umap if _check("umap") else None,
            )
            return _WebSocketServerResponse(data=json.dumps(obj, cls=NumpyEncoder))

        ############ TASK ACTIONS ###############
        @socketio.on("start-task")
        def handle_start_task(datajson):
            try:
                d = Bunch(**json.loads(datajson))  # {clientId: '...', taskId: '...', args: {}}
                Log.print(f"Creating task.", taskId=d.taskId)
                task = self.server.createTask(d.clientId, d.taskId)
                Log.print(f"{Log.BLUE}Starting task.", taskId=d.taskId)
                task.start(d.args)
                return _WebSocketServerResponse(data=Bunch(taskId=d.taskId, strarted=True))
            except Exception as e:
                _handleException(e)

        @socketio.on("pause-task")
        def handle_pause_task(datajson):
            try:
                d = Bunch(**json.loads(datajson))  # {'taskId': '...'}
                Log.print(f"{Log.YELLOW}Pausing task.", taskId=d.taskId)
                self.server.getTask(d.taskId).pause()
                return _WebSocketServerResponse(data=Bunch(taskId=d.taskId, paused=True))
            except Exception as e:
                _handleException(e)

        @socketio.on("resume-task")
        def handle_resume_task(datajson):
            try:
                d = Bunch(**json.loads(datajson))  # {'taskId': '...'}
                Log.print(f"{Log.YELLOW}Resuming task.", taskId=d.taskId)
                self.server.getTask(d.taskId).resume()
                return _WebSocketServerResponse(data=Bunch(taskId=d.taskId, resumed=True))
            except Exception as e:
                _handleException(e)

        @socketio.on("kill-task")
        def handle_kill_task(datajson):
            try:
                d = Bunch(**json.loads(datajson))  # {'taskId': '...'}
                Log.print(f"{Log.RED}Killing task.", taskId=d.taskId)
                self.server.getTask(d.taskId).kill()
                return _WebSocketServerResponse(data=Bunch(taskId=d.taskId, killed=True))
            except Exception as e:
                _handleException(e)

        @socketio.on("kill-run")
        def handle_kill_progressive_ensemble_kmeans_task_run(datajson):
            try:
                d = Bunch(**json.loads(datajson))  # {'taskId': '...', 'runId': '...' }
                Log.print(f"{Log.RED}Killing run #{d.args.runId}", taskId=d.taskId)
                self.server.getTask(d.taskId).killRun(d.args.runId)
                return _WebSocketServerResponse(data=Bunch(taskId=d.taskId, runId=d.runId, killedRun=True))
            except Exception as e:
                _handleException(e)

        socketio.run(app, port=self.port, host="0.0.0.0")

    def sendPartialResult(self, clientId, taskId, partialResult):
        self.socketio.emit(taskId, partialResult.toJson(compressed=True), to=clientId)

        # if taskId.startswith("ENS"):
        Log.print(
            f"{Log.BLUE}Sent pr#{partialResult.info.iteration}{Log.ENDC} --- info={partialResult.info} et={partialResult.earlyTermination}",
            taskId=taskId,
        )
        """elif taskId.startswith("ELB"):
            Log.print(
                f"{Log.BLUE}Sent pr#{partialResult.info.iteration}{Log.ENDC} --- info={partialResult.info}",
                taskId=taskId,
            )"""

        # else:
        #    raise RuntimeError(f"Undefined type of task {taskId}")
