const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  var file = e.target.files[0];
  var reader = new FileReader();

  reader.onload = function (event) {
    var img = document.createElement("img");
    img.src = event.target.result;
    img.classList.add("preview-image");

    // Clear any existing preview images
    var preview = document.getElementById("preview");
    preview.innerHTML = "";
    
    // Append the new image preview
    preview.appendChild(img);

    // Set the hidden input field value to the image data
    var hiddenInput = document.createElement("input");
    hiddenInput.type = "hidden";
    hiddenInput.name = "image_data";
    hiddenInput.value = event.target.result;
    preview.appendChild(hiddenInput);
  };

  reader.readAsDataURL(file);
});
