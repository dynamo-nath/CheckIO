
function commonWords (first, second) {
  var a = first.split(',')
  var b = second.split(',')
  var c = []
  for (var i = 0; i < a.length; i++) {
    for (var j = 0; j < b.length; j++) {
      if (a[i] === b[j] && c.indexOf(a[i]) !== null) {
        c.push(a[i])
      }
    }
  }
  return c.sort().toString()
}

// console.log(commonWords('hello, world', 'hello, moon'))
console.log(commonWords('one,two,three', 'two,four,five,one,three'))

// var a = ['hello', 'world']
// if (a.indexOf('hello') !== null) {
//   console.log('hello')
// } else {
//   console.log('bye')
// }
