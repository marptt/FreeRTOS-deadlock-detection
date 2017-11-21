#ifndef MACRO_H
#define MACRO_H

#include "logger.h"
#include <stdio.h>


#define traceTASK_SWITCHED_IN() taskSwitchedIn( pxCurrentTCB -> pcTaskName )
#define traceBLOCKING_ON_QUEUE_RECEIVE(xQueue) taskBlocked( xQueue, source_code_position )
#define traceQUEUE_SEND(xQueue) semaphoreGive( xQueue, source_code_position )
#define traceQUEUE_SEND_FAILED(xQueue) semaphoreGiveFailed( xQueue )

#define traceQUEUE_RECEIVE(xQueue) semaphoreTake( xQueue )
#define traceQUEUE_RECEIVE_FAILED(xQueue) semaphoreTakeFailed( xQueue )
#define traceCREATE_MUTEX(pxNewMutex) mutexCreated( pxNewMutex )

#endif
