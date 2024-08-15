$(document).ready(function() {
    // Focus and focusout border change for input fields
    var input = document.getElementsByClassName("form-control");
    for (i = 0; i < input.length; i++) {
        input[i].addEventListener("focus", function() {
            var outer = event.srcElement.parentNode;
            outer.style["border"] = "2px solid #657dde";
        });
        input[i].addEventListener("focusout", function() {
            var outer = event.srcElement.parentNode;
            outer.style["border"] = "1px solid #8c8c8c";
        });
    }

    // Toggle password visibility
    $(document).on('click', '.togglePwdicon', function() {
        console.log("Toggle button clicked"); // Add this line
        let input = $(this).closest('tr').find('.password-input');
        let type = input.attr('type') === 'password' ? 'text' : 'password';
        input.attr('type', type);
        $(this).toggleClass('fa-eye fa-eye-slash');
    });    

    // Update modal handling
    $(".update").on("click", function() {
        var id = $(this).data("id");
        var folder = $(this).data("folder");
        $("#update_rec_id").val(id);
        $("select[name='folder']").val(folder);
    });

    // Delete modal handling
    $(document).on("click", ".del", function() {
        var id = $(this).data("id");
        console.log("ID to delete:", id);  // Debugging line
        $("#delete_record_id").val(id);
    });

    // Form validation for update modal
    $("#updatebtn").on("click", function(clickEvent) {
        var password = myform.password.value;
        var c_password = myform.confirmpassword.value;
        var updateform_error = document.getElementsByClassName("updt_form_error")[0];
        if (password === "" || c_password === "") {
            clickEvent.preventDefault();
            updateform_error.classList.remove("hide");
            updateform_error.classList.add("display");
            updateform_error.innerText = "The fields cannot be empty";
            change_style(updateform_error);
        } else if (c_password != password) {
            clickEvent.preventDefault();
            updateform_error.classList.remove("hide");
            updateform_error.classList.add("display");
            updateform_error.innerText = "The two passwords didn't match!";
            change_style(updateform_error);
        } else {
            password.value = "";
            c_password.value = "";
            $("#updatemodal").modal('hide');
        }
    });

    // Utility function for showing/hiding error messages
    function change_style(element) {
        setTimeout(function() {
            element.classList.remove("display");
            element.classList.add("hide");
        }, 3000);
    }

    // Remove messages after 3 seconds
    var message = document.getElementsByClassName("message")[0];
    setTimeout(function() {
        message.style.visibility = "hidden";
        message.style.height = 0;
    }, 3000);

    // Add account modal validation
    $("#modaladdaccbtn").on("click", function(clickEvent) {
        var account_name = addform.account_name.value;
        var user_name = addform.user_name.value;
        var password = addform.password.value;
        var addform_error = document.getElementsByClassName("add_form_error")[0];
        var text = "The fields cannot be empty";
        if (account_name === "" || user_name === "" || password === "") {
            clickEvent.preventDefault();
            addform_error.classList.add("display");
            addform_error.classList.remove("hide");
            addform_error.innerHTML = text;
            change_style(addform_error);
        } else {
            document.getElementById("addform").submit();
        }
    });

    // Clear update modal on close
    $(".updtclose").on("click", function() {
        myform.password.value = "";
        myform.confirmpassword.value = "";
        document.getElementById("update_rec_id").removeAttribute("value");
    });

    // Clear add account modal on close
    $(".addbtnclose").on("click", function() {
        addform.account_name.value = "";
        addform.user_name.value = "";
        addform.password.value = "";
    });

    // Toggle password visibility (using a span element)
    var span = "<span class='fa fa-eye mx-2 displaypassword'></span>";
    document.getElementsByClassName("outerdiv")[1].innerHTML += span;
    $('.displaypassword, .togglePwdicon').on("click", function() {
        var pwdInput = $(this).prev("input, td");
        var icon = $(this).find("i");

        if (pwdInput.attr("type") === "password" || pwdInput.css("-webkit-text-security") === "disc") {
            pwdInput.attr("type", "text").css("-webkit-text-security", "none");
            icon.removeClass("fa-eye").addClass("fa-eye-slash");
        } else {
            pwdInput.attr("type", "password").css("-webkit-text-security", "disc");
            icon.removeClass("fa-eye-slash").addClass("fa-eye");
        }
    });

    // Duplicate focus event listeners for input fields
    var input = document.getElementsByClassName("form-control");
    for (i = 0; i < input.length; i++) {
        input[i].addEventListener("focus", function() {
            var outer = event.srcElement.parentNode;
            outer.style["border"] = "1px solid #657dde";
        });
        input[i].addEventListener("focusout", function() {
            var outer = event.srcElement.parentNode;
            outer.style["border"] = "1px solid #8c8c8c";
        });
    }

    // Remove messages after 3 seconds
    var message = document.getElementsByClassName("message")[0];
    setTimeout(function() {
        message.remove();
    }, 3000);
});
