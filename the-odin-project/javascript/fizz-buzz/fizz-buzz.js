// take in user input
// print numbers from 1 to what the user entered
// for multiples of 3, print fizz
// for multiples of 5, print buzz
// for multiples of both 3 AND 5, print fizzbuzz
// if neither, then just print the number
// if the number is not valid, then re-prompt

// const answer = parseInt(prompt("Please enter a number above 1."))

let answer = 100;

if (answer >= 1) {
  for (let i = 1; i <= answer; i++) {
    if (i % 3 === 0 && i % 5 === 0) {
      console.log("FizzBuzz");
    }
    if (i % 3 === 0) {
      console.log("Fizz");
    } else if (i % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
} else {
  console.log("Please input a number above or equal to 1!")
}
