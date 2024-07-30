var input = document.getElementsByClassName("form-control")
        for (i = 0; i < input.length; i++) {
            input[i].addEventListener("focus", () => {
                var outer = event.srcElement.parentNode
                outer.style["border"] = "2px solid #657dde"
            })
            input[i].addEventListener("focusout", () => {
                var outer = event.srcElement.parentNode
                outer.style["border"] = "1px solid #8c8c8c"
            })
        }
        $('.togglePwdicon').on("click", function() {
            var password = $(this).prev("td")
            password[0].style["-webkit-text-security"] = "none"
            var icon = $(this)[0].firstChild
            icon.classList.remove("fa-eye")
            icon.classList.add("fa-eye-slash")

            setTimeout(function() {
                password[0].style["-webkit-text-security"] = "disc"
                icon.classList.remove("fa-eye-slash")
                icon.classList.add("fa-eye")
            }, 2000)
        })

        $('.displaypassword').on("click", function() {
            let showpwdicon = $(this)[0]
            var pwd = $(this).prev("input")[0]
            pwd.setAttribute("type", "text")
            showpwdicon.classList.remove("fa-eye")
            showpwdicon.classList.add("fa-eye-slash")
            setTimeout(function() {
                pwd.setAttribute("type", "password")
                showpwdicon.classList.remove("fa-eye-slash")
                showpwdicon.classList.add("fa-eye")
            }, 3000)
        })
        $(".update").on("click", function() {
            var id
            var element = $(this)[0].getAttribute("data-id")
            var folder_id = $(this)[0].getAttribute("data-folder")
            id = element
            var element = document.getElementById("update_rec_id")
            element.setAttribute("value", id)
            document.querySelector("select[name='folder']").value = folder_id;
        })
        $("#updatebtn").on("click", function(clickEvent) {
            var password = myform.password.value
            var c_password = myform.confirmpassword.value
            var updateform_error = document.getElementsByClassName("updt_form_error")[0]
            if (password === "" || c_password === "") {
                clickEvent.preventDefault()
                updateform_error.classList.remove("hide")
                updateform_error.classList.add("display")
                updateform_error.innerText = "The fields cannot be empty"
                change_style(updateform_error)
            } else if (c_password != password) {
                clickEvent.preventDefault()
                updateform_error.classList.remove("hide")
                updateform_error.classList.add("display")
                updateform_error.innerText = "The two passwords didn't match!"
                change_style(updateform_error)
            } else {
                password.value = ""
                c_password.value = ""
                $("#updatemodal").modal('hide')
            }
        })

        function change_style(element) {
            setTimeout(function() {
                element.classList.remove("display")
                element.classList.add("hide")
            }, 3000)
        }

        $(".del").on("click", function() {
            var id
            var element = $(this)[0].getAttribute("data-id")
            id = element
            var ele = document.getElementById("delete_record_id")
            ele.setAttribute("value", id)
        })

        var message = document.getElementsByClassName("message")[0]
        setTimeout(function() {
            message.style.visibility = "hidden"
            message.style.height = 0
        }, 3000)

        $("#modaladdaccbtn").on("click", function(clickEvent) {
            var account_name = addform.account_name.value
            var user_name = addform.user_name.value
            var password = addform.password.value
            var addform_error = document.getElementsByClassName("add_form_error")[0]
            var text = "The fields cannot be empty"
            if (account_name === "" || user_name === "" || password === "") {
                clickEvent.preventDefault()
                addform_error.classList.add("display")
                addform_error.classList.add("hide")
                addform_error.innerHTML = text
                change_style(addform_error)
            } else {
                document.getElementById("addform").submit()
            }
        })
        $(".updtclose").on("click", function() {
            myform.password.value = ""
            myform.confirmpassword.value = ""
            document.getElementById("update_rec_id").removeAttribute("value")
        })
        $(".addbtnclose").on("click", function() {
            addform.account_name.value = ""
            addform.user_name.value = ""
            addform.password.value = ""
        })


        var span = "<span class='fa fa-eye mx-2 displaypassword'></span>"
        document.getElementsByClassName("outerdiv")[1].innerHTML+=span
        $('.displaypassword').on("click",function(){
            let showpwdicon = $(this)[0]
            var pwd = $(this).prev("input")[0]
            pwd.setAttribute("type","text")
            showpwdicon.classList.remove("fa-eye")
            showpwdicon.classList.add("fa-eye-slash")
            setTimeout(function(){
                pwd.setAttribute("type","password")
                showpwdicon.classList.remove("fa-eye-slash")
                showpwdicon.classList.add("fa-eye")
            },3000)
        })

        var input = document.getElementsByClassName("form-control")
        for(i=0;i<input.length;i++){
            input[i].addEventListener("focus",() => {
                var outer = event.srcElement.parentNode
                outer.style["border"] = "1px solid #657dde"
                })
            input[i].addEventListener("focusout",() => {
                var outer = event.srcElement.parentNode
                outer.style["border"] = "1px solid #8c8c8c"
                })
            }

        var message = document.getElementsByClassName("message")[0]
        setTimeout(function(){
            message.remove()},3000)