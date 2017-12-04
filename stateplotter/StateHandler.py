global TASK_BLOCKED   
global TASK_SUSPENDED 
global TASK_RUNNING   
global TASK_READY     
 
TASK_BLOCKED   = 'Running'    
TASK_SUSPENDED = 'Suspended' 
TASK_RUNNING   = 'Ready'    
TASK_READY     = 'Blocked'   



class StateSnapshot():
    def __init__(self, tasks, semaphores, event):
        self.tasks = tasks
        self.semaphores = semaphores
        self.event = event

# TODO make this a dict
class TaskState():
    def __init__(self,
                 taskName,
                 currentState,
                 previousState,
                 eventName,
                 requestedSemaphores,
                 heldSemaphores,
                 enableArrow
    ):
        self.currentState = currentState
        self.previousState = previousState
        self.taskName = taskName
        self.eventName = eventName
        self.requestedSemaphores = requestedSemaphores
        self.heldSemaphores = heldSemaphores
        self.enableArrow = enableArrow
        
        
class StateHandler():
    def __init__(self):
        self.currentStateCallbacks = []
        self.statesCallbacks = [] 
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
                [
                    TaskState(
                        taskName="egg",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_SUSPENDED,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = True
                    )],
                ["RedSemaphore", "GreenSemaphore", "BlueSemaphore"],
                'something happened first'
            ),
            StateSnapshot(
                [
                    TaskState(
                        taskName="egg",
                        currentState=TASK_BLOCKED,
                        previousState=TASK_SUSPENDED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = True
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    )
                ],
                ["RedSemaphore", "GreenSemaphore", "BlueSemaphore"],
                'something happened then'
            ),
            StateSnapshot(
                [
                    TaskState(
                        taskName="egg",
                        currentState=TASK_SUSPENDED,
                        previousState=TASK_READY,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = True
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="egg",
                        currentState=TASK_SUSPENDED,
                        previousState=TASK_READY,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = True
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="egg",
                        currentState=TASK_SUSPENDED,
                        previousState=TASK_READY,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = True
                    ),
                    TaskState(
                        taskName="bacon",
                        currentState=TASK_READY,
                        previousState=TASK_BLOCKED,
                        eventName="something caused this",
                        requestedSemaphores = [],
                        heldSemaphores = [],
                        enableArrow = False
                    )                    
                ],
                ["RedSemaphore", "GreenSemaphore", "BlueSemaphore"],
                'something happened then'
            )
        ])
