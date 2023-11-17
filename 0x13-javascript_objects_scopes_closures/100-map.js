#!/usr/bin/node

 // a script thatImports an array and computes a new array

const pack = require('./100-data');


const NewList = pack.list;

function NewArray (list) {
  const nArr = list.map((value, index) => value * index);
  return nArr;
}

const listtwo = NewArray(NewList);
console.log(newList);
console.log(listtwo);
