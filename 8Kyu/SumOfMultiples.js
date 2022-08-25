/*
Your Job
Find the sum of all multiples of n below m

Keep in Mind
n and m are natural numbers (positive integers)
m is excluded from the multiples
*/ 

function sumMul(n,m){
    if (m <= n || n == 0) return "INVALID";
    
    let incrAmount = n;
    let total = 0;
    while(incrAmount < m){
      total += incrAmount;
      incrAmount += n;
    }
    return total; 
  }