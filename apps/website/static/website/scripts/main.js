$(function () {

    var holder = $('#id_files').get(0);

    $('#id_files').on('change', function () {
        console.log(holder.files.length);
        if (holder.files.length > 0) {
            //$(this).parent().parent().find('.drop-area .drop-text').html(holder.files[0].name);

            if (holder.files[0].size > 5000000) {
                $('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Plik jest zbyt duży ( > 5MB )</li></ul>');
            } else {
                $('.errorlist').remove();
            }

            if(holder.files.length > 5){
                $(this).parent().parent().find('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Maksymalna ilość plików to 5</li></ul>');
            }else{
                $(this).parent().parent().find('.errorlist').remove();
            }

            $(this).parent().parent().find('.drop-area .drop-text').html('');
            var elem_holder = $(this).parent().parent().find('.drop-area .drop-text');

            $(holder.files).each(function(k,v){

                if (v.size > 5000000) {
                    $(this).parent().parent().find('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Plik jest zbyt duży ( > 5MB )</li></ul>');
                }

                elem_holder.append("<div>" + v.name + "</div>");
            });

        } else {
           $(this).parent().parent().find('.drop-area .drop-text').html('<h3>Kliknij lub upuść plik ze zdjęciem tutaj</h3>');
        }
    });

    holder.ondragover = function () {
        $(this).parent().parent().find('.drop-area').addClass('hover');
        return false;
    };

    holder.ondragend = function () {
        $(this).parent().parent().find('.drop-area').removeClass('hover');
        return false;
    };

    holder.ondrop = function () {
        $(this).parent().parent().find('.drop-area').removeClass('hover');
    };


    var holder_single = $('#id_allow_scan').get(0);

    $('#id_allow_scan').on('change', function () {
        if (holder_single.files.length > 0) {
            //$(this).parent().parent().find('.drop-area .drop-text').html(holder.files[0].name);

            if (holder_single.files[0].size > 5000000) {
                $(this).parent().parent().find('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Plik jest zbyt duży ( > 5MB )</li></ul>');
            } else {
                $(this).parent().parent().find('.errorlist').remove();
            }

            if(holder_single.files.length > 5){
                $(this).parent().parent().find('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Maksymalna ilość plików to 5</li></ul>');
            }else{
                $(this).parent().parent().find('.errorlist').remove();
            }

            $(this).parent().parent().find('.drop-area .drop-text').html('');
            var elem_holder = $(this).parent().parent().find('.drop-area .drop-text');

            $(holder_single.files).each(function(k,v){

                if (v.size > 5000000) {
                    $(this).parent().parent().find('.files-error').html('<ul class="errorlist animated infinite pulse"><li><span class="glyphicon glyphicon-ban-circle"></span>&nbsp;&nbsp;Plik jest zbyt duży ( > 5MB )</li></ul>');
                }

                elem_holder.append("<div>" + v.name + "</div>");
            });

        } else {
            $(this).parent().parent().find('.drop-area .drop-text').html('<h3>Kliknij lub upuść plik ze zdjęciem tutaj</h3>');
        }
    });

    holder_single.ondragover = function () {
        $(this).parent().parent().find('.drop-area').addClass('hover');
        return false;
    };

    holder_single.ondragend = function () {
        $(this).parent().parent().find('.drop-area').removeClass('hover');
        return false;
    };

    holder_single.ondrop = function () {
        $(this).parent().parent().find('.drop-area').removeClass('hover');
    };


    $('textarea.auto-expand').each(function () {
      this.setAttribute('style', 'height:' + (this.scrollHeight) + 'px;overflow-y:hidden;');
    }).on('input', function () {
        this.style.height = (this.scrollHeight) + 'px';
    });

    function form_is_valid(file_holder) {

        var is_valid = true;

        $(file_holder.files).each(function(k,v){
            if (v.size > 5000000) {
                is_valid = false;
            }
        });

        if(file_holder.files.length > 5){
            is_valid = false;
        }

        if($("input[type=checkbox][name='category']:checked").length == 0){
            is_valid = false;
            alert("Prosimy o zaznaczenie przynajmniej jednek kategorii");
        }



        return is_valid;
    }

    $('form').submit(function(e){
        if(!form_is_valid(holder)){
            e.preventDefault();
        }
    });

    function autoresize() {
      //this.style.height = 'auto';
      this.style.height = this.scrollHeight+'px';
    }

});