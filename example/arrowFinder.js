function sequenceFactory(length) {
  let sequence = '';

  for (let i = 0; i < length; ++i) {
    switch (Math.floor(Math.random() * 1000) % 3) {
      case 0:
        sequence += '=';
        break;
      case 1:
        sequence += '<';
        break;
      case 2:
        sequence += '>';
        break;
      default:
        break;

    }
  }

  return sequence;
}

function arrowsFinder(str) {
  let count = 0;

  const leftArrows = [];
  const rightArrows = [];

  const leftArrowsSteps = '<==<<';
  const rightArrowsSteps = '>>==>';

  for(let i = 0; i < str.length; ++i) {
    let j = 0;
    while (j < leftArrows.length) {
      if (leftArrowsSteps[leftArrows[j] + 1] === str[i]) {
        ++leftArrows[j];
        if (leftArrows[j] === 4) {
          ++count;
          leftArrows.splice(j, 1);
        } else {
          ++j;
        }
      } else {
        leftArrows.splice(j, 1);
      }
    }
    j = 0;
    while (j < rightArrows.length) {
      if (rightArrowsSteps[rightArrows[j] + 1] === str[i]) {
        ++rightArrows[j];
        if (rightArrows[j] === 4) {
          ++count;
          rightArrows.splice(j, 1);
        } else {
          ++j;
        }
      } else {
        rightArrows.splice(j, 1);
      }
    }
    
    if (leftArrowsSteps[0] === str[i]) {
      leftArrows.push(0);
    }
    
    if (rightArrowsSteps[0] === str[i]) {
      rightArrows.push(0);
    }
  }

  return count
}

function getRightAnswer(str) {
  let count = 0;
  let i = -1;
  while ((i = str.indexOf('>>==>', i + 1)) !== -1 && ++count);
  i = -1;
  while ((i = str.indexOf('<==<<', i + 1)) !== -1 && ++count);

  return count;
}

module.exports = {
  arrowsFinder,
  sequenceFactory,
  getRightAnswer,
};
