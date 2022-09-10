#!/usr/bin/node

exports.logMe = function (item) {
  if (item) {
    console.log(`${exports.logMe.num}: ${item}`);
    exports.logMe.num++;
  }
};
exports.logMe.num = 0;
