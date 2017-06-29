
function mostNumbers () {
  var a = []
  if (arguments.length === 0) {
    return 0
  } else {
    for (var i = 0; i < arguments.length; i++) {
      a.push(arguments[i])
    }
    return (Math.max.apply(null, a) - Math.min.apply(null, a))
  }
}
// console.log(mostNumbers(1, 2, 3, 4, 5, 6))
// console.log(mostNumbers(1, 2.5, 3, 0.4, 5, 6.9))
console.log(mostNumbers())
