#!/usr/bin/node

// a script prints My number: 
// <first argument converted in integer>
// if the first argument can be converted to an integer

const myNum = process.argv[2];
const Num2 = parseInt(myNum);

if (!Number.isNaN(Num2) && Number.isInteger(Num2)) {
  console.log('My number: ' + Num2);
} else {
  console.log('Not a number');
}
