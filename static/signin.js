document.addEventListener("DOMContentLoaded", () => {

    document.querySelectorAll(".input").forEach(input => {
        input.addEventListener("input", () => {
            if ((document.querySelector('.usrnm').value.length === 0) || (document.querySelector('.pswrd').value.length === 0)) {
                document.querySelector('input[type="submit"]').disabled = true;
                console.log(document.querySelector('input[type="submit"]').disabled == true);
            }
            else {
                document.querySelector('input[type="submit"]').disabled = false;
                onsole.log(document.querySelector('input[type="submit"]').disabled == true);
            }
        });
    });
})
