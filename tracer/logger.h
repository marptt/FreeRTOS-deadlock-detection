#ifndef LOGGER_H
#define LOGGER_H

#include <stdio.h>
#include "FreeRTOS.h"

int testNum;
void taskSwitchedIn(char* thing);
void taskBlocked(void* xQueue, int line, const char * file, const char * function, void* task);
void semaphoreGive(void* qwer);
void semaphoreGiveFailed(void* qwer);

void semaphoreTake(void* qwer);
void semaphoreTakeFailed(void* qwer);
void mutexCreated(void* pxNewMutex);
FILE * logFile;
void loggerInit();
void onInterrupt();

#endif
