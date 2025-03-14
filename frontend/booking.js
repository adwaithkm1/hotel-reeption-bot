function bookRoom() {
    fetch('/book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ guest_id: 1, room_number: 101 })
    })
    .then(response => response.json())
    .then(data => alert(data.message));
}
