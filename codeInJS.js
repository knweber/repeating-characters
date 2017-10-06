function repeats(str) {
  var max = 0;
  var ans = "";
  var words = str.split(" ");

  for(var i = 0; i < words.length; i++) {

    var letters = [];

    for(var j = 0; j < words[i].length; j++) {
      letters.push(words[i][j].toLowerCase());
    }

    var hashInstances = letters.reduce(function(instances,a) {
      if(a in instances) {
        instances[a]++;
      } else {
        instances[a] = 1;
      }
      return instances;
    }, {})

    var countsPerWord = Object.values(hashInstances);
    var mostPerWord = Math.max(...countsPerWord);

    if(mostPerWord > max) {
      max = mostPerWord;
      ans = words[i];
    }

  }
  return(ans);
}

repeats("Some people feel the rain, while others just get wet.");
