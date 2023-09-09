<?php
// C 2016 Amir Sadeghian (root25.com)
class AjaxFunc{
	public function distance(){
		$dist = shell_exec("sudo python distance.py 2>&1");
		return $dist;
	}
	
	public function steer($dir,$delay="0"){
		if($dir=="left"){ $dir="24"; }else{ $dir="25"; }
		if($delay!="0"){
			shell_exec("gpio -g mode ".$dir." out");
			shell_exec("gpio -g write ".$dir." 1");
			sleep($delay);
			shell_exec("gpio -g write ".$dir." 0");
			shell_exec("sudo python cleanup.py");	
		}else{
			while(1){
				shell_exec("gpio -g mode ".$dir." out");
				shell_exec("gpio -g write ".$dir." 1");
			}
		}
	}

	public function drive($dir,$delay="0"){
		if($dir=="backward"){ 
			$dir="18";
			if($delay!="0"){
				shell_exec("gpio -g mode ".$dir." out");
				shell_exec("gpio -g write ".$dir." 1");
				sleep($delay);
				shell_exec("gpio -g write ".$dir." 0");
				shell_exec("sudo python cleanup.py");
			}else{
				while(1){
					shell_exec("gpio -g mode ".$dir." out");
					shell_exec("gpio -g write ".$dir." 1");
				}
			}
		}else{ 
			$dir="23";
			if($delay!="0"){
				shell_exec("gpio -g mode ".$dir." out");
				shell_exec("gpio -g write ".$dir." 1");
				sleep($delay);
				shell_exec("gpio -g write ".$dir." 0");
				shell_exec("sudo python cleanup.py");
			}else{
				while(1){
					$dist = $this->distance();
					if(intval($dist)<10){
						$this->stop();
						return false;
						break;
					}else{
						shell_exec("gpio -g mode ".$dir." out");
						shell_exec("gpio -g write ".$dir." 1");
					}
				}
			} 
		}		
	}
	
	public function stop(){		
                shell_exec("gpio -g mode 18 out");
                shell_exec("gpio -g mode 23 out");
				shell_exec("gpio -g mode 24 out");
                shell_exec("gpio -g mode 25 out");
                shell_exec("gpio -g write 18 0");
                shell_exec("gpio -g write 23 0");
                shell_exec("gpio -g write 24 0");
                shell_exec("gpio -g write 25 0");

                shell_exec("sudo python cleanup.py");
	}

	public function blink($led,$delay="0"){
		if($led=="1"){ $led="17"; }else{ $led="27"; }
                shell_exec("gpio -g mode ".$led." out");
                shell_exec("gpio -g write ".$led." 1");
                //sleep($delay);
                //shell_exec("gpio -g write ".$led." 0");
                //shell_exec("sudo python cleanup.py");
	}


}
?>

