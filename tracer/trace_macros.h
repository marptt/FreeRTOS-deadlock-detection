#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>

#define traceTASK_SWITCHED_IN() taskSwitchedIn(pxCurrentTCB -> pcTaskName)
#define traceQUEUE_SEND(xQueue) semaphoreGive(xQueue)
#define traceQUEUE_SEND_FAILED(xQueue) semaphoreGiveFailed(xQueue)

#define traceQUEUE_RECEIVE(xQueue) semaphoreTake(xQueue)
#define traceQUEUE_RECEIVE_FAILED(xQueue) semaphoreTakeFailed(xQueue)


#endif
