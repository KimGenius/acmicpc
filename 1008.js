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
    const [a, b] = input[0].split(' ')
    console.log(a / b)
})
