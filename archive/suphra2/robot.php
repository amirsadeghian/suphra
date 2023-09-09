<?php

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
?>
<html>
<head>
<meta charset="utf-8">
<title>Suphra Project by Amir</title>
<script src="js/jquery-2.2.2.min.js"></script>
<script src="js/general.js"></script>
<link href="css/style.css" rel="stylesheet" type="text/css">
</head>

<body>
	<div class="container">
    		<div class="output">
            	<div class="title">Output:</div>
                <div class="screen"></div>
            </div>
            <div class="controls">
            	<table class="arrows">
                	<tr><td></td><td class="up" onKeyDown="go('forward',0)" onKeyUp="go('forward',0)"></td><td></td></tr>
                	<tr><td class="left" onKeyDown="go('left',0)" onKeyUp="go('left',0)"></td><td class="stop" onClick="go('stop)"></td><td class="right" onKeyDown="go('right',0)"  onKeyUp="go('right',0)"></td></tr>
                	<tr><td></td><td class="down" onKeyDown="go('backward',0)" onKeyUp="go('backward',0)"></td><td></td></tr>
                </table>
            </div>
            <div class="clear"></div>
    </div>
</body>
</html>
