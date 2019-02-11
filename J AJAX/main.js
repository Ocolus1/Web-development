function showTime(){
  //The date function and variable assignment
  var time = new Date();
   
  var d = time.getDay();
  var h = time.getHours();
  var m = time.getMinutes();
  var s = time.getSeconds();
  var session = "AM";
  var month = time.getMonth();
  var date = time.getUTCDate();

  if(h == 0){
    h = 12;
  }
  if(h > 12){
    h = h - 12;
    session = "PM";
  }
 h = (h < 10)? "0" + h :h ;
 m = (m < 10)? "0" + m : m;
 s = (s < 10)? "0" + s : s;
 document.getElementById('snd-container').innerHTML= h + ':' + m + ':' + s + ' '+ session;
 
 //days of the week code
 var mon = document.getElementById('mon');
 var tue = document.getElementById('tue');
 var wed = document.getElementById('wed');
 var thu = document.getElementById('thu');
 var fri = document.getElementById('fri');
 var sat = document.getElementById('sat');
 var sun = document.getElementById('sun');
 d = (d == 1)? mon.style.backgroundColor = 'blue': d;
 d = (d == 2)? tue.style.backgroundColor = 'blue': d;
 d = (d == 3)? wed.style.backgroundColor = 'blue': d;
 d = (d == 4)? thu.style.backgroundColor = 'blue': d;
 d = (d == 5)? fri.style.backgroundColor = 'blue': d;
 d = (d == 6)? sat.style.backgroundColor = 'blue': d;
 d = (d == 0)? sun.style.backgroundColor = 'blue': d;

// the month and date code
var demo = document.getElementById('demo');
demo.innerHTML = month + 1 + '/' + ' ' + date;
demo.style.fontSize = '60px';
demo.style.marginTop = '0px';

//the code for the alarm
var first = document.getElementById('first').value;
var second = document.getElementById('second').value;
var third = document.getElementById('third').value;
var audio = document.getElementById('audio');
if(first== h && second == m && third == session){
   audio.play();
}

//The timeout function
setTimeout(showTime, 1000);

}
showTime();


