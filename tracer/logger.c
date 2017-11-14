#include <string.h>
#include <stdio.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"
#include <signal.h>
#include <stdlib.h>
#include "queue.h"

#define writeLog( format, data ) {                                     \
    vPortEnterCritical();                                              \
    sigprocmask(SIG_BLOCK, &signal_set, NULL);                         \
    fprintf(logFile, "%i, "format"\n", xTaskGetTickCount(), data);     \
    printf(format "\n", data);                                         \
    sigprocmask(SIG_UNBLOCK, &signal_set, NULL);                       \
    vPortExitCritical();                                               \
}

void onInterrupt()
{
    vPortEnterCritical(); // cease other activity
    fclose( logFile );
    exit( 0 );
}

void loggerInit()
{
    sigemptyset(&signal_set);
    sigaddset(&signal_set, SIGINT);
    signal(SIGINT, onInterrupt); // SIGINT, triggered by Ctrl+C
    logFile = fopen("logFile","w");
    fprintf(logFile, "tickCount, message\n");
}

char* lastName = "";
int nrSemaCreated = 0;

void taskSwitchedIn(char* thing)
{
    if(strcmp(lastName, thing))
    {
        writeLog("%s", thing);
        lastName = thing;
    }
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
    vQueueAddToRegistry(pxNewMutex, str);
}
