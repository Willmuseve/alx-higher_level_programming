#!/usr/bin/node

const parg = process.argv[2];

if (!parseInt(parg)) {
  console.log('Missing number of occurrences');
} else {
  for (let j = 0; j < parg; j++) {
    console.log('C is fun');
  }
}
