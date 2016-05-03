var html=document.getElementsByTagName('html')[0];
var clientW=document.documentElement.clientWidth;
var clientH=document.documentElement.clientHeight;
if(window.orientation==90 ||window.orentation==-90){
	html.style.fontSize=clientH/20+'px';
}
html.style.fontSize=clientW/20+'px';
console.log(html.style.fontSize);