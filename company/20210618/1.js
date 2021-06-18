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
  const queue = [{ point: 1, temp: 1 }] // 현위치, 전에 이동수
  const emi = [false, true] // 무조건 1번째는 방문해봄
  let count = 1
  while(1) {
    console.log(queue)
    count++
    let size = queue.length
    for (let i = 0; i < size; i++) {
      const { point, temp } = queue[0]
      queue.shift()
      if (point == target) {
        console.log(count)
        process.exit()
      }
      // +1
      const addTemp = temp + 1
      const addNextPoint = point + addTemp
      if (!(addNextPoint > target) && !emi[addNextPoint]) { // 이전 이동에 +1 해서 이동했을 때 위치가 target보다 크거나 같으면 하지 말기
        queue.push({
          point: addNextPoint,
          temp: addTemp
        })
        emi[addNextPoint] = true
      }
      // -1
      const minusTemp = temp - 1
      const addMinusPoint = point + minusTemp
      if (!(addMinusPoint > target) && addMinusPoint > 0 && !emi[addMinusPoint]) {
        queue.push({
          point: addMinusPoint,
          temp: minusTemp
        })
        emi[addMinusPoint] = true
      }
      // 0
      if (!(point > target) && point > 0 && !emi[point]) {
        queue.push({
          point: point + temp,
          temp: temp,
        })
        emi[point] = true
      }
    }
  }
});
