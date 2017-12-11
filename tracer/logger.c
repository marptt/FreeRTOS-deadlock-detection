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
#define writeLog( format, data... ) {                                  \
    vPortEnterCritical();                                              \
    sigprocmask(SIG_BLOCK, &signal_set, NULL);                         \
    fprintf(logFile, format",\n", data, xTaskGetTickCount());		   \
    sigprocmask(SIG_UNBLOCK, &signal_set, NULL);                       \
    vPortExitCritical();                                               \
}
	/* printf( format",\n", data, xTaskGetTickCount());				   \ */


#define EVENT_FORMAT_SEMAPHORE					\
	"{\n"										\
	"    \"Event Type\": \"SEMAPHORE\",\n"		\
	"    \"Event\": \"%s\",\n"					\
	"    \"Handle\": %i,\n"						\
	"    \"File\": \"%s\",\n"					\
	"    \"Function\": \"%s\",\n"				\
	"    \"Line\": %i,\n"						\
	"    \"Tick\": %i\n"						\
	"}"											\


#define EVENT_FORMAT_DELAY						\
	"{\n"										\
	"    \"Event Type\": \"DELAY\",\n"			\
	"    \"Event\": \"%s\",\n"					\
	"    \"Duration\": %i,\n"					\
	"    \"File\": \"%s\",\n"					\
	"    \"Function\": \"%s\",\n"				\
	"    \"Line\": %i,\n"						\
	"    \"Tick\": %i\n"						\
	"}"											\

#define EVENT_FORMAT_TASK_KERNEL				\
	"{\n"										\
	"    \"Event Type\": \"TASK KERNEL\",\n"	\
	"    \"Event\": \"%s\",\n"					\
	"    \"Task Handle\": %i,\n"				\
	"    \"Task Name\": \"%s\",\n"				\
	"    \"Task Priority\": %d,\n"				\
	"    \"Tick\": %i\n"						\
	"}"											\

#define EVENT_FORMAT_TASK_USER					\
	"{\n"										\
	"    \"Event Type\": \"TASK USER\",\n"		\
	"    \"Event\": \"%s\",\n"					\
	"    \"Task Handle\": %i,\n"				\
	"    \"Task Name\": \"%s\",\n"				\
	"    \"Task Priority\": %d,\n"				\
	"    \"File\": \"%s\",\n"					\
	"    \"Function\": \"%s\",\n"				\
	"    \"Line\": %i,\n"						\
	"    \"Tick\": %i\n"						\
	"}"											\

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
	fprintf(logFile, "{\n    \"Event Type\": \"The End\",\n    \"Tick\": %i\n}]}\n", xTaskGetTickCount());
	fclose( logFile );
}

void loggerInit()
{
    sigemptyset(&signal_set);
    sigaddset(&signal_set, SIGINT);
    signal(SIGINT, onInterrupt); /* SIGINT, triggered by Ctrl+C */
    logFile = fopen("logFile","w");
    fprintf(logFile, "{\"log\":[");
}


void printSCP( const char* function, source_code_position_t scp )
{
	printf( "%s:\t '%s','%s()','%i'\n", function, scp.file, scp.function, scp.line );
}




/* ###### Trace functions ###### */

void onTraceBlockingOnQueueReceive (void* xQueue, source_code_position_t scp)
{
	/* printf("Task \"%s\" blocked from sema '%s': ", pcTaskGetName(xTaskGetCurrentTaskHandle()), (char*)pcQueueGetName(xQueue) ); */
	/* printf("%s:\n",pcQueueGetName(xQueue)); */
	
	writeLog(EVENT_FORMAT_SEMAPHORE, "Blocked on Take",(int)xQueue, scp.file, scp.function, scp.line);
	/* printSCP(__FUNCTION__, scp); */
}

void onTraceBlockingOnQueueSend(void* xQueue, source_code_position_t source_code_position )
{
	/* printSCP(__FUNCTION__,source_code_position); */
}


void onTraceCreateMutex(void* pxNewMutex, source_code_position_t scp)
{
    /* nrSemaCreated++; */
	/* char* text = "Mutex_"; */
	/* char* line = (char *)malloc( scp.line/10 + 1 ); */
	/* /\* char* nr = (char *)malloc( nrSemaCreated/10 + 1 ); *\/ */
	/* sprintf(line, "%d", scp.line); */
	/* /\* sprintf(nr, "%d", nrSemaCreated); *\/ */
	/* char *out; */
	/* /\* out = (char *)malloc(strlen(text) + strlen(scp.)  +strlen(line) + 1); *\/ */
	/* strcpy(out, text); */
	/* strcat(out, nr); */
	/* vQueueAddToRegistry(pxNewMutex,out);	 */
	
	/* printSCP(__FUNCTION__,scp); */
	writeLog(EVENT_FORMAT_SEMAPHORE, "Mutex created",(int)pxNewMutex, scp.file, scp.function, scp.line);
}


void onTraceMovedTaskToReadyState(void* xTask)
{
	writeLog(EVENT_FORMAT_TASK_KERNEL, "Moved to ready", (int)xTask, pcTaskGetName(xTask), (int)uxTaskPriorityGet(xTask));
}


void onTraceQueueReceive(void* xQueue, source_code_position_t scp )
{
    writeLog(EVENT_FORMAT_SEMAPHORE, "Take", (int)xQueue, scp.file, scp.function, scp.line);
   	/* printSCP(__FUNCTION__, scp); */
}


void onTraceQueueReceiveFailed(void* xQueue, source_code_position_t scp)
{
    writeLog(EVENT_FORMAT_SEMAPHORE, "Failed take - time out", (int)xQueue, scp.file, scp.function, scp.line);
}


void onTraceQueueSend(void* xQueue, source_code_position_t scp)
{
    /* printf("semaphore '%s' give: ", (char*)pcQueueGetName(xQueue)); */
	/* printSCP(__FUNCTION__, scp); */
	writeLog(EVENT_FORMAT_SEMAPHORE, "Semaphore give",(int)xQueue, scp.file, scp.function, scp.line);
}


void onTraceQueueSendFailed(void* xQueue, source_code_position_t source_code_position)
{
	/* printSCP(__FUNCTION__, source_code_position); */
	/* writeLog("%s", "semaphore give failed"); */
}


void onTraceTaskCreate(void* xTask, source_code_position_t scp)
{
	writeLog(EVENT_FORMAT_TASK_USER, "Create", (int)xTask, pcTaskGetName(xTask), (int)uxTaskPriorityGet(xTask), scp.file, scp.function, scp.line);
    /* printf("Lala: %s\n", pcTaskGetName(xTask)); */
}


void onTraceTaskDelay(source_code_position_t scp)
{
	/* printSCP(__FUNCTION__, scp); */
}


void onTraceTaskDelayUntil(uint32_t xTickCount, source_code_position_t scp)
{
	int a = 10;
	writeLog(EVENT_FORMAT_DELAY, "Delay until", xTickCount, scp.file, scp.function,scp.line);
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
        writeLog(EVENT_FORMAT_TASK_KERNEL, "Task switched in", (int)xTask, taskName, (int)uxTaskPriorityGet(xTask));
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
