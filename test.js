import fetch from 'node-fetch';

const url = 'http://127.0.0.1:3000/adduser';
const data = {
    username: 'John Doe',
    email: 'john.doe@example.com'
};

fetch(url, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => {
    if (!response.ok) {
        response.text().then(text => {
            throw new Error(`Network response was not ok: ${response.status} ${response.statusText} - ${text}`);
        });
    }
    return response.json();
})
.then(data => console.log('Success:', data))
.catch(error => console.error('Error:', error));