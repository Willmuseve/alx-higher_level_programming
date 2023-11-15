#!/usr/bin/node

// Prints addition of 2 integers

function add (a, b) {
  return a + b;
}

const fInt = parseInt(process.argv[2]);
const sInt = parseInt(process.argv[3]);

if (Number.isNaN(fInt) || Number.isNaN(sInt)) {
  console.log('NaN');
} else {
  const sum = add(fInt, sInt);
  console.log(sum);
}
