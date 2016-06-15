var trips = [{name:"Chicago", season:"summer", activity1:"music festival", activity2:"bean"},
              {name:"Hong Kong", season:"fall", activity1:"Ocean Park", activity2:"Disney"},
              {name:"Philadelphia", season:"spring", activity1:"go to school", activity2:"ride the train"}
];

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
