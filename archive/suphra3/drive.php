<?php
$dir=$_POST["dir"];
$delay=$_POST["delay"];

	if(!empty($dir)){
		require_once("class.ajax.php");
		$aF= new  AjaxFunc();
		$aF->blink("1",0);
		$aF->blink("2",0);
		if($dir=="forward"){
			$aF->drive("forward",$delay);
		}else if($dir=="backward"){
			$aF->drive("backward",$delay);
		}else if($dir=="left"){
			$aF->steer("left",$delay);
		}else if($dir=="right"){
			$aF->steer("right",$delay);
		}else if($dir=="stop"){
			$aF->stop();
		}
	}
?>
