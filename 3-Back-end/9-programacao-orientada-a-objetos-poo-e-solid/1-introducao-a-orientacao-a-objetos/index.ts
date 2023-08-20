import Client from './Client';
import Order from './Order';
import OrderItem from './OrderItem';

const client = new Client('JP');

const sandwitch = new OrderItem('Sanduíche Natural', 5.00);
const juice = new OrderItem('Suco de abacaxi', 5.00);
const dessert = new OrderItem('Gelatina de Uva', 2.50);

const order = new Order(client, [sandwitch, juice, dessert], 'dinheiro', 0.10)

console.log(order);
console.log('Valor normal: ', order.calculateTotal());
console.log('Valor com desconto: ', order.calculateTotalWithDiscount());



