window.addEventListener("load",function(){

	var imdbSlides=document.querySelectorAll(".imdb-slide");
	var prevImdb=document.querySelector("#prev-imdb");
	var nextImdb=document.querySelector("#next-imdb");
	var curr_imdb=0;

	function imdbSlider(){

		function restImdb(){
			for(var x=0;x<imdbSlides.length;x++){
				imdbSlides[x].style.display="none";
			}
		}

		prevImdb.addEventListener("click",function(){
			restImdb();
			if(curr_imdb===imdbSlides.length-1){
				curr_imdb=-1;
			}
			curr_imdb++;
			imdbSlides[curr_imdb].style.display="inline";
		})

		nextImdb.addEventListener("click",function(){
			restImdb();
			if(curr_imdb===0){
				curr_imdb=imdbSlides.length;
			}
			curr_imdb--;
			imdbSlides[curr_imdb].style.display="inline";
		})
	}
	
	imdbSlider();

	$(".yt-mod").click(function(e){

		var target=e.target;
		target.setAttribute("data-toggle","modal");
		target.setAttribute("data-target","#ytModal");
		var sibil=e.target.previousSibling;
		var yt_id=target.previousElementSibling.innerHTML;
		var bgIframe=document.querySelector("#bg-iframe");
		bgIframe.setAttribute("src","https://www.youtube.com/embed/"+yt_id);
	})

	
})