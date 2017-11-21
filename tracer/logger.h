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
void taskSwitchedIn(char* thing);
void taskBlocked(void* xQueue, source_code_position_t source_code_position);
void semaphoreGive(void* qwer, source_code_position_t source_code_position);
void semaphoreGiveFailed(void* qwer);

void semaphoreTake(void* qwer);
void semaphoreTakeFailed(void* qwer);

void mutexCreated(void* pxNewMutex);

sigset_t signal_set;
FILE * logFile;
void loggerInit();
void onInterrupt();

#endif
