
	    var ajxpage = function(ajx_call,div,effect,top_padding){
			
/*		hour_glass 		= typeof(hour_glass) != 'undefined' ? 1 : 0;*/
		top_padding 	= typeof(top_padding) != 'undefined' ? top_padding : 0;
	
		var div = '#' + div;
	
 		/*if (hour_glass){*/
  			jQuery(div).html('<div style="text-align: center;'+top_padding+'"><img src="http://www.myfavoritepeople.com/images/ajax-loader.gif" style="float:left;" align="middle" border="0" /></div>');
 		/*}*/
		
		jQuery.ajax({ 										 
					   type: "POST", 
					   url: ajx_call+'&rand=' + Math.floor(Math.random()*11),
					   cache: false,
					   success: function(data){ 
							jQuery(div).css('display','none');
							if (effect == 'fade')
							{
								jQuery(div).html(data).fadeIn('slow');
							 
							}
							else if (effect == 'slide')
							{
								jQuery(div).html(data).slideDown('slow');
							}
							else if (effect == 'show')
							{
								jQuery(div).html(data).show('slow');
							}
							else if (effect == 'none')
							{
								jQuery(div).html(data);
								jQuery(div).css('display','block');
							}else if (effect == 'slideup')
							{
								jQuery(div).html(data).slideToggle('slow');
							}else
							{
								jQuery(div).html(data);
								jQuery(div).css('display','');
							}
						
 				   } ,
				   error: function (){ 		
					 //alert("Sorry!\nYour request was submitted, but a response has not yet been received. You can wait another few moments to see if the server responds, or reload the page");
				   }
				   
		 });

				
	} ;