#!/usr/bin/node

const commandLineArg = process.argv;
if (commandLineArg.length === 2) {
  console.log('No argument');
} else if (commandLineArg.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
