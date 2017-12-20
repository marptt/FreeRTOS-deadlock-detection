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
sigset_t signal_set;
FILE * logFile;

void loggerInit();
void onInterrupt();
/*Trace functions*/
void onTraceBlockingOnQueueReceive (void* xQueue, source_code_position_t source_code_position);
void onTraceBlockingOnQueueSend(void* xQueue, source_code_position_t source_code_position);
void onTraceCreateCounting( void* xHandle, source_code_position_t source_code_position );
void onTraceCreateMutex(void* pxNewMutex, source_code_position_t source_code_position);
void onTraceMovedTaskToReadyState(void* xTask);
void onTraceQueueReceive(void* xQueue, source_code_position_t source_code_position);
void onTraceQueueReceiveFailed(void* xQueue, source_code_position_t source_code_position);
void onTraceQueueSend(void* xQueue, source_code_position_t source_code_position);
void onTraceQueueSendFailed(void* xQueue, source_code_position_t source_code_position );
void onTraceTaskCreate(void* xTask, source_code_position_t source_code_position );
void onTraceTaskDelay(source_code_position_t source_code_position);
void onTraceTaskDelayUntil(uint32_t xTickCount, source_code_position_t source_code_position); /*Borde vara TickType_t? */ 
void onTraceTaskDelete(void* xTask);
void onTraceTaskIncrementTick(uint32_t xTickcount); /*Borde vara TickType_t? */ 
void onTraceTaskResume(void* xTask);
void onTraceTaskSuspend(void* xTask);
void onTraceTaskSwitchedIn(void* xTask);
void onTraceTaskSwitchedOut(void* xTask);

#endif
