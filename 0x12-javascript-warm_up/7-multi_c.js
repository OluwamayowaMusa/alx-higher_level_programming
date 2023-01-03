#!/usr/bin/node

if (!Number(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (Number(process.argv[2]) > i) {
    console.log('C is fun');
    i++;
  }
}
