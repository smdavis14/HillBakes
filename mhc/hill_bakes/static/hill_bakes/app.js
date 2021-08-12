const cookieDropDown = document.getElementsByClassName('cookie')
const cakeDropDown = document.getElementsByClassName('cake')
const cakeBallDropDown = document.getElementsByClassName('cake_ball')

for (let cookie of cookieDropDown){
  cookie.addEventListener('click', () => {
  console.log("I'm a cookie, buy me!")
})
}

for (let cake of cakeDropDown){
  cake.addEventListener('click', () => {
    console.log("Let them eat cake, and lots of it")
  })
}

for (let cakeBall of cakeBallDropDown){
  cakeBall.addEventListener('click', () => {
    console.log("Let them eat cake, in the shape of a ball.  Like a donut hole.")
  })
}