#!/usr/bin/node

const smore = process.argv[2];

if (!parseInt(smore)) {
  console.log('Missing size');
} else {
  for (let j = 0; j < smore; j++) {
    let k = 0;
    let l = '';

    while (k < smore) {
      l = l + 'X';
      k++;
    }
    console.log(l);
  }
}
