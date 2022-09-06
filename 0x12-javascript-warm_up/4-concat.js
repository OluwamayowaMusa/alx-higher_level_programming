#!/usr/bin/node
import { argv } from 'node:process';

const myVar = argv[2] + ' is ' + argv[3];
console.log(myVar);
