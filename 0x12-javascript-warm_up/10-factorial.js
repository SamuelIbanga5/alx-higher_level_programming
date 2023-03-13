#!/usr/bin/node
function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}
const args = process.argv;
console.log(factorial(parseInt(args[2])));
