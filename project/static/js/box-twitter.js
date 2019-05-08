window.addEventListener("load",function(){
	var width=screen.width;
	var leftIcon=document.querySelector(".logo-icon")
	var tweetNavUl=document.querySelector("#tweet-ul-1");
	var midIcon=document.querySelector(".mid-icon");
	var tweetNavForm=document.querySelector("#tweet-form");

	if(width<992){
		leftIcon.style.display="inline";
		tweetNavUl.style.display="none";
		midIcon.style.display="none";
		tweetNavForm.style.display="none";
	}else{
		leftIcon.style.display="none";
		tweetNavUl.style.display="inline";
		midIcon.style.display="inline";
		tweetNavForm.style.display="inline";
	}

	window.addEventListener("resize",function(e){

		var width=screen.width;
		var leftIcon=document.querySelector(".logo-icon")
		var tweetNavUl=document.querySelector("#tweet-ul-1");
		var midIcon=document.querySelector(".mid-icon");
		var tweetNavForm=document.querySelector("#tweet-form");

		if(width<992){
			leftIcon.style.display="inline";
			tweetNavUl.style.display="none";
			midIcon.style.display="none";
			tweetNavForm.style.display="none";
		}else{
			leftIcon.style.display="none";
			tweetNavUl.style.display="inline";
			midIcon.style.display="inline";
			tweetNavForm.style.display="inline";
		}
	})
})