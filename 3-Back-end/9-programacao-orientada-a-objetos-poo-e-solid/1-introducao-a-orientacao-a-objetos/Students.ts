
class Student {
  private _enrollment: string;
  private _name: string;
  private _examsGrades: number[] = Array();
  private _worksGrades: number[] = Array();

  constructor(enrollment: string, name: string, exams: number[], works: number[]) {
    this._enrollment = enrollment;
    this._name = name;
    // para verificar o tamanho do array, esse examsGrades tem que referenciar o do SET que fica abaixo e não o criado acima no Student, e ele deve ter como default um Array()  vazio
    this.examsGrades = exams;
    this.worksGrades = works;
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
    this._name = value;
  }

  public get examsGrades(): number[] {
    return this._examsGrades;
  }
  public set examsGrades(value: number[]) {
    if (value.length !== 4) {
      throw new Error("A pessoa precisa de 4 notas de prova");
    }
    this._examsGrades = value;
  }

  public get worksGrades(): number[] {
    return this._worksGrades;
  }
  public set worksGrades(value: number[]) {
    if (value.length !== 2) {
      throw new Error("A pessoa precisa de 2 notas de trabalho");
    }
    this._worksGrades = value;
  }

  sumGrades(): number {
    return [...this.examsGrades, ...this.worksGrades]
    .reduce((prevGrade, grade) => {
      grade += prevGrade;
      return grade;
    }, 0)
  }

  sumAverageGrades(): number {
    const sumGrades = this.sumGrades();
    const divider = this.examsGrades.length + this.worksGrades.length;
    return Math.round(sumGrades / divider);
  }

}

const student1 = new Student('202001011', 'Maria', [8, 7, 9, 10], [6, 5]);
console.log(student1);
console.log('Soma das notas: ', student1.sumGrades());
console.log('Média das notas: ', student1.sumAverageGrades());



const student2 = new Student('202001012', 'João', [5, 7, 9, 10], [9, 8]);
console.log(student2);
console.log('Soma das notas: ', student2.sumGrades());
console.log('Média das notas: ', student2.sumAverageGrades());



