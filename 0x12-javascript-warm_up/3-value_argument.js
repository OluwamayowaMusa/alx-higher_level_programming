#!/usr/bin/node
import { argv } from 'node:process';

if (argv[1]) {
  console.log(argv[1]);
} else {
  console.log('No argument');
}
