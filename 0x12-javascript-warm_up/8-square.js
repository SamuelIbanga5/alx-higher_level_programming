#!/usr/bin/node
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(args[2]); i++) {
    let x = 'X';
    for (let j = 0; j < parseInt(args[2]) - 1; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
