var st_fwd=0;
var st_bck=0;
var st_lft=0;
var st_rght=0;
$(function() {
	function drive(dir,delay){
		$.ajax({
		  method: "POST",
		  url: "drive.php",
		  data: { dir: dir, delay: delay }
		})
		  .done(function( msg ) {
			$('screen').html(msg);
		  });	
	}
	
	function go(dir,delay){
		if(dir.localeCompare("forward")==0){
			if(st_fwd==0){
				drive("forward",delay);
				st_fwd==1;
			}else{
				drive("stop",0);
				st_fwd==0;
			}
		}else if(dir.localeCompare("backward")==0){
			if(st_bck==0){
				drive("backward",delay);
				st_bck==1;
			}else{
				drive("stop",0);
				st_bck==0;
			}
		}else if(dir.localeCompare("left")==0){
			if(st_lft==0){
				drive("left",delay);
				st_lft==1;
			}else{
				drive("stop",0);
				st_lft==0;
			}
		}else if(dir.localeCompare("right")==0){
			if(st_rght==0){
				drive("right",delay);
				st_rght==1;
			}else{
				drive("stop",0);
				st_rght==0;
			}
		}else if(dir.localeCompare("stop")==0){
			drive("stop",0);
		}
		
	}
});
