$(document).ready(function() {
       $('.phone_us').mask('(000) 000-0000');
       $("#test").click(function(event){
            $.ajax({
                 type:"POST",
                 url:"/delete_personel/",
                 data: {
                        'pk':1 // from form
                        },
                 success: function(){
                     alert('Deneme')
                 }
            });
            return false; //<---- move it here
       });

});