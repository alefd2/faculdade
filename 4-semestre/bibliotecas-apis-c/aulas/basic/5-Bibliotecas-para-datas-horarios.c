#include <stdio.h>
#include <time.h>

// horarios
int main()
{
       // Get current time
       time_t currentTime;
       time(&currentTime);

       // Convert to local time structure
       struct tm *localTime = localtime(&currentTime);

       // Print formatted date and time
       printf("Current Date: %02d/%02d/%d\n",
              localTime->tm_mday,
              localTime->tm_mon + 1,
              localTime->tm_year + 1900);

       printf("Current Time: %02d:%02d:%02d\n",
              localTime->tm_hour,
              localTime->tm_min,
              localTime->tm_sec);

       // Using strftime for formatted output
       char dateStr[100];
       strftime(dateStr, sizeof(dateStr), "Formatted date: %A, %B %d, %Y", localTime);
       printf("%s\n", dateStr);

       return 0;
}

// graficos