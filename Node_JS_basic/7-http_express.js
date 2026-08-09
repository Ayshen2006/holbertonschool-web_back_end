const express = require('express');
const fs = require('fs');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const database = process.argv[2];

  fs.readFile(database, 'utf8', (err, data) => {
    if (err) {
      res.send('This is the list of our students\nCannot load the database');
      return;
    }

    const lines = data.split('\n').filter((line) => line.trim() !== '');
    const students = lines.slice(1);

    let result = 'This is the list of our students\n';
    result += `Number of students: ${students.length}\n`;

    const fields = {};

    for (const student of students) {
      const values = student.split(',');
      const firstname = values[0];
      const field = values[3];

      if (!fields[field]) {
        fields[field] = [];
      }

      fields[field].push(firstname);
    }

    for (const field of Object.keys(fields)) {
      result += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
    }

    res.send(result);
  });
});

app.listen(1245);

module.exports = app;
