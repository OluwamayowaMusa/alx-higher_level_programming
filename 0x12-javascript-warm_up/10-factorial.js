#!/usr/bin/node

function factorial (num) {
  if (num === 1) return 1;
  return num * factorial(num - 1);
}

if (!Number(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorial(Number(process.argv[2])));
}
