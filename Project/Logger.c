#include <string.h>
#include "FreeRTOS.h"
#include "Logger.h"
#include "task.h"


char* lastName = "";

void doTheThing(char* thing)
{
    if(strcmp(lastName, thing))
    {
        printf("%s\n", thing);
        lastName = thing;
    }
}

void semaphoreTake(void* qwer)
{
    printf("semaphore take\n");
}
void semaphoreTakeFailed(void* qwer)
{
    printf("semaphore take failed\n");
}



void semaphoreGive(void* qwer)
{
    printf("semaphore give\n");
    //printf("%s\n",(char*)qwer);
}
void semaphoreGiveFailed(void* qwer)
{
    printf("semaphore give failed\n");
    //printf("%s\n",(char*)qwer);
}
