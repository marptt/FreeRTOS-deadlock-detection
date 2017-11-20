#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>

typedef struct {
    char* file;
    char* function;
    int line;
}source_code_position_t;

#define GET_SOURCE_CODE_POSITION (source_code_position_t){.file = __FILE__, .function = __FUNCTION__, .line = __LINE__}

#define traceTASK_SWITCHED_IN() taskSwitchedIn(pxCurrentTCB -> pcTaskName)
#define traceBLOCKING_ON_QUEUE_RECEIVE(xQueue) taskBlocked(xQueue, source_code_position, xTaskGetCurrentTaskHandle())
#define traceQUEUE_SEND(xQueue) semaphoreGive(xQueue)
#define traceQUEUE_SEND_FAILED(xQueue) semaphoreGiveFailed(xQueue)

#define traceQUEUE_RECEIVE(xQueue) semaphoreTake(xQueue)
#define traceQUEUE_RECEIVE_FAILED(xQueue) semaphoreTakeFailed(xQueue)
#define traceCREATE_MUTEX(pxNewMutex) mutexCreated(pxNewMutex)

#endif
