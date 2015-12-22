(function($) {
            $(document).ready(function() {
		    CKEDITOR.disableAutoInline = true;

			$("textarea").each(function(index,val){
				CKEDITOR.replace( $(val).attr('id'),
					{extraPlugins: 'mathjax'}
				);
			});
			$('.add-row').on('click',function(){
			    $text_area = $(this).closest('textarea');
			    alert($text_area.attr('id'))
				CKEDITOR.replace( $text_area.attr('id'),
					{extraPlugins: 'mathjax'}
				);
			});
	   })	
        })(django.jQuery);
