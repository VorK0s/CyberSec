const video_btn = document.getElementById("video_btn");
const lastNews_btn = document.getElementById("lastNews_btn");
const recommend_btn = document.getElementById("recommend_btn");
const ourAchievement_btn = document.getElementById("ourAchievement_btn");
const about_btn = document.getElementById("about_btn");

video_btn.addEventListener("click", sectionsToggle, false)
lastNews_btn.addEventListener("click", sectionsToggle, false)
recommend_btn.addEventListener("click", sectionsToggle, false)
ourAchievement_btn.addEventListener("click", sectionsToggle, false)
about_btn.addEventListener("click", sectionsToggle, false)

video_btn.id = '1'
lastNews_btn.id = '2'
recommend_btn.id = '3'
ourAchievement_btn.id = '4'
about_btn.id = '5'


function sectionsToggle(event) {
	let sect1 = document.getElementById("video_section");
	let sect2 = document.getElementById("lastNews_section");
	let sect3 = document.getElementById("recommend_section");
	let sect4 = document.getElementById("ourAchievement_section");
	let sect5 = document.getElementById("about_section");

	let btn1 = document.getElementById("video_lamp");
	let btn2 = document.getElementById("lastNews_lamp");
	let btn3 = document.getElementById("recommend_lamp");
	let btn4 = document.getElementById("ourAchievement_lamp");
	let btn5 = document.getElementById("about_lamp");

	let show_now= document.getElementsByClassName('show');
	show_now[0].classList.remove('show');

	let active= document.getElementsByClassName('active');
	active[0].classList.remove('active');

	if (event.target.id === '1') {
		sect1.classList.add("show");
		btn1.classList.add("active");
	}
	if (event.target.id === '2') {
		sect2.classList.add("show");
		btn2.classList.add("active");
	}
	if (event.target.id === '3') {
		sect3.classList.add("show");
		btn3.classList.add("active");
	}
	if (event.target.id === '4') {
		sect4.classList.add("show");
		btn4.classList.add("active");
	}
	if (event.target.id === '5') {
		sect5.classList.add("show");
		btn5.classList.add("active");
	}
}