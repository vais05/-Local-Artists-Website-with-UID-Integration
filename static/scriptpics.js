
        $(document).ready(function() {
            $.ajax({
                type: "GET",
                url: "{{ url_for('static', filename='images.csv') }}",
                dataType: "text",
                success: function(data) {
                    var lines = data.split("\n");
    
                    var container = document.getElementById("imageContainer");
                    container.classList.add("builder");
    
                    for (var i = 1; i <= 5; i++) {
                        var imageUrl = lines[i].split(",")[0];
                        if (imageUrl) {
                            var img = document.createElement("img");
                            img.src = imageUrl;
                            container.appendChild(img);
                        }
                    }
    
                    var cat3 = document.getElementById("cat3");
                    cat3.classList.add("builder"); // Add the 'builder' class to cat3
    
                    for (var i = 6; i < 11; i++) {
                        var imageUrl = lines[i].split(",")[0];
                        if (imageUrl) {
                            var img = document.createElement("img");
                            img.src = imageUrl;
                            cat3.appendChild(img);
                        }
                    }

                    var cat2 = document.getElementById("cat2");
                    cat2.classList.add("builder"); // Add the 'builder' class to cat2
                    for (var i = 11; i < 16; i++) {
                        var imageUrl = lines[i].split(",")[0];
                        if (imageUrl) {
                            var img = document.createElement("img");
                            img.src = imageUrl;
                            cat2.appendChild(img);
                        }
                    }

                    var cat4 = document.getElementById("cat4");
                    cat4.classList.add("builder"); // Add the 'builder' class to cat2
                    for (var i = 16; i < 21; i++) {
                        var imageUrl = lines[i].split(",")[0];
                        if (imageUrl) {
                            var img = document.createElement("img");
                            img.src = imageUrl;
                            cat4.appendChild(img);
                        }
                    }

                    var cat4 = document.getElementById("cat5");
                    cat4.classList.add("builder"); // Add the 'builder' class to cat2
                    for (var i = 21; i < 26; i++) {
                        var imageUrl = lines[i].split(",")[0];
                        if (imageUrl) {
                            var img = document.createElement("img");
                            img.src = imageUrl;
                            cat5.appendChild(img);
                        }
                    }
                }
            });
        });
 