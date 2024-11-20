document.getElementById("imageUpload").onchange = function(event) {
    const imagePreview = document.getElementById("imagePreview");
    const file = event.target.files[0];

    if (file) {
        // Display the image preview
        imagePreview.src = URL.createObjectURL(file);
        imagePreview.style.display = "block";
    } else {
        imagePreview.style.display = "none";
    }
};

document.getElementById("predictButton").onclick = function() {
    const imageInput = document.getElementById("imageUpload");

    if (imageInput.files && imageInput.files[0]) {
        document.getElementById("resultSection").innerHTML = "<p>Predicting... (This will display the result once integrated)</p>";
    } else {
        alert("Please upload an image first.");
    }
};
