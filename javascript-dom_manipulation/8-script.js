document.addEventListener('DOMContentLoaded', () => {
	const helloElement = document.getElementById('hello');
	const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  
	fetch(url)
	  .then(response => response.json())
	  .then(data => {
		helloElement.textContent = data.hello;
	  })
	  .catch(error => {
		console.error('Error fetching data:', error);
	  });
  });
  