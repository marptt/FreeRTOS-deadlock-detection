#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>


#define vTaskDelay( xTicksToDelay )  vTaskDelay_scp( xTicksToDelay, GET_SOURCE_CODE_POSITION )
#define vTaskDelayUntil( pxPreviousWakeTime, xTimeIncrement ) vTaskDelayUntil_scp( pxPreviousWakeTime, xTimeIncrement, GET_SOURCE_CODE_POSITION )


#define traceBLOCKING_ON_QUEUE_RECEIVE(xQueue) onTraceBlockingOnQueueReceive( xQueue, source_code_position )
#define traceBLOCKING_ON_QUEUE_SEND(xQueue) onTraceBlockingOnQueueSend( xQueue, source_code_position )
#define traceCREATE_MUTEX(pxNewMutex) onTraceCreateMutex( pxNewMutex, source_code_position )
#define traceMOVED_TASK_TO_READY_STATE(xTask) onTraceMovedTaskToReadyState(xTask)
#define traceQUEUE_RECEIVE(xQueue) onTraceQueueReceive(xQueue, source_code_position ) 
#define traceQUEUE_RECEIVE_FAILED(xQueue) onTraceQueueReceiveFailed(xQueue, source_code_position)
#define traceQUEUE_SEND(xQueue) onTraceQueueSend(xQueue, source_code_position )
#define traceQUEUE_SEND_FAILED(xQueue) onTraceQueueSendFailed( xQueue, source_code_position )
#define traceTASK_DELAY() onTraceTaskDelay(source_code_position)
#define traceTASK_DELAY_UNTIL(xTickCount) onTraceTaskDelayUntil(xTickCount, source_code_position)
// #define traceTASK_DELETE(xTask) onTraceTaskDelete(xTask)       	
#define traceTASK_INCREMENT_TICK(xTickCount) onTraceTaskIncrementTick( xTickCount)
#define traceTASK_RESUME(xTask)	onTraceTaskResume(xTask)
#define traceTASK_SUSPEND(xTask) onTraceTaskSuspend(xTask)
#define traceTASK_SWITCHED_IN() onTraceTaskSwitchedIn(pxCurrentTCB -> pcTaskName)
#define traceTASK_SWITCHED_OUT() onTraceTaskSwitchedOut(pxCurrentTCB -> pcTaskName)


#endif
