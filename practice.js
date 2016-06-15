var trips = [{name:"Chicago"}]


// retuns the count of number of words in string str1
function countWords(str1){
  var count = 0;
  for (var i = 1; i < str1.length; i++){
      if (str1[i] === " ")
        count++;
  }      
  return count;
}

// returns the reverse string of string str1
function reverse(str1){
  var rev = "";
  for (var i = str1.length - 1; i > -1 ; i--) // decrement
    rev += str1[i];
  return rev;
}
