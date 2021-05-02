
$(".btn").click(function(){
  currentBtn = $(this).val();
  window.location.href='/eachofus?name='+currentBtn;
});
