#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>


#define traceTASK_SWITCHED_IN() onTraceTaskSwitchedIn(pxCurrentTCB -> pcTaskName)
#define traceTASK_SWITCHED_OUT() onTraceTaskSwitchedOut(pxCurrentTCB -> pcTaskName)

#define traceQUEUE_SEND(xQueue) onTraceQueueSend(xQueue)
#define traceQUEUE_SEND_FAILED(xQueue) onTraceQueueSendFailed(xQueue)

#define traceQUEUE_RECEIVE(xQueue) onTraceQueueReceive(xQueue) 
#define traceQUEUE_RECEIVE_FAILED(xQueue) onTraceQueueReceiveFailed(xQueue)
#define traceCREATE_MUTEX(pxNewMutex) onTraceCreateMutex(pxNewMutex)

#define traceMOVED_TASK_TO_READY_STATE(xTask) onTraceMovedTaskToReadyState(xTask)
#define traceBLOCKING_ON_QUEUE_RECEIVE(xQueue) onTraceBlockingOnQueueReceive (xQueue)
#define traceBLOCKING_ON_QUEUE_SEND(xQueue) onTraceblockingOnQueueSend(xQueue)

#define traceTASK_SUSPEND(xTask) onTraceTaskSuspend(xTask)
#define traceTASK_RESUME(xTask)	onTraceTaskResume(xTask)	

#define traceTASK_INCREMENT_TICK(xTickCount) onTraceTaskIncrementTick(void* xTickcount)
#define traceTASK_DELAY() onTraceTaskDelete(void* xTask)
// #define traceTASK_DELETE(xTask) onTraceTaskDelayUntil()                     	
#define traceTASK_DELAY_UNTIL()	onTraceTaskDelay()

#endif
