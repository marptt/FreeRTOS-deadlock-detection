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

void onTraceTaskSwitchedIn(char* pcTaskName)
{
    if(strcmp(lastName, pcTaskName))
    {
        writeLog("switched in %s" , pcTaskName);
        lastName = pcTaskName;
    }
}

char* lastRemovedName = "";
void onTraceTaskSwitchedOut(char* pcTaskName)
{
    if(strcmp(lastRemovedName, pcTaskName))
    {
        writeLog("switched out %s", pcTaskName);
        lastRemovedName = pcTaskName;
    }
};

void onTraceQueueReceive(void* xQueue)
{
    writeLog("%s", "semaphore take");
}

void onTraceQueueReceiveFailed(void* xQueue)
{
    writeLog("%s", "semaphore take failed");
}

void onTraceQueueSend(void* xQueue)
{
    printf("semaphore give: %s\n", (char*)pcQueueGetName(xQueue));
    writeLog("%s", "semaphore give");
}

void onTraceQueueSendFailed(void* xQueue)
{
    writeLog("%s", "semaphore give failed");
}

void onTraceCreateMutex(void* pxNewMutex)
{
    char str[10];
    nrSemaCreated++;
    sprintf(str, "Sema_nr_%i", nrSemaCreated);

    printf("Created: %c\n", str[8]);
    vQueueAddToRegistry(pxNewMutex, str);
}


void onTraceMovedTaskToReadyState(void* xTask)
{
    //writeLog("%s","ready");
}

void onTraceBlockingOnQueueReceive (void* xQueue)
{

}

void onTraceblockingOnQueueSend(void* xQueue)
{

}

void onTraceTaskSuspend(void* xTask)
{

}

void onTraceTaskResume(void* xTask)
{

}

void onTraceTaskIncrementTick(void* xTickcount)
{

} 

void onTraceTaskDelete(void* xTask)
{

}             

void onTraceTaskDelayUntil()
{

}                     

void onTraceTaskDelay()
{

}
