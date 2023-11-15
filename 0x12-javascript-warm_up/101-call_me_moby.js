#!usr/bin/node

// a script that executes x times a function

exports.callMeMoby = function (x, theFunction) {
  for (let k = 0; k < x; k++) {
    theFunction();
  }
};
