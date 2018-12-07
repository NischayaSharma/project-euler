import numpy as np;

dimension = 5;
arr = np.zeros((dimension+1,dimension+1));
i=1;
arr[dimension/2][dimension/2]=i;
arr[dimension/2][dimension/2 + 1] = i+1;
arr[dimension/2 + 1][dimension/2 + 1] = i+2;
arr[dimension/2 + 1][dimension/2] = i+3;
arr[dimension/2 + 1][dimension/2 - 1] = i+4;
arr[dimension/2][dimension/2 - 1] = i+5;
arr[dimension/2 - 1][dimension/2 - 1] = i+6;
arr[dimension/2 - 1][dimension/2] = i+7;
arr[dimension/2 - 1][dimension/2 + 1] = i+8;
arr[dimension/2 - 1][dimension/2 + 2] = i+9;
print arr
