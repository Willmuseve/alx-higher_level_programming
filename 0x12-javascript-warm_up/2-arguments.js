#!/usr/bin/node

// prints a message depending of the number of arguments passed

if (process.argv.length > 3) {
  console.log('Arguments found');
} else if (process.argv.lenght === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
