// Initialize your app
var myApp = new Framework7();

// Export selectors engine
var $$ = Dom7;

//Detect type
var isAndroid = Framework7.prototype.device.android === true;
var isIos = Framework7.prototype.device.ios === true;

// Add view
myApp.addView('.view-main', {
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

    var apiEndPoint = "";

    $(function () {
        
        //Login action
        $("#do_action_login").on('click', function () {
            var loginPopup = $('.login-screen');

            var loginMsg = loginPopup.find('.custom_msg');
            var loginLoader = loginPopup.find('.custom_loader');

            var loginEndpoint = apiEndPoint + "";

            var apiEmail = loginMsg.find('.email_input').val();
            var apiPassword = loginMsg.find('.pw_input').val();

            loginLoader.slideDown('fast');
            loginMsg.html('Logging you in...');
            loginMsg.slideDown('fast');

            //Add API call
            $.post(loginEndpoint, {
                email: apiEmail,
                password: apiPassword
            }).done(function (ret1) {
                if (ret1) {
                    var retData = ret1['ret_data'];
                }
            }).fail(function () {
            });
        });

        //Register action
        $("#do_action_register").on('click', function () {
            var registerPopup = $('.popup-register');

            var registerMsg = registerPopup.find('.custom_msg');
            var registerLoader = registerPopup.find('.custom_loader');

            var registerEndpoint = apiEndPoint + "";

            var apiEmail = registerPopup.find('.email_input').val();
            var apiPassword = registerPopup.find('.pw_input').val();

            registerLoader.slideDown('fast');
            registerMsg.html('Creating your new account...');
            registerMsg.slideDown('fast');

            //Add API call
            $.post(registerEndpoint, {
                email: apiEmail,
                password: apiPassword
            }).done(function (ret1) {
                if (ret1) {
                    var retData = ret1['ret_data'];
                }
            }).fail(function () {
            });
        });
    });


})(jQuery);    

  