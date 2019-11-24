$(document).ready(function () {
            $("#sidebar").mCustomScrollbar({
                theme: "minimal"
            });

            $('#sidebarCollapse').on('click', function () {
                $('#sidebar, #content').toggleClass('active');
                $('.collapse.in').toggleClass('in');
                $('a[aria-expanded=true]').attr('aria-expanded', 'false');
            });
        });


(document).ready(function () {
//$('#dtBasicExample').DataTable();
$('#dtBasicExample').DataTable({
columnDefs: [{
orderable: false,
targets: 3
}]
});
$('.dataTables_length').addClass('bs-select');
});
$(document).ready(function(){
  var test1=$(".dropdown-toggle").css("width");
  var test2=$(".dropdown-menu").css("width",test1);

  $(".dropdown-toggle").click(function()
  {

    test1=$(".dropdown-toggle").css("width");
    test2=$(".dropdown-menu").css("width",test1);
  })

  })