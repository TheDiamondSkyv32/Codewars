"""
Consecutive Strings
You are given an array(list) strarr of strings and an integer k. Your task is to return the first longest string consisting of k consecutive strings taken in the array.

Examples:
strarr = ["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz"], k = 2

Concatenate the consecutive strings of strarr by 2, we get:

treefoling   (length 10)  concatenation of strarr[0] and strarr[1]
folingtrashy ("      12)  concatenation of strarr[1] and strarr[2]
trashyblue   ("      10)  concatenation of strarr[2] and strarr[3]
blueabcdef   ("      10)  concatenation of strarr[3] and strarr[4]
abcdefuvwxyz ("      12)  concatenation of strarr[4] and strarr[5]

Two strings are the longest: "folingtrashy" and "abcdefuvwxyz".
The first that came is "folingtrashy" so 
longest_consec(strarr, 2) should return "folingtrashy".

In the same way:
longest_consec(["zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"], 2) --> "abigailtheta"
n being the length of the string array, if n = 0 or k > n or k <= 0 return "" (return Nothing in Elm, "nothing" in Erlang).

Note
consecutive strings : follow one after another without an interruption
"""

def longest_consec(strarr, k):
    """My implementation"""
    
    if k<=0 or k>len(strarr): # base criteria needed for our function to work 
        return ""
    
    buildString = "" # build our string with this temp variable
    returnString = ""  
    
    for count, str in enumerate(strarr): 
        iterString = iter(strarr[count:]) # create an Iterator object but remove the elements we've already seen
        
        for _ in range(k): # max number of strings to concatenate 
            stringItem = next(iterString, 0) # grab next item in array
            
            try:
                buildString += stringItem
                
            except: # the only time we reach this Exception is when our Iterator object reaches its end, meaning end of the array
                return returnString # return the largest pair we found thus far
            
        if (len(buildString) > len(returnString)): 
            returnString = buildString # if a larger consecutive string pair arrives, set our return value to it
        buildString = "" 
        
    return returnString
           
