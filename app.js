/** 
 * You are going to write several functions
 * The goal here is to practice your skills 
 * without using the built in methods such as
 * .split, .replace, Math.
*/

//Write a function called cubed(x) that accepts an argument x and returns its cubed value
function cubed(x){

}

//write a function called power that accepts two args (base, exp) and returns the power  
function power(base, exp){

}

/*
* write a function called modByX that will accept two args (an array of numbers and x the mod number) the function should return an array where each number was modified to be the result of the number % x 
*/

function modByX(arr, x){

}



/**
  Fill in the necessary parts of the findById function below
  findById(1000) Bad Id's should return the following object {error: 'Sorry that user id could not be found'} 
  The array will look something like this
  
  var users = [{id: 1, name: 'Jon'},{id: 2, name: 'Yuli'},{id: 21, name: 'Peter'},{id: 17, name: 'St. MaryLou de la playa carmen'},{id: 51, name: 'Doug'},{id: 881, name: 'Paul'},{id: 0, name: 'Jon'},{id: 999, name: 'Timma'}]
*/

function findById(array, id){
}

//write a fn called letterCount that accepts two arguments a (sentence, letter) have the function return the number of times that letter repeats in the sentence

function letterCount(sen, letter){
 
}


//Modify the letterCount Function above to accept an optional third argument allowing for case sensitivity Default should value is true letterCount(sentence, letter, isCaseSensitive)
function letterCount(sen, letter, isCaseSensitive){
  
}


//write a fn called pythagorean(a,b) 
//The forumula for pythagorean is  a^2 + b^2 = c^2
//this function should return the value of c^2
function pythagorean(a,b) {
  
}


/**
    Best Practice: Constructor functions are the only variables that start with an uppercase letter
    The keyword this refers to a single instance
    When calling or invoking a constructor function you must use the *** new *** keyword
*/


//Write a function called sumAll that accepts an array of numbers and returns the sum of all items in the array

function sumAll(arr){
  
}



//write an isEqual function that accepts two arguments and returns a boolean (3,'3') returns false ('abc', 'abc') returns true

function isEqual(a, b){

}


//write a function called inStock that accepts an array of objects and a productId or productName and returns the product if it is in stock based on its quantity

function inStock(arr, lookup){
  
}



var products =[{
    id: 123,
    name: 'Squaty Potty', 
    quantity: 5,
    price: 19.99
},{
    id: 124,
    name: 'Design Your Own Cage', 
    quantity: 0, 
    price: 1.99
},{
    id: 125,
    name: 'Worlds Best Chap Stick', 
    quantity: 280,
    price: 0.99
}]













//do not modify
test.cubed = cubed
test.power = power
test.modByx = modByX
test.findById = findById
test.letterCount=letterCount
test.pythagorean = pythagorean
test.sumAll = sumAll
test.isEqual = isEqual
test.inStock =  inStock