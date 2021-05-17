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
	const inp = input[0].split(' ')
	let goorm = parseInt(inp[0])
	const bro = parseInt(inp[1])
	let result = 0
	if (goorm > bro) {
		while(goorm !== bro) {
			goorm--
			result++
		}
		console.log(result)
		process.exit()
	} else {
		const queue = [goorm]
		const point = []
		while(1) {
			const loop = queue.length
			for(let i = 0; i < loop; i++) {
				const q0 = queue[0]
				queue.shift()
				if (q0 === bro) {
					console.log(result)
					process.exit()
				}
				if (q0 + 1 <= 100000 && !point[q0 + 1]) queue.push(q0 + 1)
				point[q0 + 1] = true
				if (q0 - 1 >= 0 && !point[q0 - 1]) queue.push(q0 - 1)
				point[q0 - 1] = true
				if (q0 * 2 <= 100000 && !point[q0 * 2]) queue.push(q0 * 2)
				point[q0 * 2] = true
			}
			result++
		}
	}
});
