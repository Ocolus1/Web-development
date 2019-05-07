window.addEventListener( 'DOMContentLoaded', function () {

    const buttonRoolDice = document.querySelector( '.dice-roll' );

function rollDice () {

    const diceSide1 = document.getElementById( 'dice-side-1' );
    const diceSide2 = document.getElementById( 'dice-side-2' );
    const status = document.getElementById( 'status' );

    const side1 = Math.floor( Math.random() * 99 ) + 1;
    // const side2 = Math.floor( Math.random() * 99 ) + 1;
    const diceTotal = side1 ;

    diceSide1.innerHTML = side1;
    // diceSide2.innerHTML = side2;
    var count=0;
    var ms = 200;
    var step = 100;
    var counter=setTimeout(timer, ms);

    function timer(){
    count=count+1;
    if (count <= side1)
    {
        //Do code for showing the number of seconds here
        diceSide1.innerHTML = count;
        // document.getElementById("countdown").innerHTML=count ; // watch for spelling
        ms = ms - step;
        counter = setTimeout(timer, ms);

    }

    }


    status.innerHTML = 'You rolled ' + diceTotal + '.';

    // if ( side1 === side2 ) {
    //     status.innerHTML += ' Doubles! You get a free turn!';
    // }
}

buttonRoolDice.addEventListener( 'click', rollDice, false );

}, false);


// var count=0;
// var ms = 200;
// var step = 30;
// var counter=setTimeout(timer, ms); //1000 will  run it every 1 second

// function timer()
// {
//   count=count+1;
//   if (count <= 30)
//   {
//     //Do code for showing the number of seconds here
//      document.getElementById("countdown").innerHTML=count ; // watch for spelling
//      ms = ms - step;
//      counter = setTimeout(timer, ms);

//   }

// }