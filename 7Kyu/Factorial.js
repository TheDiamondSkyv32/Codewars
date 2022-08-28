/*
Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial
*/

function factorial(n){
    if (n === 0)return 1;
    
    let sum = 1;
    while(n > 0){
      sum *= n
      n-=1;
    }
    return sum;
  }