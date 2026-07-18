const student = {
  name: "John Doe",
  grades: [
    { name: "math", grade: 80 },
    { name: "science", grade: 100 },
    { name: "history", grade: 60 },
    { name: "PE", grade: 90 },
    { name: "music", grade: 98 }
  ]
};


let total = 0;
for (let i = 0; i < student.grades.length; i++) {
  total += student.grades[i].grade;
}
let gradeAvg = total / student.grades.length;


let highest = student.grades[0];
let lowest = student.grades[0];

for (let i = 1; i < student.grades.length; i++) {
  if (student.grades[i].grade > highest.grade) {
    highest = student.grades[i];
  }
  if (student.grades[i].grade < lowest.grade) {
    lowest = student.grades[i];
  }
}


const result = {
  name: student.name,
  gradeAvg: gradeAvg,
  highestGrade: highest.name,
  lowestGrade: lowest.name
};

console.log(result);
