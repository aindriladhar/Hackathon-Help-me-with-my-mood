const electron = require('electron')

const remote = electron.remote

document.getElementById("close-button").addEventListener("click",function(e) {
	const window = remote.getCurrentWindow()
	window.close()
})


//MINIMIZE WINDOW
document.getElementById("min-button").addEventListener("click",function(e) {
	const window = remote.getCurrentWindow()
	window.minimize()
})

//HOME BUTTOM
document.getElementById("home").addEventListener("click",function(e) {
	//document.getElementById("body2").style.display = "none";
	$("#body2").fadeOut();
	$("#body3").fadeOut();
	$("#body4").fadeOut();
	$("#home").addClass("actve");
	$("#body1").delay(500).fadeIn();
});

$('select').formSelect(); //MATERIALIZE SELECT
$('.chips').chips();//MATERIALIZE CHIPS
  $('.chips-autocomplete').chips({
    autocompleteOptions: {
      data: {
        'Pop': null,
        'Rock': null,
        'Alternative': null,
        'Jazz': null,
        'Hip Hop': null,
        'Rap': null,
        'Metal': null,
        'Indie': null,
        'Regional': null,
        'Folk': null,
        'Bollywood': null,
        'Country': null,
        'EDM': null,
        'Dubstep': null
      },
      limit: Infinity,
      minLength: 1
    }
  });

//NAV REQUESTS
document.getElementById("quick-start").addEventListener("click",function(e) {
	$("#body1").fadeOut();
	$("#body2").delay(500).fadeIn();
	$("#home").removeClass("actve");
});

document.getElementById("reg").addEventListener("click",function(e) {
	$("#body1").fadeOut();
	$(".body3").css("display","flex").hide().delay(500).fadeIn();
	$("#home").removeClass("actve");
	$("#uname-contain").show();
	$("#name-contain").hide();
	$("#lang-contain").hide();
	$("#genre-contain").hide();
	$("#read-contain").hide();
	$("#animal-contain").hide();
});

document.getElementById("continue").addEventListener("click",function(e) {
	$("#body1").fadeOut();
	$(".body4").css("display","flex").hide().delay(500).fadeIn();
	$("#home").removeClass("actve");
});

/*REG FORM PREV NEXT*/
$("#next0").click(function() {
	if(!$('#uname').val()){
		alert("We must know your username. Promise we won't misuse it. Read terms of use for more info.");
	}
	else{
		$("#uname-contain").hide();
		$("#name-contain").show();
		$(".determinate").css("width","17%");
	}	
});

$("#prev0").click(function() {
	$("#uname-contain").show();
	$("#name-contain").hide();
	$(".determinate").css("width","0%");
});

document.getElementById("next1").addEventListener("click",function(e) {
	if(!$('#name').val()){
		alert("We won't remember you if you don't share your name.");
	}
	else{
		$("#name-contain").hide();
		$("#lang-contain").show();
		$(".determinate").css("width","34%");
	}	
});

$("#prev1").click(function() {
	$("#name-contain").show();
	$("#lang-contain").hide();
	$(".determinate").css("width","17%");
});

$("#next2").click(function() {

	if($('select[name=garden] >option:selected').length < 1){
		alert("You must select atleast one language.");
	}
	else{
		$("#genre-contain").show();
		$("#lang-contain").hide();
		$(".determinate").css("width","51%");
	}	
});

$("#prev2").click(function() {
	$("#genre-contain").hide();
	$("#lang-contain").show();
	$(".determinate").css("width","34%");
});

$("#next3").click(function() {
	var chipInstance = M.Chips.getInstance($(".chips"));
	var data = chipInstance.chipsData;
	if(data.length<1){
		alert("Atleast one genre, please.");
	}
	else{
		$("#read-contain").show();
		$("#genre-contain").hide();
		$(".determinate").css("width","68%");
	}	
});

$("#prev3").click(function() {
	$("#genre-contain").show();
	$("#read-contain").hide();
	$(".determinate").css("width","51%");
});

$("#next4").click(function() {
	var read = $('#read').val();
	if(!read){
		alert("You can do better than that. Come on now!.");
	}
	else if(read != "YES" && read != "NO"){
		alert("'YES' or 'NO' please");
	}
	else{
		$("#animal-contain").show();
		$("#read-contain").hide();
		$(".determinate").css("width","85%");
	}
});

$("#next5").click(function() {
	if(!$('.animals').is(':checked')){
		alert('Cats are cute, check them!');
	}
	else{
		$(".determinate").css("width","100%");
		$(".body3").fadeOut();
		$("#loading").fadeIn();
	}	
});

$("#prev4").click(function() {
	$("#animal-contain").hide();
	$("#read-contain").show();
	$(".determinate").css("width","68%");
});

/*ANIMAL CHECKBOX ADJUST*/
$('#all').on('change', function() {
	if($('#all').is(':checked')){
		$('.animals').not(this).prop('checked', false);
		$('.animals').not(this).prop('disabled', true);
	}
	else{
		$('.animals').not(this).prop('disabled', false);
	}    
});

function get_odd(){
  var pyshell = require('python-shell')
console.log(pyshell)
pyshell.runString('x=1;print(x)', null, function (err, results) {
  // script finished
});
}