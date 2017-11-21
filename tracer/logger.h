#ifndef LOGGER_H
#define LOGGER_H

#include <signal.h>
#include <stdio.h>
#include "FreeRTOS.h"


typedef struct {
    const char* file;
    const char* function;
    int line;
}source_code_position_t;


#define GET_SOURCE_CODE_POSITION (source_code_position_t){.file = __FILE__, .function = __FUNCTION__, .line = __LINE__}

int testNum;
void onTraceTaskSwitchedIn(char* pcTaskName);
void onTraceTaskSwitchedOut(char* pcTaskName);
void onTraceQueueSend(void* xQueue, source_code_position_t source_code_position);
void onTraceQueueSendFailed(void* xQueue);
void onTraceQueueReceive(void* xQueue);
void onTraceQueueReceiveFailed(void* xQueue);
void onTraceCreateMutex(void* pxNewMutex);
void onTraceMovedTaskToReadyState(void* xTask);
void onTraceBlockingOnQueueReceive (void* xQueue, source_code_position_t source_code_position);
void onTraceblockingOnQueueSend(void* xQueue);
void onTraceTaskSuspend(void* xTask);
void onTraceTaskResume(void* xTask);
void onTraceTaskIncrementTick(uint32_t xTickcount); /*Borde vara TickType_t? */ 
// void onTraceTaskDelete(void* xTask);             
void onTraceTaskDelayUntil();                     
void onTraceTaskDelay();



sigset_t signal_set;
FILE * logFile;
void loggerInit();
void onInterrupt();

#endif
