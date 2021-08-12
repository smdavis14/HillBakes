const cookieDropDown = document.getElementsByClassName('cookie')
const cakeDropDown = document.getElementById('cake')
const cakeBallDropDown = document.getElementById('cake_ball')

for (let cookie of cookieDropDown){
  cookie.addEventListener('click', () => {
  console.log("I'm a cookie, buy me!")
})
}