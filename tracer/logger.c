#include <string.h>
#include <stdio.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"
#include <signal.h>
#include <stdlib.h>

#define writeLog( format, data ) {                                     \
    vPortEnterCritical();                                              \
    fprintf(logFile, "%i, " format "\n", xTaskGetTickCount(), data); \
    printf(format "\n", data);                                         \
    vPortExitCritical();                                               \
}

/*Variables*/
char* lastName = "";
int nrSemaCreated = 0;


void onInterrupt(int signum)
{
    fclose( logFile );
    exit( 0 );
}

void loggerInit()
{
    signal(SIGINT, onInterrupt);
    logFile = fopen("logFile","w");
    fprintf(logFile, "tickCount, message\n");
}

void taskSwitchedIn(char* thing)
{
    if(strcmp(lastName, thing))
    {
        writeLog("%s", thing);
        lastName = thing;
    }
}

void taskBlocked(void* xQueue, int line,const char* file, const char * function, void* task)
{
    printf("Task \"%s\" blocked from sema \"%s\" on row %i, %s, %s.\n", pcTaskGetName(task), (char*)pcQueueGetName(xQueue),line, file, function);
}

void semaphoreTake(void* qwer)
{
    writeLog("%s", "semaphore take");
}
void semaphoreTakeFailed(void* qwer)
{
    writeLog("%s", "semaphore take failed");
}

void semaphoreGive(void* qwer)
{
    printf("semaphore give: %s\n", (char*)pcQueueGetName(qwer));
    writeLog("%s", "semaphore give");
}
void semaphoreGiveFailed(void* qwer)
{
    writeLog("%s", "semaphore give failed");
    //printf("%s\n",(char*)qwer);
}

void mutexCreated(void* pxNewMutex)
{
    char str[10];
    nrSemaCreated++;
    sprintf(str, "Sema_nr_%i", nrSemaCreated);

    printf("Created: %c\n", str[8]);
    vQueueAddToRegistry(pxNewMutex, "apa");
}
