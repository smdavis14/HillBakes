
let toOrder = []

const cookieDropDown = document.getElementsByClassName('cookie')
const cakeDropDown = document.getElementsByClassName('cake')
const cakeBallDropDown = document.getElementsByClassName('cake_ball')

for (let cookie of cookieDropDown){
  cookie.addEventListener('click', () => {
    placeOrder()
})
}

const cookieList = ['Cookies - Single $5', 'Cookies - 3 $13', 'Cookies - 6 $27']
const placeOrder = () => {document.createElement('select')
  placeOrder.name = 'cookie'
  placeOrder.id = 'cookie'
  for (let choice of cookieList){
    console.log(choice)
    let option = document.createElement('option')
    console.log(option)
    option.value = choice
  }
  console.log('my select dropdown')}




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