function loading() {
    alert("Loading weather report...")
}
function remov(){
    x=document.getElementById("b-col");
    x.remove();
}

async function getgithub(){
    img=document.getElementById('img');
    select=document.getElementById('select');
    loc=document.getElementById('loc');
    loc=loc.value;
    console.log(loc);
    var response= await fetch(`http://api.weatherapi.com/v1/current.json?key=d3d61be91bed4e84a85131926231312&q=${loc}&aqi=no`);
    var coderData = await response.json();
    img.src=coderData.current.condition.icon;
    condition.innerText=coderData.current.condition.text;
    if(select.value=='°C'){
        temp1.innerText=coderData.current.temp_c+select.value; 
    } 
    else{
        temp1.innerText=coderData.current.temp_f+select.value; 
    }
    
}  