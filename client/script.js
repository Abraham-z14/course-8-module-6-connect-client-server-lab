const API_URL = "http://localhost:5000/events";

const form = document.querySelector("form");
const titleInput = document.querySelector("#title");
const eventList = document.querySelector("#event-list");


function renderEvent(event) {
    const li = document.createElement("li");
    li.textContent = event.title;
    eventList.appendChild(li);
}


function loadEvents() {
    fetch(API_URL)
        .then((response) => {
            if (!response.ok) {
                throw new Error("Could not load events");
            }

            return response.json();
        })
        .then((events) => {
            eventList.innerHTML = "";
            events.forEach(renderEvent);
        })
        .catch((error) => {
            console.error("Error loading events:", error);
        });
}


form.addEventListener("submit", (event) => {
    event.preventDefault();

    const title = titleInput.value.trim();

    if (!title) {
        alert("Please enter an event title.");
        return;
    }

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ title: title }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error("Could not create event");
            }

            return response.json();
        })
        .then((newEvent) => {
            renderEvent(newEvent);
            form.reset();
        })
        .catch((error) => {
            console.error("Error creating event:", error);
        });
});


loadEvents();