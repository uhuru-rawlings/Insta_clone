const Validatesignup = () =>{
    let username = document.getElementById("usernames");
    let useremail = document.getElementById("useremails");
    let userimage = document.getElementById("userimages");
    let passwords = document.getElementById("passwords");
    let cpasswords = document.getElementById("confirmpassword");

    if(username.value.trim() === "" || useremail.value.trim() === "" || userimage.value.trim() === "" || passwords.value.trim() === "" || cpasswords.value.trim() === ""){
        if(username.value.trim() === ""){
            username.style.borderColor = "red";
            return false;
        }else if(useremail.value.trim() === ""){
            useremail.style.borderColor = "red";
            return false;
        }else if(userimage.value.trim() === ""){
            userimage.style.borderColor = "red";
            return false;
        }else if(passwords.value.trim() === ""){
            passwords.style.borderColor = "red";
            return false;
        }else{
            cpasswords.style.borderColor = "red";
            return false;
        }
    }else{
        if(cpasswords.value.trim() != passwords.value.trim()){
            passwords.style.borderColor = "red";
            cpasswords.style.borderColor = "red";
            return false;
        }
    }
}

const removerError = (cliked_id) =>{
    document.getElementById(cliked_id).style.borderColor = "gainsboro";
}

const ValidateLogin = () =>{
    let username = document.getElementById("useremails");
    let password = document.getElementById("passwords");

    if(username.value.trim() === "" || password.value.trim() === ""){
        if(username.value.trim() === ""){
             username.style.borderColor = 'red';
             return false;
        }else{
            password.style.borderColor = 'red';
            return false;
        }
    }
}