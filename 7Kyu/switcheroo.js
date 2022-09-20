/*
Given a string made up of letters a, b, and/or c, switch the position of letters a and b (change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
*/

function switcheroo(x){
  let newStr = ""
  
  for (let i = 0; i < x.length; i++){
    if (x[i] === 'a'){
      newStr += "b";
      }
      else if (x[i] === 'b'){
      newStr += "a"
      }
    else{
      newStr += x[i];
      }
    }
  return newStr;
}
