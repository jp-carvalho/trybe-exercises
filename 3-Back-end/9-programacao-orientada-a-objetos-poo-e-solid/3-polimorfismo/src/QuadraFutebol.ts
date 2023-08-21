import Quadra from './Quadra';
import normas from './normas/normasDeUso';
import { IFutebol } from './interfaces/IFutebol';
import { IAgenda } from './interfaces/IAgenda';

class QuadraFutebol extends Quadra {
// busca os dados da quadra referenciada
  public futebolData: IFutebol = normas.futebol;

  public reservar<IFutebol>(horaReserva: Date): IAgenda<IFutebol> {
    // gerando protocolo de agendamento genérico
    const protocolo = (Math.random() + 1).toString(30).substring(3);

    return {
      protocolo,
      data: horaReserva,
      regras: this.futebolData as unknown as IFutebol,
    }
  }
}

export default QuadraFutebol;