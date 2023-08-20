export default class OrderItem {
  private _name: string;
  private _price: number;

  constructor(name: string, price: number) {
    this._name = name;
    this._price = price;
  }
  
  public get name(): string {
    return this._name;
  }
  public set name(value: string) {
    if (value.length < 3) {
      throw new Error("O nome deve conter no mínimo 3 caracteres");
    }
    this._name = value;
  }

  public get price(): number {
    return this._price;
  }
  public set price(value: number) {
    if (value < 0) {
      throw new Error("O preço deve ser positivo");
    }
    this._price = value;
  }
}