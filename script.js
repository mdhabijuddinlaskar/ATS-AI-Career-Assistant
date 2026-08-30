// ATS CHECKER

const atsForm = document.getElementById("atsForm");

if (atsForm) {

    atsForm.addEventListener("submit", async function(event) {

        event.preventDefault();

        const formData = new FormData();

        const resume = document.getElementById("resume").files[0];

        const jobDescription =
            document.getElementById("job_description").value;

        formData.append("resume", resume);

        formData.append(
            "job_description",
            jobDescription
        );

        const response = await fetch("/check-ats", {

            method: "POST",

            body: formData

        });

        const data = await response.json();

        const result =
            document.getElementById("result");

        if (data.error) {

            result.innerHTML =
                `<p>${data.error}</p>`;

        } else {

            result.innerHTML = `
                <h2>ATS Score: ${data.score}%</h2>

                <p>${data.message}</p>

                <h3>Job Keywords:</h3>

                <p>
                    ${data.keywords_found.join(", ")}
                </p>
            `;
        }

    });

}


// CHATBOT

async function sendMessage() {

    const input =
        document.getElementById("message");

    const message =
        input.value.trim();

    if (!message) return;

    const chatBox =
        document.getElementById("chat-box");

    chatBox.innerHTML += `
        <div class="user-message">
            <b>You:</b> ${message}
        </div>
    `;

    input.value = "";

    try {

        const response =
            await fetch("/chat", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    message: message
                })

            });

        const data =
            await response.json();

        chatBox.innerHTML += `
            <div class="ai-message">
                <b>AI:</b> ${data.response}
            </div>
        `;

        chatBox.scrollTop =
            chatBox.scrollHeight;

    }

    catch (error) {

        console.error(error);

    }

}