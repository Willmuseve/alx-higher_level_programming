#!/usr/bin/node

// a script that prints the first argument passed

const argument = process.argv[2];

if (argument === undefined) {
  console.log('No argument');
} else {
  console.log(argument);
}
