$(document).ready(function() {
    $(window).on('scroll', function() {
        const scrollTop = $(document).scrollTop();
        const screenHeight = $(document).height();

        if (scrollTop < 40) {
            $('#indexHeader').removeClass('-translate-y-0 opacity-0').addClass('translate-y-0 opacity-100');
        } else if (scrollTop < 250) {
            $('#indexHeader').removeClass('translate-y-0 opacity-100').addClass('-translate-y-0 opacity-0');
        } else if (scrollTop > 250) {
            $('#indexHeader').removeClass('-translate-y-0 opacity-0').addClass('translate-y-0 opacity-100');
        }
    });
});