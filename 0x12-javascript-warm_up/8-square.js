#!/usr/bin/node

if (!Number(process.argv[2])) {
  console.log('Missing Size');
} else {
  let str = '';
  const size = Number(process.argv[2]);
  for (let i = 0; i < size; i++) { str += 'X'; }
  for (let i = 0; i < size; i++) { console.log(str); }
}
