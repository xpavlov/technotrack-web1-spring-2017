/**
 * Created by osboxes on 17/04/17.
 */

        console.log('blaaaaa');

$(document).ready(
    function () {

        function csrfSafeMethod(method) {
            // these HTTP methods do not require CSRF protection
            return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", $('meta[name=csrf]').attr("content"));
                }
            }
        });





        $('.like').each(function () {
            counter = $(this);
            console.log(counter.data('url'));
            setInterval(function () {

                counter.load(counter.data('url'))

            }, 5000);
        });


        $(document).on('click', '.ajaxlike', function () {
            var data = $(this).data();
            var btn = $(this)
            console.log(data);
            var likespan = $('#likes-' + data.postid);
            $.post({url: data['url']}).done(function (data, status, response) {
                    console.log(data);
                    if(data.liked) {

                        btn.html('Unlike');
                    }
                    else
                    {
                        btn.html('Like');
                    }
                    likespan.html(data.count);
                }
            );
            return false;
        });

    }
);

