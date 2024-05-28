// jquery script for home page
    
    $(document).ready(function() {
        $('#hideButton').click(function() {
        hideDiv();
        });
    });

    function hideDiv() {
        $('.hide').hide();
    }