import Clube from './Clube';
import QuadraFutebol from './QuadraFutebol';

const trybeClube = new Clube();
const quadraFutebol = new QuadraFutebol();
trybeClube.adicionarQuadra(quadraFutebol);

//data que queremos reservar, aqui vc pode colocar qualquer data obedecendo ano-mes-dia
const dataReserva = new Date('2023-05-17');

const reservarQuadraFutebol = trybeClube
  .buscarQuadra<QuadraFutebol>(0)//buscando a quadra de futebol na posição 0, já q ela foi adicionada primeiro no array de quadras do clube
  .reservar(dataReserva); //o método de reservar é da classe QuadraFutebol, e passamos a data que queremos reservar
console.log(reservarQuadraFutebol);