#!/usr/bin/node

//a program that Computes factorial of a number n

function factorial (n) {
  if (isNaN(n)) {
    return 1;
  }

  if (n === 0 || n === 1) {
    return 1;
  }

  return n * factorial(n - 1);
}

const numb = parseInt(process.argv[2]);
const ret = factorial(numb);

console.log(ret);
