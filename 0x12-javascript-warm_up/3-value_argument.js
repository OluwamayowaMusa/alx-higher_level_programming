#!/usr/bin/node

const commandLineArg = process.argv;
if (commandLineArg.length === 2) {
  console.log('No Argument');
} else {
  console.log(commandLineArg[2])
}
