int solution(int N)
{
// write your code in C++11 (g++ 4.8.2)

    int countZero = 0, maxZero = 0;
    bool isStarted = false;
    bool bit;
    do
    {        
        bit = N % 2;
        if(bit)
        {
            if (isStarted)
            {
                maxZero = max(maxZero, countZero);
            }
            countZero = 0;
            isStarted = true;
        }
        else
        {
            countZero++;
        }
        N = N / 2;
    }
    while (N != 0);

    return maxZero;
}