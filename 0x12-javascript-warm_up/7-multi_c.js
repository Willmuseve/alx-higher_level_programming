#!/usr/bin/node

//a script that prints x times "C is fun"

const numb = process.argv[2];

if (!parseInt(numb) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numb; i++) {
    console.log('C is fun');
  }
}
