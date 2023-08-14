#!/usr/bin/node

// prints a message depending of the number of arguments passed

const argumentsLength = process.argv.length - 1;

if (argumentsLength === 0) {
  console.log("No argument");
} else if (argumentsLength === 1) {
  console.log("Argument found");
} else {
  console.log("Arguments found");
}
