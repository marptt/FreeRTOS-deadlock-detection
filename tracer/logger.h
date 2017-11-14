#ifndef LOGGER_H
#define LOGGER_H

#include "FreeRTOS.h"

int testNum;
void taskSwitchedIn(char* thing);
void semaphoreGive(void* qwer);
void semaphoreGiveFailed(void* qwer);

void semaphoreTake(void* qwer);
void semaphoreTakeFailed(void* qwer);

FILE * logFile;
void onInterrupt();

#endif
