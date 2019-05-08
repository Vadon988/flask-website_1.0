window.addEventListener("load",function(){

	var width=screen.width;
	var boxHiddenNav=document.querySelectorAll(".box-hidden-nav");
	var boxForm=document.querySelectorAll(".box-form");
	var boxHiddenCol=document.querySelectorAll(".box-hidden-col");
	
	if(width>992){
		for(var x=0;x<boxHiddenNav.length;x++){
			boxHiddenNav[x].style.display="none";
			boxHiddenCol[x].style.display="none";
		}
		for(var x=0;x<boxForm.length;x++){
			boxForm[x].style.display="inline";
		}
	}else{
		for(var x=0;x<boxForm.length;x++){
				boxForm[x].style.display="none";
		}
	}
	
	var boxBars=document.querySelectorAll(".box-bars");
	var boxTog=document.querySelectorAll(".box-tog");

	window.addEventListener("resize",function(e){
		var width=screen.width;
		var boxHiddenNav=document.querySelectorAll(".box-hidden-nav");
		var boxForm=document.querySelectorAll(".box-form");
		var boxHiddenCol=document.querySelectorAll(".box-hidden-col");
		if(width>992){
			for(var x=0;x<boxHiddenNav.length;x++){
				boxHiddenNav[x].style.display="none";
				boxHiddenCol[x].style.display="none";
			}
			for(var x=0;x<boxForm.length;x++){
				boxForm[x].style.display="inline";
			}
		}else{
			for(var x=0;x<boxForm.length;x++){
				boxForm[x].style.display="none";
			}
		}
	})

	$(boxBars).click(function(e){
		var parent=e.target.offsetParent;
		var sib=parent.nextElementSibling;
		var sib1=sib.nextElementSibling;
		var contentBox=sib1.nextElementSibling;
		var hiddenCol=contentBox.firstElementChild;
		if(hiddenCol.style.display==="none"){
			hiddenCol.style.display="inline";
		}else{
			hiddenCol.style.display="none";
		}

	})
	

	$(boxTog).click(function(e){
		var parent=e.target.offsetParent;
		var hiddenNav=parent.nextElementSibling;
		$(hiddenNav).slideToggle('slow');
	})

	//GOOGLE QUERY
	var googleBtn=document.querySelector("#google-btn");
	googleBtn.addEventListener("click",function(e){
		var googleQ=document.querySelector("#google-q").value;
		var googleInput=document.querySelector("#query_g");
		var googleSubmit=document.querySelector("#submit_g");
		googleInput.value=googleQ;
		googleSubmit.click()
		//console.log(googleQ)
		
	})

	

	
})