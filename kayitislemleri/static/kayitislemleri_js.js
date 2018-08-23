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

});
