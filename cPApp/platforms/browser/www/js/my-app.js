// Initialize your app
var myApp = new Framework7();

// Export selectors engine
var $$ = Dom7;

//Detect type
var isAndroid = Framework7.prototype.device.android === true;
var isIos = Framework7.prototype.device.ios === true;

// Add view
var mainView = myApp.addView('.view-main', {
    // Because we use fixed-through navbar we can enable dynamic navbar
    dynamicNavbar: true
});

/*---------------------
index page
--------------------- */
myApp.onPageInit('index', function (page) {
    myApp.swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    });
    myApp.swiper('.swiper-container2', {
        autoplay: 2500,
        autoplayDisableOnInteraction: false
    });
    myApp.swiper('.best-sellers', {
        //autoplay: 2500,
        autoplayDisableOnInteraction: false,
        nextButton: '.best-next',
        prevButton: '.best-prev',
    });

});


(function ($) {
    "use strict";

    $(function () {
        //Login action
        $("#do_action_login").on('click', function () {

        });

        //Login action
        $("#do_action_register").on('click', function () {
            alert('register');
        });
    });


})(jQuery);    

  