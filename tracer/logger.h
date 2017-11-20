#ifndef LOGGER_H
#define LOGGER_H

#include <signal.h>
#include <stdio.h>
#include "FreeRTOS.h"

int testNum;


void onTraceTaskSwitchedIn(char* pcTaskName);
void onTraceTaskSwitchedOut(char* pcTaskName);
void onTraceQueueSend(void* xQueue);
void onTraceQueueSendFailed(void* xQueue);
void onTraceQueueReceive(void* xQueue);
void onTraceQueueReceiveFailed(void* xQueue);
void onTraceCreateMutex(void* pxNewMutex);
void onTraceMovedTaskToReadyState(void* xTask);
void onTraceBlockingOnQueueReceive (void* xQueue);
void onTraceblockingOnQueueSend(void* xQueue);
void onTraceTaskSuspend(void* xTask);
void onTraceTaskResume(void* xTask);
void onTraceTaskIncrementTick(void* xTickcount); 
// void onTraceTaskDelete(void* xTask);             
void onTraceTaskDelayUntil();                     
void onTraceTaskDelay();



sigset_t signal_set;
FILE * logFile;
void loggerInit();
void onInterrupt();

#endif
