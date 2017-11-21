#include <string.h>
#include <stdio.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"
#include <signal.h>
#include <stdlib.h>
#include "queue.h"

#define GET_SOURCE_CODE_POSITION (source_code_position_t){.file = __FILE__, .function = __FUNCTION__, .line = __LINE__}

#define writeLog( format, data ) {                                     \
    vPortEnterCritical();                                              \
    sigprocmask(SIG_BLOCK, &signal_set, NULL);                         \
    fprintf(logFile, "%i, "format"\n", xTaskGetTickCount(), data);     \
    printf(format "\n", data);                                         \
    sigprocmask(SIG_UNBLOCK, &signal_set, NULL);                       \
    vPortExitCritical();                                               \
}

void printSCP(source_code_position_t scp);

/*Variables*/
char* lastName = "";
int nrSemaCreated = 0;


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

void taskSwitchedIn(char* thing)
{
    if(strcmp(lastName, thing))
    {
	writeLog("%s", thing);
        lastName = thing;
    }
}

void taskBlocked(void* xQueue, source_code_position_t source_code_position)
{
    printf("Task \"%s\" blocked from sema '%s': ", pcTaskGetName(xTaskGetCurrentTaskHandle()), (char*)pcQueueGetName(xQueue) );
	printSCP(source_code_position);
}

void semaphoreTake(void* qwer)
{
    writeLog("%s", "semaphore take");
}
void semaphoreTakeFailed(void* qwer)
{
    writeLog("%s", "semaphore take failed");
}

void semaphoreGive(void* qwer, source_code_position_t source_code_position)
{
    printf("semaphore '%s' give: ", (char*)pcQueueGetName(qwer));
	printSCP(source_code_position);
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

void printSCP(source_code_position_t scp)
{
	printf( "'%s','%s','%i'\n", scp.file, scp.function, scp.line );
}
