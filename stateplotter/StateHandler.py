
class TaskState():
    def __init__(self, name, taskState):
        self.taskState = taskState
        self.name = name

class StateHandler():
    def __init__(self):
        self.currentStateCallbacks = []
        self.statesCallbacks = []

        self.TASK_BLOCKED = 0
        self.TASK_SUSPENDED =1
        self.TASK_RUNNING = 2
        self.TASK_READY = 3

        self.testStates()
        
    def subscribeToCurrentState(self, callback):
        self.currentStateCallbacks.append(callback)

    def subscribeToStates(self, callback):
        self.statesCallbacks.append(callback)
        
    def emitCurrentStateChange(self, index):
        for cb in self.currentStateCallbacks:
            cb(index)

    def emitStatesChange(self, states):
        for cb in self.statesCallbacks:
            cb(states)
            
    def setStates(self, states):
        self.states = states
        self.emitStatesChange(states)
        
    def testStates(self):
        self.setStates( [
            TaskState("ready task", self.TASK_READY),
            TaskState("suspended task", self.TASK_SUSPENDED),
            TaskState("running task", self.TASK_RUNNING),
            TaskState("also runningtask", self.TASK_RUNNING),
            TaskState("blocked task", self.TASK_BLOCKED)
        ])
