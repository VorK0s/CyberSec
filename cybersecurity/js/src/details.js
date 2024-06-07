document.querySelectorAll('.news').forEach((detail) => {
	detail.addEventListener('toggle', function () {
		const content = this.querySelector('.news__content');
		if (this.open) {
			content.classList.remove('collapsed');
			content.style.maxHeight = content.scrollHeight + 'px';
		} else {
			content.style.maxHeight = content.scrollHeight + 'px';
			setTimeout(() => {
				content.classList.add('collapsed');
				content.style.maxHeight = null;
			}, 0);
		}
	});
});