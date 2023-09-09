<?php
//error_reporting(E_ALL);
/*
* 18 Engine backward
* 23 Engine Forward
* 24 Steer left
* 25 Steer right
* 17 Led 1
* 27 Led 2
*/
//shell_exec("python cleanup.py");
//shell_exec("gpio -g mode 17 out");
//shell_exec("gpio -g mode 27 out");
//while(1){        
	//shell_exec("gpio -g write 17 1");
	//shell_exec("gpio -g write 27 1");
	//sleep(1);
//	shell_exec("gpio -g write 17 0");
//	shell_exec("gpio -g write 27 0");
//}
		//$gpio_on=shell_exec("gpio -g write 27 1");
		//sleep(0.5);
		//shell_exec("gpio -g write 27 0");
		

		require_once("class.ajax.php");
		$aF= new  AjaxFunc();
		echo 'amir';
		print_r( intval($aF->distance() ));
?>
<html>
<head>
<meta charset="utf-8">
<title>Suphra Project by Amir</title>
<script src="js/jquery-2.2.2.min.js"></script>
<script src="js/general.js"></script>
<link href="css/style.css" rel="stylesheet" type="text/css">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
	<div class="container">
    		<div class="output">
            	<div class="title">Output:</div>
                <div class="screen"><img src="<?='http://'.$_SERVER['HTTP_HOST'] ?>:8093/?action=stream" /></div>
            </div>
            <div class="controls">
            	<table class="arrows">
                	<tr><td></td><td class="up" onClick="go('forward',0);"></td><td></td></tr>
                	<tr><td class="left" onClick="go('left',2)"></td><td class="stop" onClick="go('stop')"></td><td class="right" onClick="go('right',2)"></td></tr>
                	<tr><td></td><td class="down" onClick="go('backward',10)"></td><td></td></tr>
                </table>
            </div>
            <div class="clear"></div>
    </div>
</body>
</html>
