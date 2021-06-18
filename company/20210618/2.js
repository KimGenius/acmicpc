const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const input = [];
rl.on("line", function(line) {
	input.push(line.trim())
	rl.close()
}).on("close", function() {
	const target = input[0]
  const addTarget = Math.sqrt(target)
  let count = 1 + addTarget
  let current = 1
  for (let i = 1; i < addTarget; i++) {
    current += i
  }
  for (let i = addTarget - 1; i > addTarget; i--) {
    current += i
  }
  console.log(current)
})
