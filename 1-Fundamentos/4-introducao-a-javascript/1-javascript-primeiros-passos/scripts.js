// exercicio 1 Ver o maior entre 2
// const num1 = 10;

// const num2 = 20;

// if ( num1 > num2 ){
//     console.log( num1 );
// }
// else {
//     console.log( num2 );
// }

// exercicio 2 Compara 3 numeros para o maior
// const num1 = 10;

// const num2 = 20;

// const num3 = 45;

// if ( num1 > num2 && num1 > num3){
//     console.log( num1 );
// }
// else if ( num2 > num1 && num2 > num3 ) {
//     console.log( num2 );
// }

// else {
//     console.log( num3 );
// }

//exercicio 3 Positivo/Negativo
// let num1 = -5;

// if ( num1 > 0) {
//     console.log("Positive");
// }
// else if ( num1 < 0){
//     console.log("Negative");
// } 
// else {
//     console.log('zero');
// }

//exercicio 4 
// const angle1 = 50;

// const angle2 = 90;

// const angle3 = -40;

// let sumAngle = angle1 + angle2 + angle3;

// let positives = angle1 >0 && angle2 >0 && angle3 >0;

// if ( positives ){
//     if ( sumAngle === 180 ){
//         console.log(true);
//     }
//     else {
//         console.log(false);
//     };
// }
// else {
//         console.log('Erro: Angulo negativo');
// }

//exercicio 5
// const chessPiece = 'PeãO';

//     switch (chessPiece.toLowerCase()) {
//         case 'peão':
//             console.log('Se move apenas para a frente');
//             break;
        
//         case 'torre':
//             console.log('Qualquer numero de casas para frente ou lados')
//             break;

//         case 'bispo':
//             console.log('Qualquer numero de casas na Diagonal');
//             break;

//         case 'rainha':
//             console.log('Quantas casas quiser em qualquer direção');
//             break;

//         case 'rei':
//             console.log('Uma casa em qualquer direção');
//             break;
        
//         default:
//             console.log('Peça Inválida');
//     }

//exercicio 6
// const nota = 100;

//     if (nota >= 90 && nota < 100 ) {
//         console.log('A');
//     }
//     else if ( nota >= 80 && nota < 90 ){
//         console.log('B');
//     }
//     else if ( nota >= 70 && nota < 80 ){
//         console.log('C');
//     }
//     else if ( nota >= 60 && nota < 70 ){
//         console.log('D');
//     }
//     else if ( nota >= 50 && nota < 60 ){
//         console.log('E');
//     }
//     else if ( nota < 50 ){
//         console.log('F');
//     }
//     else {
//         console.log('Error')
//     }

//exercicio 7
// const num1 = 10;

// const num2 = 17;

// const num3 = 33;

// if ( num1 %2 === 0 || num2 % 2 === 0 || num3 % 2 === 0) {
//     console.log('true');
// }
// else {
//     console.log(false);
// }

//exercicio8
// const num1 = 10;

// const num2 = 12;

// const num3 = 34;

// if ( num1 %2 !== 0 || num2 % 2 !== 0 || num3 % 2 !== 0) {
//     console.log('true');
// }
// else {
//     console.log(false);
// }

//exercicio9
// const cost = 1;

// const sell = 2;

// let totalCost = cost * 1.2;

// if( cost > 0 && sell > 0 ){
//     const total = ( sell - totalCost )* 1000;
//     console.log(total);
// }
// else {
//     console.log('Valor não pode ser igual a zero')
// }

//exercicio10 IMPOSTO DE RENDA
// ESTOU FALHANDO NA MATEMÁTICA MENTAL
let aliquotINSS;
let aliquotIR;

let grossWage = 3000; 
//calcula salario - INSS
if (grossWage <= 1556.94){
    aliquotINSS = grossWage * 0.08; 
} else if (grossWage <= 2594.92){
    aliquotINSS = grossWage * 0.09;
} else if (grossWage <= 5189.82) {
    aliquotINSS = grossWage * 0.11;
} else {
    aliquotINSS = 570.88 ;
};

let baseSalary = grossWage - aliquotINSS;
//calcula (salario com desconto INSS) - IR
if (baseSalary <= 1903.98){
    aliquotIR = 0;
}else if (baseSalary <= 2826.65) {
    aliquotIR = (baseSalary * 0.075) - 142.80;
}else if (baseSalary <= 3751.05) {
    aliquotIR = (baseSalary * 0.15) - 354.80;
}else if (baseSalary <= 4664.68) {
    aliquotINSS = (baseSalary * 0.225) - 636.13;
}else {
    aliquotIR = (baseSalary * 0.275) - 869.36;
};
//calculo salario final
console.log('Salário Líquido: R$' + (baseSalary - aliquotIR));