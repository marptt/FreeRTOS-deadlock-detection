class StateSnapshot():
    def __init__(self, tasks, semaphores, event):
        self.tasks = tasks
        self.semaphores = semaphores
        self.event = event

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
        newState = self.states[index]
        for cb in self.currentStateCallbacks:
            cb(newState)

    def emitStatesChange(self, states):
        for cb in self.statesCallbacks:
            cb(states)
            
    def setStates(self, states):
        self.states = states
        self.emitStatesChange(states)
        
    def testStates(self):
        self.setStates( [
            StateSnapshot(
                [TaskState("eggs", self.TASK_READY)],
                [],
                'something happened first'
            ),
            StateSnapshot(
                [TaskState("eggs", self.TASK_READY)],
                [],
                'something happened second'
            ),
            StateSnapshot(
                [TaskState("eggs", self.TASK_BLOCKED)],
                [],
                'something happened third'
            ),
            StateSnapshot(
                [TaskState("eggs", self.TASK_RUNNING)],
                [],
                'something  else happened'
            ),
            StateSnapshot(
                [
                    TaskState("eggs", self.TASK_SUSPENDED),
                    TaskState("bacon", self.TASK_SUSPENDED)
                ],
                [],
                'something more happened'
            ),
            StateSnapshot(
                [
                    TaskState("eggs", self.TASK_READY),
                    TaskState("bacon", self.TASK_SUSPENDED)
                ],
                [],
                'something additionally happened'
            ),
            StateSnapshot(
                [
                    TaskState("eggs", self.TASK_READY),
                    TaskState("bacon", self.TASK_SUSPENDED)
                ],
                [],
                'something happened again'
            ),
            StateSnapshot(
                [
                    TaskState("eggs", self.TASK_SUSPENDED),
                    TaskState("bacon", self.TASK_READY),
                    TaskState("milk", self.TASK_RUNNING)
                ],
                [],
                'something happened yet again'
            ),
            StateSnapshot(
                [TaskState("eggs", self.TASK_READY)],
                [],
                'something happened yet yet again'
            ),
            StateSnapshot(
                [TaskState("eggs", self.TASK_READY)],
                [],
                'something happened yet yet yet again'
            )
        ])
