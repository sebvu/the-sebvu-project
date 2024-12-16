console.log("Begin");

let input = prompt("Who's there?");

if (input == "Admin") {
  let password = prompt("Password?");
  if (password == "TheMaster") {
    console.log("Welcome!");
  } else if (password == "Cancel") {
    console.log("Canceled");
  } else {
    console.log("Wrong password");
  }
} else if (input == "Cancel") {
  console.log("Canceled");
} else {
  console.log("I don't know you");
}

// NOTES: Should use === expression
