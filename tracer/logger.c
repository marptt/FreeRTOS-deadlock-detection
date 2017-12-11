#include <string.h>
#include <stdio.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"
#include <signal.h>
#include <stdlib.h>
#include "queue.h"

#define GET_SOURCE_CODE_POSITION (source_code_position_t){.file = __FILE__, .function = __FUNCTION__, .line = __LINE__}

#define JSON_STRING(key, value) "\""key"\": " "\""value"\""
#define writeLog( format, data... ) {                                   \
        vPortEnterCritical();                                           \
        sigprocmask(SIG_BLOCK, &signal_set, NULL);                      \
        fprintf(logFile, format",\n", data, xTaskGetTickCount());       \
        sigprocmask(SIG_UNBLOCK, &signal_set, NULL);                    \
        vPortExitCritical();                                            \
    }
/* printf( format",\n", data, xTaskGetTickCount());                                \ */


#define EVENT_DATA                              \
    "    \"event\":{\n"                         \
    "        \"data\": \"%s\",\n"               \
    "        \"tick\": %i\n"                    \
    "    }\n"                                   \
        
#define SOURCE_CODE_DATA                        \
    "    \"source\":{\n"                        \
    "        \"file\": \"%s\",\n"               \
    "        \"function\": \"%s\",\n"           \
    "        \"line\": %i\n"                    \
    "    },\n"                                  \


#define EVENT_FORMAT_SEMAPHORE                  \
    "{\n"                                       \
    "    \"type\": \"SEMAPHORE\",\n"            \
    "    \"handle\": %i,\n"                     \
    SOURCE_CODE_DATA                            \
    EVENT_DATA                                  \
    "}"                                         \

#define EVENT_FORMAT_DELAY                      \
    "{\n"                                       \
    "    \"type\": \"DELAY\",\n"                \
    "    \"duration\": %i,\n"                   \
    SOURCE_CODE_DATA                            \
    EVENT_DATA                                  \
    "}"                                         \

#define EVENT_FORMAT_TASK_KERNEL                \
    "{\n"                                       \
    "    \"type\": \"TASK_KERNEL\",\n"          \
    "    \"taskHandle\": %i,\n"                 \
    "    \"taskName\": \"%s\",\n"               \
    "    \"taskPriority\": %d,\n"               \
    EVENT_DATA                                  \
    "}"                                         \

#define EVENT_FORMAT_TASK_USER                  \
    "{\n"                                       \
    "    \"type\": \"TASK_USER\",\n"            \
    "    \"taskHandle\": %i,\n"                 \
    "    \"taskName\": \"%s\",\n"               \
    "    \"taskPriority\": %d,\n"               \
    SOURCE_CODE_DATA                            \
    EVENT_DATA                                  \
    "}"                                         \

/* Function  */
void printSCP( const char* function, source_code_position_t scp);
void closeJSONandFile();

/* Variables */
char* lastName = "";
int nrSemaCreated = 0;
char* lastRemovedName = "";


/* Functions */
void onInterrupt()
{
    vPortEnterCritical(); /* cease other activity */
    closeJSONandFile();
    exit( 0 );
}

void closeJSONandFile()
{
    fprintf(logFile, "{\n    \"type\": \"The End\",\n    \"tick\": %i\n}]}\n", xTaskGetTickCount());
    fclose( logFile );
}

void loggerInit()
{
    sigemptyset(&signal_set);
    sigaddset(&signal_set, SIGINT);
    signal(SIGINT, onInterrupt); /* SIGINT, triggered by Ctrl+C */
    logFile = fopen("logFile.json","w");
    fprintf(logFile, "{\"log\":[");
}


void printSCP( const char* function, source_code_position_t scp )
{
    printf( "%s:\t '%s','%s()','%i'\n", function, scp.file, scp.function, scp.line );
}


/* ###### Trace functions ###### */

void onTraceBlockingOnQueueReceive (void* xQueue, source_code_position_t scp)
{       
    writeLog(EVENT_FORMAT_SEMAPHORE, (int)xQueue, scp.file, scp.function, scp.line, "Blocked on Take");
    /* printSCP(__FUNCTION__, scp); */
}

void onTraceBlockingOnQueueSend(void* xQueue, source_code_position_t source_code_position )
{
    /* printSCP(__FUNCTION__,source_code_position); */
}


void onTraceCreateMutex(void* pxNewMutex, source_code_position_t scp)
{
	/* printSCP(__FUNCTION__,scp); */
    writeLog(EVENT_FORMAT_SEMAPHORE, (int)pxNewMutex, scp.file, scp.function, scp.line, "Mutex created");
}


void onTraceMovedTaskToReadyState(void* xTask)
{
    writeLog(EVENT_FORMAT_TASK_KERNEL, (int)xTask, pcTaskGetName(xTask), (int)uxTaskPriorityGet(xTask), "Moved to ready");
}


void onTraceQueueReceive(void* xQueue, source_code_position_t scp )
{
    writeLog(EVENT_FORMAT_SEMAPHORE, (int)xQueue, scp.file, scp.function, scp.line, "Take");
    /* printSCP(__FUNCTION__, scp); */
}


void onTraceQueueReceiveFailed(void* xQueue, source_code_position_t scp)
{
    writeLog(EVENT_FORMAT_SEMAPHORE, (int)xQueue, scp.file, scp.function, scp.line, "Failed take - timed out" );
    /* printSCP(__FUNCTION__, source_code_position); */
}


void onTraceQueueSend(void* xQueue, source_code_position_t scp)
{
	/* printSCP(__FUNCTION__, scp); */
    writeLog(EVENT_FORMAT_SEMAPHORE, (int)xQueue, scp.file, scp.function, scp.line, "Semaphore give" );
}


void onTraceQueueSendFailed(void* xQueue, source_code_position_t source_code_position)
{
    /* printSCP(__FUNCTION__, source_code_position); */
    /* writeLog("%s", "semaphore give failed"); */
}


void onTraceTaskCreate(void* xTask, source_code_position_t scp)
{
    writeLog(EVENT_FORMAT_TASK_USER, (int)xTask, pcTaskGetName(xTask), (int)uxTaskPriorityGet(xTask), scp.file, scp.function, scp.line, "Create");
}


void onTraceTaskDelay(source_code_position_t scp)
{
    /* printSCP(__FUNCTION__, scp); */
}


void onTraceTaskDelayUntil(uint32_t xTickCount, source_code_position_t scp)
{
    writeLog(EVENT_FORMAT_DELAY, xTickCount, scp.file, scp.function, scp.line, "Delay until");
    /* printSCP(__FUNCTION__, scp); */
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


void onTraceTaskSwitchedIn(void* xTask)
{
    char* taskName = pcTaskGetName(xTask);
    if(strcmp(lastName, taskName))
    {
        writeLog(EVENT_FORMAT_TASK_KERNEL, (int)xTask, taskName, (int)uxTaskPriorityGet(xTask), "Task switched in");
        lastName = taskName;
    }
}


void onTraceTaskSwitchedOut(void* xTask)
{
    char* taskName = pcTaskGetName(xTask);
    if(strcmp(lastRemovedName, taskName))
    {
        /* writeLog("switched out %s", pcTaskName); */
        lastRemovedName = taskName;
    }
}
