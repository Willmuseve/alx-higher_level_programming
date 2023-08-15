#!/usr/bin/node

const firstA = process.argv[2];

if (firstA === undefined) {
  console.log("No argument");
} else {
  console.log(firstA);
}
