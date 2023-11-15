#!/usr/bin/node

// Prints a square
// The first argument is the size of the square

const sq = process.argv[2];
const sqSize = parseInt(sq);

if (Number.isNaN(sqSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sqSize; i++) {
    let x = '';
    for (let j = 0; j < sqSize; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
