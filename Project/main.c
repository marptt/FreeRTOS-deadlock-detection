

/* Standard includes. */
#include <stdio.h>
#include <stdlib.h>

#include "FreeRTOS.h"
#include "task.h"
#include "helpers.h"


/* Define the strings that will be passed in as the task parameters. These are
   defined const and not on the stack to ensure they remain valid when the tasks are
   executing. */
static const char *pcTextForTask1 = "Task 1 (Continuous) is running\r\n";
static const char *pcTextForTask2 = "Task 2 (Continuous) is running\r\n";
static const char *pcTextForTask3 = "Task 3 (Periodic) is running\r\n";

void vContinuousProcessingTask( void *pvParameters );
void vTaskFunction( void *pvParameters );

void vContinuousProcessingTask( void *pvParameters )
{
    /* char *pcTaskName; */
    /* The string to print out is passed in via the parameter. Cast this to a
       character pointer. */
    /* pcTaskName = ( char * ) pvParameters; */
    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Print out the name of this task. This task just does this repeatedly
           without ever blocking or delaying. */
        /* vPrintString( pcTaskName ); */
    }
}

void vTaskFunction( void *pvParameters )
{
    char *pcTaskName;
    portTickType xLastWakeTime;
    /* The string to print out is passed in via the parameter. Cast this to a
       character pointer. */
    pcTaskName = ( char * ) pvParameters;
    /* The xLastWakeTime variable needs to be initialized with the current tick
       count. Note that this is the only time the variable is written to explicitly.
       After this xLastWakeTime is updated automatically internally within
       vTaskDelayUntil(). */
    xLastWakeTime = xTaskGetTickCount();
    /* As per most tasks, this task is implemented in an infinite loop. */
    for( ;; )
    {
        /* Print out the name of this task. */
        vPrintString( pcTaskName );
        /* This task should execute exactly every 250 milliseconds. As per
           the vTaskDelay() function, time is measured in ticks, and the
           portTICK_RATE_MS constant is used to convert milliseconds into ticks.
           xLastWakeTime is automatically updated within vTaskDelayUntil() so is not
           explicitly updated by the task. */
        vTaskDelayUntil( &xLastWakeTime, ( 250 / portTICK_RATE_MS ) );
    }
}

int main( void )
{
    /* Create the first task at priority 1. 
       parameter. */
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask1", 1000, (void*)pcTextForTask1, 1, NULL );
    /* Create the second task at priority 1. */
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask2", 1000, (void*)pcTextForTask2, 1, NULL );
    /* Create the second task at priority 2. */
    xTaskCreate( vTaskFunction, "PeriodicTask", 1000, (void*)pcTextForTask3, 2, NULL );
    /* Start the scheduler so the tasks start executing. */
    vTaskStartScheduler();
    return 0;
}

