#include <string.h>
#include <stdio.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"
#include <signal.h>
#include <stdlib.h>



#define writeLog( format, data ) {          \
    vPortEnterCritical();                   \
    fprintf(logFile, format "\n", data);    \
    printf(format "\n", data);              \
    vPortExitCritical();                    \
}

void onInterrupt(int signum)
{
    fclose( logFile );
    exit( 0 );
}

void loggerInit()
{
    signal(SIGINT, onInterrupt);
    logFile = fopen("logFile","w");
}

char* lastName = "";

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
    writeLog("%s", "semaphore give");
    //printf("%s\n",(char*)qwer);
}
void semaphoreGiveFailed(void* qwer)
{
    writeLog("%s", "semaphore give failed");
    //printf("%s\n",(char*)qwer);
}
