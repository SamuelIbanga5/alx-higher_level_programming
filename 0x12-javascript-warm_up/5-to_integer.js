#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Not a number');
} else {
  const integer = parseInt(args[2]);
  console.log('My number: ' + integer);
}
