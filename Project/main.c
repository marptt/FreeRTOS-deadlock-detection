

/* Standard includes. */
#include <stdio.h>
#include <stdlib.h>

#include "FreeRTOS.h"
#include "task.h"
#include "helpers.h"
#include "semphr.h"

/* Define the strings that will be passed in as the task parameters. These are
   defined const and not on the stack to ensure they remain valid when the tasks are
   executing. */
static const char *pcTextForTask1 = "Task 1 (Continuous) is running\r\n";
static const char *pcTextForTask2 = "Task 2 (Continuous) is running\r\n";
static const char *pcTextForTask3 = "Task 3 (Periodic) is running\r\n";

void vContinuousProcessingTask( void *pvParameters );
void vTaskFunction( void *pvParameters );


SemaphoreHandle_t xSemaphore_qwer;


void vContinuousProcessingTask( void *pvParameters )
{
    portTickType xLastWakeTime_qwer;
    xLastWakeTime_qwer = xTaskGetTickCount();

    for( ;; )
    {
        xSemaphoreTake( xSemaphore_qwer, portMAX_DELAY );
        vTaskDelayUntil( &xLastWakeTime_qwer, ( 1000 / portTICK_RATE_MS ) );
        xSemaphoreGive( xSemaphore_qwer );
        //vTaskDelayUntil( &xLastWakeTime_qwer, ( 1 / portTICK_RATE_MS ) );
    }
}

void vTaskFunction( void *pvParameters )
{
    char *pcTaskName;
    portTickType xLastWakeTime;
    pcTaskName = ( char * ) pvParameters;
    xLastWakeTime = xTaskGetTickCount();
    for( ;; )
    {
        vTaskDelayUntil( &xLastWakeTime, ( 250 / portTICK_RATE_MS ) );
    }
}

int main( void )
{
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask1", 1000, (void*)pcTextForTask1, 1, NULL );
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask2", 1000, (void*)pcTextForTask2, 1, NULL );
    xTaskCreate( vTaskFunction, "PeriodicTask", 1000, (void*)pcTextForTask3, 2, NULL );
   
    xSemaphore_qwer = xSemaphoreCreateMutex();
    
    vTaskStartScheduler();
    return 0;
}

