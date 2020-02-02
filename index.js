
 function submitForm (event) {
    event.preventDefault()
    const   username = document.getElementById('username'),
            password = document.getElementById('password'),
            confirmPassword = document.getElementById('confirmPassword'),
            email = document.getElementById('email'),
            usernameError = document.getElementById('usernameError'),
            passwordError = document.getElementById('passwordError'),
            confirmError = document.getElementById('confirmError'),
            emailError = document.getElementById('emailError'),
            select = document.getElementById('inputGroupSelect01'),
            selectError = document.getElementById('selectError'),
            form = document.getElementById('submitForm')

    const validEmailRegex = 
    RegExp(/^(([^<>()[\].,;:\s@"]+(\.[^<>()[\].,;:\s@"]+)*)|(".+"))@(([^<>()[\].,;:\s@"]+\.)+[^<>()[\].,;:\s@"]{2,})$/i);
   
    if (username.value === '') {
        usernameError.innerHTML ='!Important'
        username.classList.add('error')
    } else if (password.value === '') {
        passwordError.innerHTML ='!Important'
        password.classList.add('error')
    } else if (password.value <= 8 && password > 1) {
        passwordError.innerHTML ='!Too short'
        password.classList.add('error')
    } else if (password.value > 8) {
        passwordError.innerHTML ='!Max-length is 16'
        password.classList.add('error')
    } else if (confirmPassword.value !== password.value) {
        confirmError.innerHTML ='Password-mismatch'
        confirmPassword.classList.add('error')
    } else if (email.value === '') {
        emailError.innerHTML ='!Important'
        email.classList.add('error')
    } else if (email.value !== validEmailRegex && email.value > 1) {
        emailError.innerHTML ='Invalid Email'
        email.classList.add('error')
    } else if (select.value === '') {
        selectError.innerHTML = '!Important'
    }
        else {
            console.log(email.value)
            console.log(username.value)
            console.log(password.value)
            console.log(select.value)
            form.reset()
        }
}