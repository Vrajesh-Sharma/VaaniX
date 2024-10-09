document.getElementById("textForm").addEventListener("submit", function(event){
    event.preventDefault();

    var formData = new FormData(this);

    fetch("/convert", {
        method: "POST",
        body: formData
    })
    .then(response => response.blob())
    .then(blob => {
        var url = URL.createObjectURL(blob);
        var audio = document.getElementById("audio");
        audio.src = url;
        document.getElementById("audioPlayer").style.display = "block";
    })
    .catch(error => console.error('Error:', error));
});