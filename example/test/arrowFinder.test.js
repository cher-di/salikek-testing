const {assert} = require('chai');
const {
  arrowsFinder,
  sequenceFactory,
  getRightAnswer
} = require('../arrowFinder');

String.prototype.replaceAt = function(index, replacement) {
  return this.substr(0, index) + replacement + this.substr(index + replacement.length);
};

const EXAMPLES = {
  '>>==>': 1,
  '<==<<': 1,
  '>>==>>==>': 2,
  '<==<<==<<': 2,
  '>>==><==<<': 2,
  '<==<<>>==>': 2,
  '>>>>>>>==>>>>>>>>': 1,
  '<<<<<<<==<<<<<<<<': 1,
  '>>==>>==>>==>': 3,
  '<==<<==<<==<<': 3,
}

describe('Тесты для arrowFinder:', () => {
  describe('Тесты на готовых случаях:', () => {
    Object.keys(EXAMPLES).map(str => {
      it(`Строка ${str}`, () => {
        assert.equal(arrowsFinder(str), EXAMPLES[str]);
      });
    });
  });

  describe('Тесты на строках с ошибками: ', () => {
    Object.keys(EXAMPLES).slice(0, 3).map(str => {
      describe(`Тесты с ошибками в строке ${str}:`, () => {
        for (let j = 0; j < str.length; ++j) {
          const newStr = str.replaceAt(j, '0');
          it(`Строка ${newStr}`, () => {
            assert.equal(arrowsFinder(newStr), getRightAnswer(newStr));
          });
        }
      });
    });
  });

  describe('Тесты на случайно сгенерированых строках:', () => {
    for (let i = 0; i < 5; ++i) {
      const str = sequenceFactory(50 + i);
      it(`Строка ${str}`, () => {
        assert.equal(arrowsFinder(str), getRightAnswer(str)); 
      })
    }
  });
});

