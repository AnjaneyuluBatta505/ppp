(function($) {
            $(document).ready(function() {
		    CKEDITOR.disableAutoInline = true;

			$("textarea").each(function(index,val){
				CKEDITOR.replace( $(val).attr('id'),
					{extraPlugins: 'mathjax'}
				);
			});
			$('.add-row').on('click',function(){
			    $("textarea").each(function(index,val){
				CKEDITOR.replace( $(val).attr('id'),
					{extraPlugins: 'mathjax'}
				);
			});
			});
	   })	
        })(django.jQuery);
