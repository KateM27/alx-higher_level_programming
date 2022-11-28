#!/usr/bin/node
function add(a, b) {
sum = a + b;
return sum
}

const args = process.argv;
console.log(add(Number(args[2]), Number(args[3])));
