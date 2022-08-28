/*
Given an array of numbers, return a new array of length number containing the last even numbers from the original array (in the same order). The original array will be not empty and will contain at least "number" even numbers.

For example:

([1, 2, 3, 4, 5, 6, 7, 8, 9], 3) => [4, 6, 8]
([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2) => [-8, 26]
([6, -25, 3, 7, 5, 5, 7, -3, 23], 1) => [6]
*/

function evenNumbers(array, number) {
    let thwee = number; // three = thwee, im tired
    let reverseArr = array.reverse()
    let firstThree = reverseArr.filter(function(x){
      if (thwee > 0){
        if (x % 2 == 0){
          thwee -= 1;
          return true;
        }
      }
      return false;
    })
    return firstThree.reverse();
  }