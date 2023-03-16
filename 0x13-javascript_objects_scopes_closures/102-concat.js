#!/usr/bin/node
const args = process.argv;
const fs = require('fs');
const a = fs.readFileSync(args[2], 'utf8');
const b = fs.readFileSync(args[3], 'utf8');
fs.writeFileSync(args[4], a + b);
