// Practicing with Objects

var trips = [{name:"Chicago", season:"summer", activity1:"music festival", activity2:"bean"},
              {name:"Hong Kong", season:"spring", activity1:"Ocean Park", activity2:"Disney"},
              {name:"Philadelphia", season:"fall", activity1:"go to school", activity2:"ride the train"}
];

// alternatively
var trip1 = new Object();
trip1.name = "Chicago";
trip1.season = "summer";
trip1.activity1 = "music festival";
trip1.activity2= "bean";

// alternatively
function trip(name, season, activity1, activity2) {
  this.name = name;
  this.season = season;
  this.activity1 = activity1;
  this.activity2 = activity2;
}

var tripNo1 = new trip("Chicago", "summer", "music festival", "bean");

// retuns the count of number of words in string str1
function countWords(str1){
  var count = 1;
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
