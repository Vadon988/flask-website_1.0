window.addEventListener("load",function(){

	function newSlider(){
		var nSlides=document.querySelectorAll('.col-news');
		var prevNews=document.querySelector('#prev-news');
		var nextNews=document.querySelector('#next-news');
		var curr_news=0;

		function restNews(){
			for(var x=0;x<nSlides.length;x++){
				nSlides[x].style.display="none";
			}
		}

		prevNews.addEventListener("click",function(e){
			restNews();
			if(curr_news===nSlides.length-1){
				curr_news=-1;
			}
			curr_news++;
			nSlides[curr_news].style.display="flex";
		})

		nextNews.addEventListener("click",function(e){
			restNews();
			if(curr_news===0){
				curr_news=nSlides.length;
			}
			curr_news--;
			nSlides[curr_news].style.display="flex";
		})
		
	}

	newSlider();

	//X-RATE COLORE
	var xRate=document.querySelectorAll(".x-change");
	var arrow=document.querySelectorAll(".arrow");
	
	for(var x=0;x<xRate.length;x++){
		if(xRate[x].innerHTML[0]==='-'){
			xRate[x].style.color="red";
			arrow[x].innerHTML="&#9660;";
			arrow[x].style.color="red";
		}else{
			xRate[x].style.color="green";
			arrow[x].innerHTML="&#9650;";
			arrow[x].style.color="green";
		}
	}
})