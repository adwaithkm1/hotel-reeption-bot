function sendMessage() {
    let userInput = document.getElementById("userInput").value;

    fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: userInput })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.response;
    });
}
