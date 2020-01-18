/* Mkhanyisi Javascript Code
   Itlize Global Training
   01/13/2020
*/
function show_date() {

    var date = new Date();
    var year = date.getFullYear();
    var d = date.getDay();
    var daym= date.getDate();
    var minute = date.getMinutes();  
    var hour = date.getHours();
    var seconds = date.getSeconds();
    var td;
    var today ="Today is : ";
    var month = date.getMonth()+1;
    
    

    if(hour<12){
        td= " AM: ";
    }
    else{
    	hour = hour%12;
      td= " PM: ";
    }
    var day;
    switch(d){
    	case 0:
        	day="Sunday";
            break;
        case 1:
        	day="Monday";
            break;
        case 2:
        	day="Tuesday";
            break;
        case 3:
        	day="Wednesday";
            break;
        case 4:
        	day="Thursday";
            break;
        case 5:
        	day="Friday";
            break;
        case 6:
        	day="Saturday";
            break;
        
    }

    // final string 
    var str = today.concat(day,"\n","Current time is : ",hour,td,minute," : ",seconds,"\n",month,"-",daym,"-",year);
    //str.concat(today,day,"\n","Current time is :",hour,td,minute," : ",seconds);

    console.log(str);
  
    alert(str); 
  
}

function multiply() {
        var myBox1 = document.getElementById('num1').value; 
        var myBox2 = document.getElementById('num2').value;
        var result = document.getElementById('result'); 
        var myResult = myBox1 * myBox2;
        //alert("Multiplication Result is"+myResult); 
        document.getElementById('result').innerHTML  = myResult;
}

function divide() {
        var myBox1 = document.getElementById('num1').value; 
        var myBox2 = document.getElementById('num2').value;
        var result = document.getElementById('result'); 
        var myResult = myBox1 / myBox2;
        //alert("Division Result is"+myResult); 
        document.getElementById('result').innerHTML = myResult;

}

function docURL(){
	document.getElementById('docURL').innerHTML = document.URL;
	//console.log(document.URL);
}

function reverseNum(){
	var num = document.getElementById('revnum').value;
    
    var reversed = num.split("").reverse().join("") ;
    document.getElementById('revnum').innerHTML = reversed;
    //console.log(reversed);
    alert(reversed);
    
}

function Second_Greatest_Lowest(arr_num)
{
  arr_num.sort(function(x,y)
           {
           return x-y;
           });
  var uniqa = [arr_num[0]];
  var result = [];
  
  for(var j=1; j < arr_num.length; j++)
  {
    if(arr_num[j-1] !== arr_num[j])
    {
      uniqa.push(arr_num[j]);
    }
  }
    result.push(uniqa[1],uniqa[uniqa.length-2]);
  return result.join(',');
  }
  
function largest(arr){
	alert(Math.max(arr));
}

// top-down implementation
function merge(left, right) {
  let arr = [];

  while (left.length && right.length) {
    if (left[0] < right[0]) {
      arr.push(left.shift());
    } else {
      arr.push(right.shift());
    }
  }
  return arr.concat(left.slice().concat(right.slice()));
}

function mergeSort(arr) {
  if (arr.length < 2) {
    return arr;
  }

  const middle = Math.floor(arr.length / 2);
  const left = arr.slice(0, middle);
  const right = arr.slice(middle);

  return merge(mergeSort(left), mergeSort(right));
}


function checkNan(val){
        return val !== val;
}

function is_sameType(value1, value2) {
        if(checkNan(value1) || checkNan(value2)) {
         return checkNan(value1) === checkNan(value2);
        }
        return toString.call(value1) === toString.call(value2);
}
