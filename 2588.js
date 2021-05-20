const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const rl2 = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const input = [];
rl.on("line", function(line) {
	input.push(line.trim())
	rl.close()
}).on("close", function() {	
	rl2.on("line", function(line) {
		input.push(line.trim())
		rl2.close()
	}).on("close", function() {
		console.log(input[0])
		const [a, b] = input[0].split('\n')
		console.log(a, b)
	})
})
