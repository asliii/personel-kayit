$(document).ready(function() {
       $('.phone_us').mask('(000) 000-0000');
        $(".delete_button").click(function() {
        var id = $(this).attr('id');
            $.ajax({
            type:'get',
            url: '/personel/delete/'+id,
            contentType: 'application/json',
            success: function () {
                  swal("Veri Başarıyla Silindi.","",'success')
                        .then(() => {
                           location.reload();
                   });
            }
        });
       });
       $( "#positionSelecte" ).change(function() {
           var position;
           $( "select option:selected" ).each(function() {
               position =$( this ).val();
                $.ajax({
                   type:'get',
                   url: '/personel/filter/'+position,
                   contentType: 'application/json',
                });
           });

       });

      // $( "#positionSelecte" ).change(function() {
       //     var position;
         //   $( "select option:selected" ).each(function() {
           //     position = $( this ).text();
             //   $("td").each(function(){
               //     if($(this).text()!=position)
                 //       $(this).parent().addClass('hide')
                  //  else
                    //    $(this).parent().removeClass('hide')
              //  })
           // });

     //  });


});
