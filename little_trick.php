# index.php
<?php
    error_reporting(0);
    highlight_file(__FILE__);
    $nep = $_GET['nep'];
    $len = $_GET['len'];
    if(intval($len)<8 && strlen($nep)<13){
        eval(substr($nep,0,$len));
    }else{
        die('too long!');
    }
?>
# nepctf.php
<?php
$flag = 'NepCTF{n3pn3p_l1ttle_tr1ck_c0me_bAck}';
?>