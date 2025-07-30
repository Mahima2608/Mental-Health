// document.getElementById('user-input').addEventListener('keydown', function(event) {
//     if (event.key === 'Enter') {
//         sendMessage();
//     }
// });

// function sendMessage() {
//     const userInput = document.getElementById('user-input').value;
//     if (userInput.trim() === "") return;

//     const chatBox = document.getElementById('chat-box');
//     const userMessage = document.createElement('div');
//     userMessage.className = 'message user-message';
//     userMessage.textContent = userInput;
//     chatBox.appendChild(userMessage);
//     document.getElementById('user-input').value = '';

//     fetch('/get_response', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ message: userInput })
//     })
//     .then(response => response.json())
//     .then(data => {
//         const botMessage = document.createElement('div');
//         botMessage.className = 'message bot-message';
//         botMessage.textContent = data.response;
//         chatBox.appendChild(botMessage);
//         chatBox.scrollTop = chatBox.scrollHeight;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//     });
// }
