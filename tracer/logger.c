#include <string.h>
#include "FreeRTOS.h"
#include "logger.h"
#include "task.h"


char* lastName = "";
int nrSemaCreated = 0;

void taskSwitchedIn(char* thing)
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
    printf("semaphore give: %s\n", (char*)pcQueueGetName(qwer));
}
void semaphoreGiveFailed(void* qwer)
{
    printf("semaphore give failed\n");
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
