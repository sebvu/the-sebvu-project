// add 7 to number using function decleration
function add7(number) {
  return number + 7;
}

// multiply two numbers using function expression w/anon function
let multiply = function (num1, num2) {
  return num1 * num2;
};

// capitalize the first letter of a word using function expression w/arrow function
let capitalize = (word) => word[0].toUpperCase(); // since there are no braces, it implicitly returns it

// return last letter of a word using function expression w/arrow function in multiline
let lastLetter = (word) => {
  return word[word.length - 1];
};

// test cases

console.log(add7(7)); // 14

console.log(multiply(5, 5)); // 25

console.log(capitalize("gaby")); // "Gaby"

console.log(lastLetter("boom")); // "m"
