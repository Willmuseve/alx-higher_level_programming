#!/usr/bin/node

// prints two arguments passed to it

const argum1 = process.argv[2];
const argum2 = process.argv[3];

if (argum1 === undefined) {
  console.log(argum1 + ' is ' + argum2);
} else {
  console.log(argum1 + ' is ' + argum2);
}
