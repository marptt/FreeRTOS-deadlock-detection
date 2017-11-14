#ifndef LOGGER_H
#define LOGGER_H

#include <signal.h>
#include <stdio.h>
#include "FreeRTOS.h"

int testNum;
void taskSwitchedIn(char* thing);
void semaphoreGive(void* qwer);
void semaphoreGiveFailed(void* qwer);

void semaphoreTake(void* qwer);
void semaphoreTakeFailed(void* qwer);

void mutexCreated(void* pxNewMutex);

sigset_t signal_set;
FILE * logFile;
void loggerInit();
void onInterrupt();

#endif
