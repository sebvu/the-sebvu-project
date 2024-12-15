/* // console.log("These are my edits");
//
// let age = 11;
// const birth = 2005;
//
// age += 1;
// // birth += 1; Cannot happen as this is a constant, and you can't change when you were born!
//
// console.log(age);
// console.log(birth);
//
// console.log(3 + 2 - 76 * (1 + 1));

/* assignments: */

// add two numbers together
console.log(23 + 97); // 120

// add a sequence of 6 different numbers
console.log((((35 + 62 - 2) / 2) * Math.abs(-5)) % Math.log(10)); // random number

// print the value of the following expression: (4+ 6 + 9) / 77 (value should be 0.24675)
console.log((4 + 6 + 9) / 77);

// using variables!
//  set a = 10 using let then print it
let a = 10;
// print(a);
// now do 9 * a
console.log(9 * a);
// now try typing b = 7 * a (returns undefined) then console.log(b)
// THE REASON WHY IT IS UNDEFINED
/*
because typing 'let b = 7 * a' in console, it will return a undefined because
the console is returning the output of the decleration statmenet which is 
UNDEFINED.

BUT, if you print b then it will actually be its normal number.
*/
let b = 7 * a;
console.log(b);

// Declare a constant variable max with the value 57
// Set another variable actual to max - 13
// Set another variable percentage to actual / max
// If you type percentage in the console and press Enter you should see a value like 0.7719

const max = 57;
const actual = max - 13;
const percentage = actual / max;
console.log(percentage);

/* variables in js assignments */
// declare two variables admin and name
let admin, name;
name = "John";
admin = name;
// alert(admin);
// matched solution

// create a variable with the name of our planet
let planetName;
// solution: ourPlanetName;
// create name to store the name of current visitor to website
let currentVisitor;
// solution: currentUserName;

// uppercase const,
// const birthday = (birthday)
// const age = someCode(birthday)
// should we capitalize both since their const?
//
// NO!!
// only BIRTHDAY could be capitalized since it is HARD CODED
// age is calculated so it should just be a normal camelcase

/* operators

+ (addition)
- (subtraction)
* (multiplication)
** (exponentation) [power of]
/ (division)
% (modulus) [remainder]
++ (increment)
-- (decrement)

== (loose equality) if they both have different datatypes
javascript will attesmpt to convert one of them to match
the other datatype before comparing

=== (strict equality)
compares BOTH value and datatype
>= (greater than)
> (greater than)
<= (less than)
< (less than)

!= (not equal)
!== (strict non equality)

= (assignment operator)

+= (addition assignment)
-= (subtraction assignment)
*= (multiplication assignment)
/= (division assignment)

unary: operation acted on one operand
binary: operation acted on two operands
operand: the value/variable that the operator acts on

let x = 5
x--; (unary operation, the x is the operand being acted on)
x + 5 (binary operation since there are two values, the x and 5 are the operands)

unary can CONVERT non numbers

alert(+true) = 1
alert(+"") = false
does the same as Number() but shorter

(note that unary operations are higher precedence than binary operations)

NEED TO STUDY BITWISE OPERATORS

AND ( & )
OR ( | )
XOR ( ^ )
NOT ( ~ )
LEFT SHIFT ( << )
RIGHT SHIFT ( >> )
ZERO-FILL RIGHT SHIFT ( >>> 

, will allow several expressions to be ran, but the last one is returned

let a = (1 + 2, 3 + 4);

alert( a ); // 7 (the result of 3 + 4)

*/

console.log(0.2 + 0.1); // this will NOT equal 0.3 because of floating point arith.

const TOLERANCE = 1e-10; // amount of tolerance

console.log((0.2 * 10 + 0.1 * 10) / 10); // this will = 0.3

// JS uses + for concatentation
// NaN means not a number when doing stuff like 100 * "Apple"
// But if the string is numeric, smth like 100 * "10"; it will result in a number
// you can use isNan() to find out if its a number or not
let x = 100 / "Apple";
isNaN(x);

const myInt = 5;
const myFloat = 6.667;
myInt;
myFloat;

console.log(typeof myInt);
console.log(typeof myFloat);

const LARGEDECIMALNUMBER = 1.724345624656246756426;
console.log(LARGEDECIMALNUMBER);
const twoDecimalPlaces = LARGEDECIMALNUMBER.toFixed(2); // fixed at 2 points
console.log(twoDecimalPlaces); // turned into a string..?
console.log(typeof twoDecimalPlaces);
// operator precedence is the same as school, PEMDAS <3

// TASKS

let aa = 1,
  bb = 1;
// (prefix and postfix)
let c = ++aa; // ?
let d = bb++; // ?
console.log(aa);
2;
console.log(bb);
2;
console.log(c);
2;
console.log(d);
1;

// c will equal 2, d will equal 1
// correct

/* What are the values of a and x after the code below?

let a = 2;

let x = 1 + (a *= 2); */

// a = 4
// x = 5
// correct

// What are results of these expressions? (type conversions)
/* "" + 1 + 0 = "10" // (1)
"" - 1 + 0 = -1 // (2)
true + false = 1
6 / "3" = 2
"2" * "3" = 6
4 + 5 + "px" = "9px"
"$" + 4 + 5 = "$45"
"4" - 2 = 2
"4px" - 2 = NaN
"  -9  " + 5 = "  -9  5" // (3)
"  -9  " - 5 = -14 // (4)
null + 1 = 1 // (5)
undefined + 1 = NaN // (6)
" \t \n" - 2 = -2 // (7) */

console.log(4 + 5 + "px"); // 9px
console.log(4 + 5 + "px" - 6);
// NaN, but if the - was a + it would be a string concatentation so it would be 9px6
