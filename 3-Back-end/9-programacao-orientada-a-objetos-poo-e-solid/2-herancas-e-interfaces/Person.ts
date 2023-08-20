export default class Person {
  // não entendi o uso no course se volta como retorno no log.
  // protected MINIMUM_NAME_LENGTH = 3;

  // protected MAXIMUM_AGE = 120;

  constructor(
    private _name: string,
    private _birthDate: Date,
  ) {
    this.validatePerson(); // validação do objeto criado com o construtor da classe
  }

  get name(): string {
    return this._name;
  }

  set name(value: string) {
    this.validateName(value);
    this._name = value;
  }

  get birthDate(): Date {
    return this._birthDate;
  }

  set birthDate(value: Date) {
    this.validateBirthDate(value);
    this._birthDate = value;
  }

  static getAge(date: Date): number {
    const diff = Math.abs(new Date().getTime() - date.getTime()); // diferença em milissegundos entre a data atual e a data passada por parâmetro
    const yearMs = 31_536_000_000; // 1 ano = 31536000000 milissegundos
    return Math.floor(diff / yearMs);
  }

  private validateName(name: string): void {
    if (name.length < 3) {
      throw new Error(`O nome deve conter no mínimo 3 caracteres.`);
    }
  }

  private validateBirthDate(date: Date): void {
    if (date.getTime() > new Date().getTime()) {
      throw new Error('A data de nascimento não pode ser uma data no futuro.');
    }
    if (Person.getAge(date) > 120) {
      throw new Error(`A pessoa deve ter no máximo 120 anos.`);
    }
  }

  private validatePerson(): void {
    this.validateName(this.name);
    this.validateBirthDate(this.birthDate);
  }
}
