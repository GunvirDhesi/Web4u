document.addEventListener("mousemove", paralax);
function paralax(e)
{
  this.querySelectorAll('.imageLayer').forEach(function(move){
    var speed = move.getAttribute('data-speed')
    var x = (e.clientX * speed)/100
    var y = (e.clientY * speed)/100

    move.style.transform = 'translateX(' + x + 'px) translateY(' + y + 'px)'
  })
}
