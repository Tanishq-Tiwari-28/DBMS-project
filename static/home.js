// Find the placeholder element
var placeholder = document.getElementById('about-us-placeholder');

// Create a new XMLHttpRequest object
var xhr = new XMLHttpRequest();

// Set up the onload event handler
xhr.onload = function() {
  // Set the inner HTML of the placeholder element to the response text
  placeholder.innerHTML = xhr.responseText;
};

// Open a GET request to the about-us.html file
xhr.open('GET', 'about-us.html');

// Send the request
xhr.send();
