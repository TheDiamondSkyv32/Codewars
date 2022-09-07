/*
Find the sum of the odd numbers within an array, after cubing the initial integers. The function should return undefined if any of the values aren't numbers.
*/

function cubeOdd(arr) {
  const isNum = (element) => Number.isInteger(element) === false;
  if (arr.some(isNum))return undefined
  let oddNums = arr.filter(x => x % 2 !==0);
  oddNums = oddNums.map(x=> x**3);
  
  if (!Array.isArray(oddNums)) return undefined
  let sumNums = oddNums.reduce( (total, curr) => total += curr, 0)
  return sumNums
}

