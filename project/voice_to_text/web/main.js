function startRecording() {
    const language = document.getElementById('language').value;
    eel.start_recording(language);
}

function stopRecording() {
    const language = document.getElementById('language').value;
    eel.stop_recording(language);
}

function saveTranscription() {
    const fileName = document.getElementById('fileName').value;
    if (fileName) {
        eel.save_transcription(fileName);
    } else {
        alert("Please enter a file name.");
    }
}

eel.expose(update_transcription);
function update_transcription(text) {
    document.getElementById('transcription').innerText = text || "No transcription available.";
}

eel.expose(show_status);
function show_status(message) {
    alert(message);
}

eel.expose(show_popup);
function show_popup(message) {
    alert(message);
}
