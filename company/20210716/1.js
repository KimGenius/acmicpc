// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	const startList = ['(', '{', '[']
	const endList = [')', '}', ']']
	const list = []
	for (let i = 0; i < line.length; i++) {
		const a = line.charAt(i)
		if (startList.includes(a)) {
			list.push(a)
		} else if (endList.includes(a)) {
      var last = list[list.length - 1]
      var startIndex = startList.indexOf(last)
      var lastIndex = endList.indexOf(a)
      if (startIndex === lastIndex) {
				list.pop()
			} else {
				console.log(false)
        rl.close()
			}
		}
	}
	if (list.length) {
    console.log(false)
    rl.close()
  }
	console.log(true)
	rl.close()
}).on("close", function() {
	process.exit();
});
