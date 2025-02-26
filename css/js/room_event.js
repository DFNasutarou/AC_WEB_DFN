document.addEventListener("DOMContentLoaded", function () {
    const roomsContainer = document.getElementById("rooms");
    for (let i = 0; i < 6; i++) {
        const roomDiv = document.createElement("div");
        roomDiv.classList.add("room");
        roomDiv.innerHTML = `<img class="img" src="css/picture/glass.png" />`;
        roomsContainer.appendChild(roomDiv);
    }
});