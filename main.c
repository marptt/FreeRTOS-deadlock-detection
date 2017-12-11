

/* Standard includes. */
#include <stdio.h>
#include <stdlib.h>

#include "FreeRTOS.h"
#include "task.h"
#include "helpers.h"
#include "semphr.h"
#include "logger.h"

/* Define the strings that will be passed in as the task parameters. These are
   defined const and not on the stack to ensure they remain valid when the tasks are
   executing. */
static const char *pcTextForTask1 = "Task 1 (Continuous) is running\r\n";
static const char *pcTextForTask2 = "Task 2 (Continuous) is running\r\n";
static const char *pcTextForTask3 = "Task 3 (Periodic) is running\r\n";

void vContinuousProcessingTask( void *pvParameters );
void vTaskFunction( void *pvParameters );
void continuousPeriodicExample( void );
SemaphoreHandle_t xSemaphore_qwer;


void vContinuousProcessingTask( void *pvParameters )
{
    portTickType xLastWakeTime_qwer;
    xLastWakeTime_qwer = xTaskGetTickCount();

    for( ;; )
    {
        xSemaphoreTake( xSemaphore_qwer, portMAX_DELAY );
        vTaskDelayUntil( &xLastWakeTime_qwer, ( 500 / portTICK_RATE_MS ) );
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



void continuousPeriodicExample( void )
{
    loggerInit();
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask1", 1000, (void*)pcTextForTask1, 1, NULL );
    xTaskCreate( vContinuousProcessingTask, "ContinuousTask2", 1000, (void*)pcTextForTask2, 1, NULL );
    xTaskCreate( vTaskFunction, "PeriodicTask", 1000, (void*)pcTextForTask3, 2, NULL );
   
    xSemaphore_qwer = xSemaphoreCreateMutex();
     
    vTaskStartScheduler();
}





SemaphoreHandle_t xSemaphore_fork_a;
SemaphoreHandle_t xSemaphore_fork_b;
SemaphoreHandle_t xSemaphore_fork_c;

void vPhilosopherTask_a(void *pvParameters)
{
    portTickType xLastWakeTime;
    xLastWakeTime = xTaskGetTickCount();
    for( ;; )
    {
        xSemaphoreTake( xSemaphore_fork_a, portMAX_DELAY );
	vTaskDelayUntil( &xLastWakeTime, ( 3 / portTICK_RATE_MS ) );
        xSemaphoreTake( xSemaphore_fork_b, portMAX_DELAY );
        vTaskDelayUntil( &xLastWakeTime, ( 10 / portTICK_RATE_MS ) );
        xSemaphoreGive( xSemaphore_fork_b );
        xSemaphoreGive( xSemaphore_fork_a );
    }
}

void vPhilosopherTask_b(void *pvParameters)
{
    portTickType xLastWakeTime;
    xLastWakeTime = xTaskGetTickCount();
    for( ;; )
    {
        xSemaphoreTake( xSemaphore_fork_b, portMAX_DELAY );
	vTaskDelayUntil( &xLastWakeTime, ( 5 / portTICK_RATE_MS ) );
        xSemaphoreTake( xSemaphore_fork_c, portMAX_DELAY );
        vTaskDelayUntil( &xLastWakeTime, ( 13 / portTICK_RATE_MS ) );
        xSemaphoreGive( xSemaphore_fork_c );
        xSemaphoreGive( xSemaphore_fork_b );
    }
}

void vPhilosopherTask_c(void *pvParameters)
{
    portTickType xLastWakeTime;
    xLastWakeTime = xTaskGetTickCount();
    for( ;; )
    {
        xSemaphoreTake( xSemaphore_fork_c, portMAX_DELAY );
	vTaskDelayUntil( &xLastWakeTime, ( 7 / portTICK_RATE_MS ) );
        xSemaphoreTake( xSemaphore_fork_a, portMAX_DELAY );
        vTaskDelayUntil( &xLastWakeTime, ( 17 / portTICK_RATE_MS ) );
        xSemaphoreGive( xSemaphore_fork_a );
        xSemaphoreGive( xSemaphore_fork_c );
    }
}

void diningPhilosophersExample( void )
{
    /* As defined by wikipedia: */
    /* think until the left fork is available; when it is, pick it up; */
    /* think until the right fork is available; when it is, pick it up; */
    /* when both forks are held, eat for a fixed amount of time; */
    /* then, put the right fork down; */
    /* then, put the left fork down; */
    /* repeat from the beginning. */
    loggerInit();

    xSemaphore_fork_a = xSemaphoreCreateMutex();
    xSemaphore_fork_b = xSemaphoreCreateMutex();
    xSemaphore_fork_c = xSemaphoreCreateMutex();

    xTaskCreate( vPhilosopherTask_a, "philosopher_a", 1000, NULL, 1, NULL );
    xTaskCreate( vPhilosopherTask_b, "philosopher_b", 1000, NULL, 1, NULL );
    xTaskCreate( vPhilosopherTask_c, "philosopher_c", 1000, NULL, 1, NULL );
   
    //xSemaphore_qwer = xSemaphoreCreateMutex();
     
    vTaskStartScheduler();
}

int main( void )
{
    //continuousPeriodicExample();
    diningPhilosophersExample();
    
    return 0;
}
