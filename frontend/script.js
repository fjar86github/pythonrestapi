function fetchData(endpoint) {
  fetch(endpoint)
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').innerText = JSON.stringify(data);
    })
    .catch(err => console.error(err));
}
