// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on("line", function (line) {
  input.push(line.split(" "));
}).on("close", function () {
  let w = 0;
  let h = 0;

  let count = [
    ['1', '0', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0'],
    ['0', '0', '0', '0']
  ];

  let result = "";

  function go() {
    if (input[w][h + 1] == 1) { // 오른쪽
      count[w][h + 1] = "1";
      h++;
      if (w == 3 && h == 3) {
        return sortF();
      }
      go();
    } else if (input[w + 1][h] == 1) { // 아래
      count[w + 1][h] = "1";
      w++;
      if (w == 3 && h == 3) {
        return sortF();
      }
      go();
    }
  }
  go();

  function sortF() {
    for (let i = 0; i < 4; i++) {
      for (let j = 0; j < 4; j++) {
        if (j == 0) {
          result = result + "ㅁ" + count[i][j];
        } else {
          result = result + "ㅁㅁ" + count[i][j];
        }
      }
      result = result + "ㅁ\n";
    }
    return console.log(result);
  }

  process.exit();
});