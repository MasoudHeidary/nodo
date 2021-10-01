(function ($) {

    "use strict";

    $(".toggle-password").click(function () {

        $(this).toggleClass("fa-eye fa-eye-slash");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
            input.attr("type", "text");
        } else {
            input.attr("type", "password");
        }
    });

})(jQuery);

const e2p = s => s.replace(/\d/g, d => '۰۱۲۳۴۵۶۷۸۹'[d])

function phone_number_validate() {
    let phone_number = document.forms['login']['PhoneNumber'].value
    if (phone_number.length !== 11) {
        let err = document.querySelector('#PhoneNumberError')
        err.innerHTML = "شماره موبایل صحیح نمی باشد"
        return false
    }
}

function phone_number_to_persian() {
    let phone_number_field = document.forms['login']['PhoneNumber']
    phone_number_field.value = e2p(phone_number_field.value)
}

function password_number_to_persian() {
    let password_field = document.forms['login']['Password']
    password_field.value = e2p(password_field.value)
}


const ONE_TIME_PASSWORD_TIME = 10 * 60;
let TimeSpendSecond = 0
let OneTimePasswordTimer = setInterval(update_one_time_password_timer, 1000)

function update_one_time_password_timer() {
    TimeSpendSecond += 1
    let remain_time_second = ONE_TIME_PASSWORD_TIME - TimeSpendSecond;
    if (remain_time_second === 0)
        clearInterval(OneTimePasswordTimer)

    timer_digit_to_persian(`${Math.floor(remain_time_second / 60)}:${Math.floor(remain_time_second % 60)}`)
}

function timer_digit_to_persian(time) {
    let timer = document.querySelector('#OneTimePasswordTimer')
    if (!timer)
        return
    timer.innerHTML = time
}
