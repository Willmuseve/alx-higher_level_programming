#!/usr/bin/node

//prints message depending on the number of args passed

const argsco = process.argv.length;

if (argsco > 2) {
  console.log('Argument' + (argc > 3 ? 's' : '') + ' found');
} else {
  console.log('No argument');
}
