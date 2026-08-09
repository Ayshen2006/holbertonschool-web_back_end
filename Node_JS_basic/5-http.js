const http = require('http');
const fs = require('fs');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');

    fs.readFile(process.argv[2], 'utf8', (error, data) => {
      if (error) {
        res.end('Cannot load the database');
        return;
      }

      const lines = data.split('\n').filter((line) => line.trim() !== '');
      const students = lines.slice(1);

      res.write(`Number of students: ${students.length}\n`);

      const fields = {};

      students.forEach((student) => {
        const values = student.split(',');
        const firstname = values[0];
        const field = values[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      });

      Object.keys(fields).forEach((field) => {
        res.write(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`,
        );
      });

      res.end();
    });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);

module.exports = app;
