let phototbn = document.querySelector('#userphotobtn');
let file = document.querySelector('#file');
let fileName = document.querySelector('#filename');
let img = document.querySelector('#pimg');

phototbn.addEventListener("click", function(){
    file.click();
});

file.addEventListener("change", function(e){
    fileName.textContent = e.target.files[0].name
    // // console.log()
});


////
let form = document.querySelector("#submissionForm");
let formButton = document.querySelector("#submissionFormButton");
let pass = document.querySelector("#password");
let rePass = document.querySelector("#repassword");

formButton.addEventListener("click", function(){
    if(pass.value != rePass.value ){
        alert("Password and retype password does not match");
    }else{
        form.submit();
    }
});