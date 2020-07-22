
$(document).ready(function(){    
  console.log("hola");

  $('#btn').on('click', function(){
    

    $link = $('#txtwebinput').val();
    console.log($link);
    
    // coloca loader en el boton
    $('#wait').addClass('fa-spinner')

    // Ajax enviando el link a la ruta y se recibe el html
    $.ajax({
      url: 'cotizar/',
      type: 'GET',
      data: {
      link: $link,
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function(response){
        $('#result').html(response);

        // remueve loader en el boton
        $('#wait').removeClass('fa-spinner')


      },
      error: function(XMLHttpRequest, textStatus, errorThrown) { 
        $('#wait').removeClass('fa-spinner')

        // remueve loader en el boton
        $('#result').html("Error: " + errorThrown);
      }    

    });

  });

});
