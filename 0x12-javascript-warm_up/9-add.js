#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const args = process.argv;
add(parseInt(args[2]), parseInt(args[3]));
