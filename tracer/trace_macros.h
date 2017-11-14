#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>

#define traceTASK_SWITCHED_IN() taskSwitchedIn(pxCurrentTCB -> pcTaskName)
#define traceBLOCKING_ON_QUEUE_RECEIVE(xQueue, line, file, function) taskBlocked(xQueue, line, file, function, pxCurrentTCB)
#define traceQUEUE_SEND(xQueue) semaphoreGive(xQueue)
#define traceQUEUE_SEND_FAILED(xQueue) semaphoreGiveFailed(xQueue)

#define traceQUEUE_RECEIVE(xQueue) semaphoreTake(xQueue)
#define traceQUEUE_RECEIVE_FAILED(xQueue) semaphoreTakeFailed(xQueue)
#define traceCREATE_MUTEX(pxNewMutex) mutexCreated(pxNewMutex)

#endif
