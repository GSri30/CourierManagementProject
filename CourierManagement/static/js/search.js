couriers=document.getElementById("couriers");
noresult=document.getElementById("no-results");
noresult.getElementsByTagName("h4").item(0).style.display="none";

//Performs a linear search
//!Slow

function searchInput(search){
    noresult.getElementsByTagName("h4").item(0).style.display="none";
    searchData=search.value.toLowerCase().split(" ")
    var finalBool=false;
    for(var i=3;i<couriers.childNodes.length;i+=4){
        courier="";
        for(var j=1;j<couriers.childNodes[i].childNodes.length;j+=2){
            if(couriers.childNodes[i].childNodes[j].childNodes[0])
            courier+=couriers.childNodes[i].childNodes[j].childNodes[0].textContent.toLowerCase()+" ";
        }
        var found=true;
        for(var k=0;k<searchData.length;k++){
            if(!courier.includes(searchData[k])){
                found=false;break;
            }
        }
        if(found){
            couriers.childNodes[i-2].style.display="";
            finalBool=true;
        }
        else{
            couriers.childNodes[i-2].style.display="none";
        }
    }
    if(!finalBool){
        noresult.getElementsByTagName("h4").item(0).style.display="";
    }
}