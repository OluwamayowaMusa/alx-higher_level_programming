#!/usr/bin/node

exports.converter = function (base) {
  if (base) {
    function convertTobase (num) {
      return num.toString(base);
    }
    return convertTobase;
  }
};
