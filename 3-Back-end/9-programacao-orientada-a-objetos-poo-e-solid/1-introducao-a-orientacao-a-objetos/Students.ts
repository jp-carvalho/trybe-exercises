class Student {
  private _enrollment: string;

  private _name: string;

  private _examsGrades: number[];

  private _assignmentsGrades: number[];


  constructor(enrollment: string, name: string) {
    this._enrollment = enrollment;
    this._name = name;
    this._examsGrades = [];
    this._assignmentsGrades = [];
  }
  
  public get enrollment(): string {
    return this._enrollment;
  }
  public set enrollment(value: string) {
    this._enrollment = value;
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

  public get examsGrades(): number[] {
    return this._examsGrades;
  }
  public set examsGrades(value: number[]) {
    if (value.length !== 4) {
      throw new Error("A pessoa estudante só pode possuir 4 notas de provas");
    }
    this._examsGrades = value;
  }

  public get assignmentsGrades(): number[] {
    return this._assignmentsGrades;
  }
  public set assignmentsGrades(value: number[]) {
    if (value.length !== 2) {
      throw new Error("A pessoa estudante só pode possuir 2 notas de trabalhos");
      
    }
    this._assignmentsGrades = value;
  }

  sumGrades(): number {
    return [...this.examsGrades, ...this.assignmentsGrades]
    .reduce((previousNote, note) => {
        const nextNote = note + previousNote;

        return nextNote;
      }, 0)
  }

  sumAvarageGrade(): number {
    const sumGrades = this.sumGrades();
    const divider = this.examsGrades.length + this.assignmentsGrades.length;

    return Math.round(sumGrades / divider)
  }
  
}

const personOne = new Student('101202303', 'Maria da Silva');
personOne.examsGrades = [25, 20, 23, 23];
personOne.assignmentsGrades = [45, 45];

console.log(personOne);
console.log('Soma de todas as notas de exames: ', personOne.sumGrades());
console.log('Média das notas de exames: ', personOne.sumAvarageGrade());

