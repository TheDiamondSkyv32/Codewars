/* 
Write Number in Expanded Form

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expandedForm(12); // Should return '10 + 2'
expandedForm(42); // Should return '40 + 2'
expandedForm(70304); // Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0.
*/

function expandedForm(num) {
  // Your code here
  let strNum = String(num)
  let stringPlaceholder = ""
  
  let numOfZeroes = strNum.length-1;
  for (let i = 0; i < strNum.length; i++){
    if ((strNum[i] == 0)){ // we don't pad 0s with more 0s, skip iteration
      numOfZeroes -= 1;
      continue
    }
    stringPlaceholder += strNum[i] + "0".repeat(numOfZeroes) + " "
    numOfZeroes -= 1;
  }
  let formatString = stringPlaceholder.trim().split(" ").join(" + ") 
  return formatString

}