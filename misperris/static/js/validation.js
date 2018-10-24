function validate()
{


    console.log("validando...")

    var txtName = document.getElementById("txtName")
    var nameValidator = document.getElementById("nameValidator")

    if(txtName.value.trim().split(' ').length < 4)
    {
        nameValidator.innerHTML = "Este campo debiese tener al menos 4 palabras";
    }
     else
    {
        nameValidator.innerHTML = " ";
    }
}


function telValidator(event)
{
    var telValidator = document.getElementById("telValidator");



    if(event.charCode >= 48 && event.charCode <= 57)
    {
        return true;
    }
    else {
      return false;

    }

}

function telValidator(){

  var txtTel = document.getElementById("txtTel");

  if(txtTel.value.trim().length < 9)
  {
    telValidator.innerHTML = "Debe ingresar un número con un largo mínimo de 9";
  }
  else
  {
    telValidator.innerHTML = "";
  }
}
