#!/usr/bin/node

// prints x times c if dfun

const numb = process.argv[2];
const numb2 = parseInt(numb);

if (Number.isNaN(numb2)) {
  console.log('Missing number of occurrences');
} else {
  let j = numb2;
  while (j > 0) {
    console.log('C is fun');
    j--;
  }
}
