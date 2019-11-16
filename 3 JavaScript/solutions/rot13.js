const readline = require('readline-sync');

let rotation = parseInt(readline.question('enter the rotation: '));
const answer = readline.question('enter a string: ');

let lowerLetters = 'abcdefghijklmnopqrstuvwxyz';
let upperLetters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

let convertedString = '';

if (rotation < 0) {
    lowerLetters = lowerLetters.split("").reverse().join("");
    upperLetters = upperLetters.split("").reverse().join("");
    rotation = Math.abs(rotation);
}

for (i = 0; i < answer.length; i++) {
    index = lowerLetters.indexOf(answer[i]);   

    if (index !== -1)
        convertedString += lowerLetters[(index + rotation) % 26];
    else if (index === -1) {
        index = upperLetters.indexOf(answer[i]);
        if (index === -1)
            convertedString += answer[i];
        else
            convertedString += upperLetters[(index + rotation) % 26];
    }
}

console.log(convertedString);