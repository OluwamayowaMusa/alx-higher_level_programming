#!/usr/bin/node

const commandLineArg = process.argv;
if (commandLineArg.size === 2) {
  console.log('No argument');
} else {
  console.log(commandLineArg[2]);
}
