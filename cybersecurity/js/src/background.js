document.addEventListener('DOMContentLoaded', addNewElements);


function getRndInteger(min, max) {
	return Math.floor(Math.random() * (max - min + 1)) + min;
}


function addNewElements() {
	let container = document.getElementById('dynamic_background');

	for (let i = 0; i < 400; i++) {
		let newElement = document.createElement('span');

		let rand = getRndInteger(1, 30);

		if (rand === 1) {
			newElement.classList.add('animateBG');
		}
		else if (rand === 2) {
			newElement.classList.add('animateBG2');
		}
		else if (rand === 3) {
			newElement.classList.add('animateBG3');
		}

		container.appendChild(newElement);
	}
}
