//exercicio 01 - Crie um algoritmo que imprima na tela o fatorial de 10.

// let number = 1;

// for( let index = 10; index > 0; index -= 1) {
//     number *= index;
// }

// console.log(number);



// exercicio 02 - Utilize a estrutura de repetição for para desenvolver um algoritmo que seja capaz de inverter uma palavra. Por exemplo, a palavra “banana” seria invertida para “ananab”. Utilize a string abaixo como exemplo, depois troque por outras para verificar se seu algoritmo está funcionando corretamente.

// let word = 'tryber';

// let letter = '';

// for (let index = 0; index < word.length; index +=1) {
//     letter += word[word.length - 1 - index];
// }
// console.log(letter);

let word = 'tryber';
let reverseWord = '';

reverseWord = word.split('').reverse().join('');

console.log(reverseWord);


// exercicio 03 - Considere o array de strings abaixo, utilize a estrutura de repetição for para escrever dois algoritmos: um que imprima no console a maior palavra desse array e outro que imprima a menor. Considere o número de caracteres de cada palavra.

// let array = ['java', 'javascript', 'python', 'html', 'css'];

//exercicio 04 - Um número primo é um número inteiro maior do que 1 que possui somente dois divisores, ou seja, é divisível por 1 e por ele mesmo. Sabendo disso, escreva um algoritmo que imprima no console o maior número primo entre 2 e 50.