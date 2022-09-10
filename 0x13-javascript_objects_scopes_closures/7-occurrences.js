#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let numOfOcccurence = 0;
  for (const i of list) {
    if (i === searchElement) numOfOcccurence++;
  }
  return numOfOcccurence;
};
