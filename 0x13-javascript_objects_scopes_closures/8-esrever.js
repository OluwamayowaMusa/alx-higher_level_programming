#!/usr/bin/node

exports.esrever = function (list) {
  const tmp = [];
  for (const i of list) {
    tmp.unshift(i);
  }
  return tmp;
};
