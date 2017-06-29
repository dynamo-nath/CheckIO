
function absoluteSorting (numbers) {
  return numbers.sort(function (c, d) {
    return (Math.abs(c) - Math.abs(d))
  })
}

console.log(absoluteSorting([-5, 1, -10, 20]))
