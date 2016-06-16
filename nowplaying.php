<head>
<style>
body {
    background: gray;
}
#main {
    color: rgba(255, 255, 255, 0.8);
    margin: 0px 0px 0px 0px;
    padding: 2px 2px 2px 2px;
    font-family: "Trebuchet MS";
    font-size: 20px;
    text-align: center;
    width: 700px;
} 
</style>

<script type="text/javascript"
    src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
<script>
$(function() {
    startRefresh();
});

function startRefresh() {
    setTimeout(startRefresh,5000);
    $.get('playing.php', function(data) {
        $('#main').html(data);    
    });
}
</script>
</head>

<html>
<body>
<div id="main"> 
</div>
</body>
</html>
