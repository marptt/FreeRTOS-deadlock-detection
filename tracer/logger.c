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
    sigprocmask(SIG_UNBLOCK, &signal_set, NULL);                       \
    vPortExitCritical();                                               \
}

/*Function for testing trace macros*/
void printSCP( const char* function, source_code_position_t scp);

/*Variables*/
char* lastName = "";
int nrSemaCreated = 0;
char* lastRemovedName = "";


/*Functions*/
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


void printSCP( const char* function, source_code_position_t scp )
{
	printf( "%s:\t '%s','%s()','%i'\n", function, scp.file, scp.function, scp.line );
}




/*###### Trace functions ######*/

void onTraceBlockingOnQueueReceive (void* xQueue, source_code_position_t source_code_position)
{
	/* printf("Task \"%s\" blocked from sema '%s': ", pcTaskGetName(xTaskGetCurrentTaskHandle()), (char*)pcQueueGetName(xQueue) ); */
	printSCP(__FUNCTION__,source_code_position);
}

void onTraceBlockingOnQueueSend(void* xQueue, source_code_position_t source_code_position )
{
	printSCP(__FUNCTION__,source_code_position);
}


void onTraceCreateMutex(void* pxNewMutex, source_code_position_t source_code_position)
{
    /* char str[10]; */
    /* nrSemaCreated++; */
    /* sprintf(str, "Sema_nr_%i", nrSemaCreated); */

    /* printf("Created: %c\n", str[8]); */
   	printSCP(__FUNCTION__,source_code_position);
	vQueueAddToRegistry(pxNewMutex, "apa");
}


void onTraceMovedTaskToReadyState(void* xTask)
{
    //writeLog("%s","ready");
}


void onTraceQueueReceive(void* xQueue, source_code_position_t source_code_position )
{
    writeLog("%s", "semaphore take");
   	printSCP(__FUNCTION__, source_code_position);
}


void onTraceQueueReceiveFailed(void* xQueue, source_code_position_t source_code_position)
{
    /* writeLog("%s", "semaphore take failed"); */
   	printSCP(__FUNCTION__, source_code_position);
}


void onTraceQueueSend(void* xQueue, source_code_position_t source_code_position)
{
    /* printf("semaphore '%s' give: ", (char*)pcQueueGetName(xQueue)); */
	printSCP(__FUNCTION__, source_code_position);
    writeLog("%s", "semaphore give");
}


void onTraceQueueSendFailed(void* xQueue, source_code_position_t source_code_position)
{
	printSCP(__FUNCTION__, source_code_position);
	writeLog("%s", "semaphore give failed");
}


void onTraceTaskDelay(source_code_position_t source_code_position)
{
	printSCP(__FUNCTION__, source_code_position);
}


void onTraceTaskDelayUntil(uint32_t xTickCount, source_code_position_t source_code_position)
{
	printSCP(__FUNCTION__, source_code_position);
}


void onTraceTaskDelete(void* xTask)
{

}


void onTraceTaskIncrementTick(uint32_t xTickcount)
{

} 

             
void onTraceTaskResume(void* xTask)
{

}                     


void onTraceTaskSuspend(void* xTask)
{

}


void onTraceTaskSwitchedIn(char* pcTaskName)
{
    if(strcmp(lastName, pcTaskName))
    {
        /* writeLog("switched in %s" , pcTaskName); */
        lastName = pcTaskName;
    }
}


void onTraceTaskSwitchedOut(char* pcTaskName)
{
    if(strcmp(lastRemovedName, pcTaskName))
    {
        /* writeLog("switched out %s", pcTaskName); */
        lastRemovedName = pcTaskName;
    }
}
