
#include "FreeRTOS.h"
#include "Logger.h"

void doTheThing(char* thing)
{
    printf("%i\n", testNum++);
    printf("%s \n", thing);
}
