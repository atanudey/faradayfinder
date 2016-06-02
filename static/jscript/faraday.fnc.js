// JavaScript Document

/**
 * Code : 15/6/2012
 * @ mahesh.php.developer@gmail.com
 */

function loginfo_check(){
	
	var userEmail = trim(jQuery('#userEmail').val());
	var userPass  = trim(jQuery('#userPass').val());
	var error     = 0;
	
	if(!userEmail || !email_validate(userEmail))
	{ error++;
	  jQuery('#userEmail_error').html('Blank/wrong email-id');
	}
	else
	{ 
	  jQuery('#userEmail_error').html('');
	}
	
	if(!userPass )
	{ error++;
	  jQuery('#userPass_error').html('Blank/wrong password');
	}
	else
	{ 
	  jQuery('#userPass_error').html('');
	}
	
	if(error)
	{
		return false;
	}
	else
	{
	 document.loginform.submit();	
	 return true;
	}
}


function change_class(id)
{
	for(var i=1;i<=13;i++)
	{
		if(id == 'Newtaborg'+i)
		{
			jQuery('#Newtaborg'+i).attr('class','Selected'); 
			jQuery('#Newtaborgnum'+i).show();
		}
		else
		{
			jQuery('#Newtaborg'+i).attr('class','');	
			jQuery('#Newtaborgnum'+i).hide();
		}
	}
}


function change_tab_class(id)
{
	for(var i=1;i<=13;i++)
	{
		if(id == 'UserTab'+i)
		{
		 jQuery('#UserTab'+i).attr('class','Selected');
		 jQuery('#Newtabusrnum'+i).show(); 	
		}
		else
		{
		jQuery('#UserTab'+i).attr('class','');		
		jQuery('#Newtabusrnum'+i).hide();			
		}
	}
}


function add_org_related()                                       
{
	jQuery('#Opendivblock').slideToggle('slow');
}

function add_user_share()                                       
{
	jQuery('#Opendivblock').slideToggle('slow');
}

function submit_suggestion(id,org_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_suggestion.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Suggestion has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_suggestion.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your suggestion text !');}
 	return false;
}


function submit_announcement(id,org_id,show_per)
{
	var text = trim(jQuery('#text').val());
 
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_announcement.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
																									 
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Announcement has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_announcement.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your announcement text !');}
 	return false;
}

function submit_problem(id,org_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_problem.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Problem has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_problem.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');		
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your problem text !');}
 	return false;
}


function submit_thankyou(id,org_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_thankyou.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Thankyou has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_thankyou.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your thankyou text !');}
 	return false;
}

function submit_fyi(id,org_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_fyi.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>FYI text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_fyi.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your fyi text !');}
 	return false;
}


function submit_share(id,user_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_share.php',{ detail: text, user_id: user_id }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Your message has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_user_share.php?page_no=1&user_id='+user_id+'&show_per='+show_per,'user_common_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your message!');}
 	return false;
}


function submit_faq(id,org_id,show_per)
{
	var text   = trim(jQuery('#'+id).val());
	var answer = trim(jQuery('#answer').val());		
	answer     = (answer=='undefined')?'':answer;
	
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_faq.php',{ detail: text, oe_id: org_id, answer:answer, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Question has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_faq.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your question !');}
 	return false;
}


function submit_grading(grading,org_id)
{
	/*var grading = trim(jQuery('#amount').val());*/
	if(grading)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_grading.php',{ grade: grading, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Your grading has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_grading.php?oe_id='+org_id,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please select your grading !');}
 	return false;
}



function submit_file(org_id,show_per)
{
	var title = trim(jQuery('#title').val());
	var desc  = trim(jQuery('#desc').val());
	var file  = trim(jQuery('#file').val());
	
	if(title && desc && file)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_file.php',{ title: title,desc: desc, file: file, oe_id: org_id, type:1 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>File has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_file.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
			});
		  });
	    });
	}
	else
	{ alert ('Please enter all fields !');}
 	return false;
}


// ================= Event Functions Starts from here ============ //

function submit_event_suggestion(id,event_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_suggestion.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Suggestion has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_suggestion.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your suggestion text !');}
 	return false;
}


function submit_event_announcement(id,event_id,show_per)
{
	var text = trim(jQuery('#text').val());
 
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_announcement.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
																									 
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Announcement has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_announcement.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your announcement text !');}
 	return false;
}

function submit_event_problem(id,event_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_problem.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
																								  
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Problem has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_problem.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your problem text !');}
 	return false;
}


function submit_event_thankyou(id,event_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_thankyou.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Thankyou has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_thankyou.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your thankyou text !');}
 	return false;
}

function submit_event_fyi(id,event_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_fyi.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>FYI text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_fyi.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your fyi text !');}
 	return false;
}

function submit_event_faq(id,event_id,show_per)
{
	var text = trim(jQuery('#'+id).val());
	var answer = trim(jQuery('#answer').val());		
	answer     = (answer=='undefined')?'':answer;	
	if(text)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_faq.php',{ detail: text, oe_id: event_id, answer:answer, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Question has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_faq.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter your question !');}
 	return false;
}


function submit_event_grading(grading,event_id)
{
	/*var grading = trim(jQuery('#amount').val());*/
	if(grading)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_grading.php',{ grade: grading, oe_id: event_id, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>Your grading has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_grading.php?oe_id='+event_id,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please select your grading !');}
 	return false;
}



function submit_event_file(event_id,show_per)
{
	var title = trim(jQuery('#title').val());
	var desc  = trim(jQuery('#desc').val());
	var file  = trim(jQuery('#file').val());
	
	if(title && desc && file)
	{
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_file.php',{ title: title,desc: desc, file: file, oe_id: event_id, type:2 }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>File has been submitted successfully</strong></span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_file.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
	}
	else
	{ alert ('Please enter all fields !');}
 	return false;
}


 function validateOrgCategory(org_id)
 {
	var title     = trim(jQuery('#title').val());
	if(org_id && title)
	{
		jQuery.post('ajax/ajx_org_bookmark_category.php',{ title: title,org_id: org_id }, function() {	
		jQuery('#add_new_category').fadeOut('slow',function(){
			  jQuery('#add_new_category').html('<span class=\"Redcolor\">Category has been added successfully</span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_org_bookmark_category.php?org_id='+org_id,'organization_bookmark','fade','padding-left:20px; padding-top:20px;');				
			});
		  });
	    });
		
	}
	else
	{	
		alert('Please fill category title.');
	}
 }



 function validateEventCategory(event_id)
 {
	var title     = trim(jQuery('#title').val());
	if(event_id && title)
	{
		jQuery.post('ajax/ajx_event_bookmark_category.php',{ title: title,event_id: event_id }, function() {	
		jQuery('#add_new_category').fadeOut('slow',function(){
			  jQuery('#add_new_category').html('<span class=\"Redcolor\">Category has been added successfully</span>').fadeIn('slow',function(){				
			  ajxpage('ajax/ajx_event_bookmark_category.php?event_id='+event_id,'event_bookmark','fade','padding-left:20px;padding-top:20px;');				
			});
		  });
	    });
		
	}
	else
		alert('Please fill category title.');
 }



 


 function popup_chat_window(room_id) {
	  jQuery.ajax({
	  type : 'POST',
	  url  : AJAX_PATH+"enter_chat_room.php?cat=1",
	  cache: false,	
	  data : "&room_id="+room_id+"&rand="+ Date(),
	  success : function(res){ 
		if(res==1)
		{
			var leftPos = (screen.availWidth-700) / 2;
			var topPos 	= (screen.availHeight-370) / 2;
			Press1Win 	= window.open(WEBSITE_URL+'/blab5ent','','width=700,height=370,scrollbars=yes,resizable=no,titlebar=0,top=' + topPos + ',left=' + leftPos);
		}			
	  },
	  error: function(){ 		
		 alert("Sorry! AJAX call is not responding");
	  }	  
	 });
 }


 function popup_private_chat(uid) {
	 
	  jQuery.ajax({
	  type : 'POST',
	  url  : AJAX_PATH+"enter_private_chat.php?uid="+uid,
	  cache: false,	
	  data : "&rand="+ Date(),
	  success : function(res){
		if(res){
		var leftPos = (screen.availWidth-700) / 2;
		var topPos 	= (screen.availHeight-370) / 2;
		Press1Win 	= window.open(WEBSITE_URL+'/blab5ent/blab_p.php?u='+res,'','width=700,height=370,scrollbars=yes,resizable=no,titlebar=0,top=' + topPos + ',left=' + leftPos);
		}
	  },
	  error: function(){
		 alert("Sorry! AJAX call is not responding");
	  }	  
	 });
	  
 }
 

 function popup_ticket_window(code) {
	
	var leftPos = (screen.availWidth-700) / 2;
	var topPos 	= (screen.availHeight-370) / 2;
	Press1Win 	= window.open(WEBSITE_URL+'/ticket.php?code='+code,'','width=700,height=370,scrollbars=yes,resizable=no,titlebar=0,top=' + topPos + ',left=' + leftPos);
 }


   jQuery(function() {
		jQuery( "#dialog:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#dialog" ).dialog({
			autoOpen: false,height: 200,width: 350,	modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" }
		});	
		
		jQuery( "#profile_image:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#profile_image" ).dialog({
			autoOpen: false,height: 200,width: 350,	modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" }
		});			
		
		jQuery( "#edialog:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#edialog" ).dialog({
			autoOpen: false,height: 200,width: 350,	modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" }
		});
		
		jQuery( "#addbookmark:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#addbookmark" ).dialog({
			autoOpen: false,height: 330,width: 360,	modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" }
		});	
		
		jQuery( "#addslideshow:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#addslideshow" ).dialog({
			autoOpen: false,height: 330,width: 400,	modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" },
			close: function(event, ui){
				 window.setTimeout('location.reload()', 500);
    		}
		});	
		
		jQuery( "#vclass:ui-dialog" ).dialog( "destroy" );		 
		jQuery( "#vclass" ).dialog({
			autoOpen: false,height: 375,width: 600,modal: true,show: 'slide',stack: false,overlay:{ opacity: 0.7,background: "red" }
		});	
		
	});
	
	
	function check_lab_protection(main_cat,name)
	{	// function will be called only if the organization is password protected
		// if session is not started		 
		jQuery('#lab_name').html('<em>&#147;&nbsp;'+name+'&nbsp;&#148;</em>');		
		  jQuery.ajax({
		  type : 'POST',
		  url  : AJAX_PATH+"ajx_check_lab_password.php?main_cat="+main_cat,
		  cache: false,	
		  data : "&exist=1&rand="+ Date(),
		  success : function(res){ 
				if(res != 0) { window.location.href="view-lab/"+res; } 
				else{ 
					jQuery('#protection_id').val(main_cat);
					jQuery("#dialog").dialog( "open" ); 
				}
		  },
		  error: function(){ 		
			 alert("Sorry! AJAX call is not responding");
		  }	  	
		 });
	}


	function check_lab_password()
	{
		var main_cat = jQuery('#protection_id').val();
		var password = jQuery('#lab_password').val();
        jQuery('#processing').html('<img src="images/dialogue-loder.gif" />');		

		  jQuery.ajax({
		  type : 'POST',
		  url  : AJAX_PATH+"ajx_check_lab_password.php?main_cat="+main_cat,
		  cache: false,	
		  data : "&check=1&password="+password+"&rand="+ Date(),
		  success : function(res){ 
				if(res != 0) { window.location.href="view-lab/"+res; } 
				else{ 
				jQuery('#processing').html('The password you have entered is wrong !');	
				}
		  },
		  error: function(){ 		
			 alert("Sorry! AJAX call is not responding");
		  }	  	
		 });		
	}

	function check_event_protection(main_cat,name)
	{	// function will be called only if the event is password protected
		// if session is not started
		  jQuery('#event_name').html('<em>&#147;&nbsp;'+name+'&nbsp;&#148;</em>');		
		  jQuery.ajax({
		  type : 'POST',
		  url  : AJAX_PATH+"ajx_check_event_password.php?main_cat="+main_cat,
		  cache: false,	
		  data : "&exist=1&rand="+ Date(),
		  success : function(res){ 
				if(res != 0) { window.location.href="view-event/"+res; } 
				else{ 
					jQuery('#protection_id2').val(main_cat);
					jQuery("#edialog").dialog( "open" ); 
				}
		  },
		  error: function(){ 		
			 alert("Sorry! AJAX call is not responding");
		  }	  	
		 });
	}	
	
	function check_event_password()
	{		
		var main_cat = jQuery('#protection_id2').val();
		var password = jQuery('#event_password').val();
        jQuery('#processing2').html('<img src="images/dialogue-loder.gif" />');		
		  jQuery.ajax({
		  type : 'POST',
		  url  : AJAX_PATH+"ajx_check_event_password.php?main_cat="+main_cat,
		  cache: false,	
		  data : "&check=1&password="+password+"&rand="+ Date(),
		  success : function(res){ 
 
				if(res != 0) { window.location.href="view-event/"+res; } 
				else{ 
				jQuery('#processing2').html('The password you have entered is wrong !');	
				}
		  },
		  error: function(){ 		
			 alert("Sorry! AJAX call is not responding");
		  }	  	
		 });		
	}	
	
	
	function submit_bookmark()
	{
		var category       = trim(jQuery('#category').val());
		var bookmark_title = trim(jQuery('#bookmark_title').val());
		var bookmark_url   = trim(jQuery('#bookmark_url').val());
		
		var oe_id          = trim(jQuery('#oe_id').val());
		var type           = trim(jQuery('#type').val());
		var rurl           = trim(jQuery('#rurl').val());
		
		if(!category || !bookmark_title || !bookmark_url || !(type ==1 || type ==2) || !oe_id)
		{ 
			jQuery('#processing_bookmark').html('Please select/fill all the fields correctly !');			
		}else{ 
			jQuery('#processing_bookmark').html('<img src="images/dialogue-loder.gif" />');
			jQuery.ajax({
			type : 'POST',
			url  : AJAX_PATH+"ajx_add_bookmark.php?exist=1",
			cache: false,	
			data : "&oe_id="+oe_id+"&type="+type+"&category="+category+"&bookmark_title="+bookmark_title+"&bookmark_url="+bookmark_url+"&rand="+ Date(),
			success : function(res){ 
				if(res == 1) { 
				    // view-organization and view-event according to the type
					if(type==1)
					{ window.location.href="view-organization/"+rurl;  }
					else if(type==2)
					{ window.location.href="view-event/"+rurl;         }
				} 
				else{ 
				jQuery('#processing').html('Error during bookmark insertion!');	
				}
			},
			error: function(){ 		
			 alert("Sorry! AJAX call is not responding");
			}
			});
		}
	}
	
	
	
	 function popup_ticket_window(code) {
		
		var leftPos = (screen.availWidth-700) / 2;
		var topPos 	= (screen.availHeight-370) / 2;
		Press1Win 	= window.open(WEBSITE_URL+'/ticket.php?orderion='+code,'','width=700,height=370,scrollbars=yes,resizable=no,titlebar=0,top=' + topPos + ',left=' + leftPos);
	 }
 
	
	function fill_shipping_address()
	{
		var checked = jQuery("#same_as_billing").attr('checked');
		
		if(checked)
		{	 
			jQuery('#ship_street').val(jQuery('#bill_street').val());
			jQuery('#ship_city').val(jQuery('#bill_city').val());
			jQuery('#ship_state').val(jQuery('#bill_state').val());
			jQuery('#ship_country').val(jQuery('#bill_country').val());
			jQuery('#ship_zip').val(jQuery('#bill_zip').val());			
		}
		else
		{  
			jQuery('#ship_street').val('');
			jQuery('#ship_city').val('');
			jQuery('#ship_state').val('');
			jQuery('#ship_country').val('');
			jQuery('#ship_zip').val('');
		}
	}
	
	/*
	* @ for deleting the problem from event/organization
	*/
	
	function delete_org_problem(problem_id,org_id,show_per)
	{
		var problem_id = trim(problem_id);
		if(problem_id)
		{
			if(confirm('Are you sure,want to delete this problem?')){
			jQuery.post('ajax/delete_problem.php',{ problem_id: problem_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Problem has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_problem.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}	
	
	
	function delete_event_problem(problem_id,event_id,show_per)
	{
		var problem_id = trim(problem_id);
		if(problem_id)
		{
			if(confirm('Are you sure,want to delete this problem?')){
			jQuery.post('ajax/delete_problem.php',{ problem_id: problem_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Problem has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_problem.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}	
	
	
	
	/*
	* @ for deleting the FYI -for your information- from event/organization
	*/
	
	function delete_org_fyi(fyi_id,org_id,show_per)
	{
		var fyi_id = trim(fyi_id);
		if(fyi_id)
		{
			if(confirm('Are you sure,want to delete this FYI?')){
			jQuery.post('ajax/delete_fyi.php',{ fyi_id: fyi_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>FYI has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_fyi.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}	
	
	
	function delete_event_fyi(fyi_id,event_id,show_per)
	{
		var fyi_id = trim(fyi_id);
		if(fyi_id)
		{
			if(confirm('Are you sure,want to delete this FYI?')){
			jQuery.post('ajax/delete_fyi.php',{ fyi_id: fyi_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>FYI has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_fyi.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}
	
	
	
	/*
	* @ for deleting the Thank you - text - from event/organization
	*/
	
	function delete_org_thankyou(thankyou_id,org_id,show_per)
	{	var thankyou_id = trim(thankyou_id);
		if(thankyou_id)
		{
			if(confirm('Are you sure,want to delete this Thankyou?')){
			jQuery.post('ajax/delete_thankyou.php',{ thankyou_id: thankyou_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Thankyou has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_thankyou.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}
	
	function delete_event_thankyou(thankyou_id,event_id,show_per)
	{	var thankyou_id = trim(thankyou_id);
		if(thankyou_id)
		{
			if(confirm('Are you sure,want to delete this Thankyou?')){
			jQuery.post('ajax/delete_thankyou.php',{ thankyou_id: thankyou_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Thankyou has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_thankyou.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}
	
	
	
	/*
	* @ for deleting the Thank you - text - from event/organization
	*/
	
	function delete_org_announcement(announcement_id,org_id,show_per)
	{	var announcement_id = trim(announcement_id);
		if(announcement_id)
		{
			if(confirm('Are you sure,want to delete this Announcement?')){
			jQuery.post('ajax/delete_announcement.php',{ announcement_id: announcement_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Announcement has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_announcement.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');	
				});
			  });
			});
			}
		}
	}
	
	function delete_event_announcement(announcement_id,event_id,show_per)
	{	var announcement_id = trim(announcement_id);
		if(announcement_id)
		{
			if(confirm('Are you sure,want to delete this Announcement?')){
			jQuery.post('ajax/delete_announcement.php',{ announcement_id: announcement_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Announcement has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_announcement.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}
	
	
	/*
	* @ for deleting the Suggestion - text - from event/organization
	*/
	
	function delete_org_suggestion(suggestion_id,org_id,show_per)
	{	var suggestion_id = trim(suggestion_id);
		if(suggestion_id)
		{
			if(confirm('Are you sure,want to delete this Suggestion?')){
			jQuery.post('ajax/delete_suggestion.php',{ suggestion_id: suggestion_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Suggestion has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_suggestion.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}
	
	function delete_event_suggestion(suggestion_id,event_id,show_per)
	{	var suggestion_id = trim(suggestion_id);
		if(suggestion_id)
		{
			if(confirm('Are you sure,want to delete this Suggestion?')){
			jQuery.post('ajax/delete_suggestion.php',{ suggestion_id: suggestion_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Suggestion has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_suggestion.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}	
	
	
	
	/*
	* @ for deleting the Faq - text - from event/organization
	*/
	
	function delete_org_faq(faq_id,org_id,show_per)
	{	var faq_id = trim(faq_id);
		if(faq_id)
		{
			if(confirm('Are you sure,want to delete this Faq?')){
			jQuery.post('ajax/delete_faq.php',{ faq_id: faq_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Faq has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_faq.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}
	
	function delete_event_faq(faq_id,event_id,show_per)
	{	var faq_id = trim(faq_id);
		if(faq_id)
		{
			if(confirm('Are you sure,want to delete this Faq?')){
			jQuery.post('ajax/delete_faq.php',{ faq_id: faq_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>Faq has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_faq.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}
			


	function delete_event(event_id)
	{	var event_id = trim(event_id);
		if(event_id)
		{
			if(confirm("Do you really want delete this Event ? \nThis action will delete all the data related with this event & can not be reverted back !!")){
			jQuery.post('ajax/delete_my_prop.php?',{ id: event_id, type:'event' }, function() {	 			
				  ajxpage('ajax/ajx_events_created_by_me.php?','events_created','fade','');								 
			});
			}
		}
	}		
	
	function delete_lab(lab_id)
	{	var lab_id = trim(lab_id);
		if(lab_id)
		{			 
			if(confirm("Do you really want delete this Lab ? \nThis action will delete all the data related with this lab and related projects and events & can not be reverted back !!")){
			jQuery.post('ajax/delete_my_prop.php?',{ id: lab_id, type:'lab' }, function() {				 				
				  ajxpage('ajax/ajx_labs_created_by_me.php?','labs_created','fade','');								 
			});
			}
		}
	}	
		
	function delete_project(project_id)
	{	var project_id = trim(project_id);
		if(project_id)
		{			 
			if(confirm("Do you really want delete this Project ? \nThis action will delete all the data related with this project & can not be reverted back !!")){
			jQuery.post('ajax/delete_my_prop.php?',{ id: project_id, type:'project' }, function() {	 			
				  ajxpage('ajax/ajx_projects_created_by_me.php?','projects_created','fade','');								 
			});
			}
		}
	}		
		
		
	
	function delete_ss(oe_id,type,id)
	{	 
		if(oe_id && type && id)
		{
			if(confirm("Do you really want to delete this Slideshow Image!")){
				  jQuery.ajax({
				  type : 'POST',
				  url  : AJAX_PATH+"delete_ss_image.php?oe_id="+oe_id+"&id="+id,
				  cache: false,
				  data : "&rand="+ Date(),
				  success : function(res){
					ajxpage('ajax/ajx_ss_image.php?type='+type+'&oe_id='+oe_id,'current_ss','fade','');  			
				  },
				  error: function(){
					 alert("Sorry! AJAX call is not responding");
				  }
				 });				
			}
		}
	}
	
  function popup_org_chart(oe_id,type) {	
	var leftPos = (screen.availWidth-700) / 2;
	var topPos 	= (screen.availHeight-370) / 2;
	Press1Win 	= window.open(WEBSITE_URL+'org_chart.php?oe_id='+oe_id+'&type='+type,'','width=850,height=800,scrollbars=yes,resizable=no,titlebar=0,top=' + topPos + ',left=' + leftPos);
  }	
  
	/*
	@ Milestone related function (7-2-2012)
	*/
	function submit_milestone(id,org_id,show_per)
	{
		var date = trim(jQuery('#date').val());						
		var text = trim(jQuery('#'+id).val());
 
		if(text)
		{
			jQuery('#Opendivblock').slideUp('slow');
			jQuery.post('ajax/submit_milestone.php',{ detail: text,date: date, oe_id: org_id, type:1 }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>MILESTONE text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_milestone.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
		}
		else
		{ alert ('Please enter your milestone text !');}
		return false;
	}
	
	function submit_event_milestone(id,event_id,show_per)
	{
	    var date = trim(jQuery('#date').val());						
		var text = trim(jQuery('#'+id).val());
		if(text)
		{
			jQuery('#Opendivblock').slideUp('slow');
			jQuery.post('ajax/submit_milestone.php',{ detail: text,date:date, oe_id: event_id, type:2 }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>MILESTONE text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_milestone.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
		}
		else
		{ alert ('Please enter your milestone text !');}
		return false;
	}
	
	function delete_org_milestone(milestone_id,org_id,show_per)
	{
		var milestone_id = trim(milestone_id);
		if(milestone_id)
		{
			if(confirm('Are you sure,want to delete this MILESTONE?')){
			jQuery.post('ajax/delete_milestone.php',{ milestone_id: milestone_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>MILESTONE has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_milestone.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}
	
	function delete_event_milestone(milestone_id,event_id,show_per)
	{
		var milestone_id = trim(milestone_id);
		if(milestone_id)
		{
			if(confirm('Are you sure,want to delete this MILESTONE?')){
			jQuery.post('ajax/delete_milestone.php',{ milestone_id: milestone_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>MILESTONE has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_milestone.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}  
	
	
   /*
	@ Todo related function (7-2-2012)
	*/
	function submit_todo(id,org_id,show_per)
	{
		
		var text    = trim(jQuery('#'+id).val());
		if(text)
		{
			jQuery('#Opendivblock').slideUp('slow');
			jQuery.post('ajax/submit_todo.php',{ detail: text, oe_id: org_id, type:1 }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>TODO text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_todo.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
		}
		else
		{ alert ('Please enter your todo text !');}
		return false;
	}
	
	function submit_event_todo(id,event_id,show_per)
	{
		
		var text = trim(jQuery('#'+id).val());
		if(text)
		{
			jQuery('#Opendivblock').slideUp('slow');
			jQuery.post('ajax/submit_todo.php',{ detail: text, oe_id: event_id, type:2 }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>TODO text has been submitted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_todo.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
		}
		else
		{ alert ('Please enter your todo text !');}
		return false;
	}
	
	function delete_org_todo(todo_id,org_id,show_per)
	{
		var todo_id = trim(todo_id);
		if(todo_id)
		{
			if(confirm('Are you sure,want to delete this TODO?')){
			jQuery.post('ajax/delete_todo.php',{ todo_id: todo_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>TODO has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_org_todo.php?page_no=1&oe_id='+org_id+'&show_per='+show_per,'organization_block','fade','padding-left:20px; padding-top:20px;');
				});
			  });
			});
			}
		}
	}
	
	function delete_event_todo(todo_id,event_id,show_per)
	{
		var todo_id = trim(todo_id);
		if(todo_id)
		{
			if(confirm('Are you sure,want to delete this TODO?')){
			jQuery.post('ajax/delete_todo.php',{ todo_id: todo_id }, function() {	
			jQuery('#message').fadeOut('slow',function(){
				  jQuery('#message').html('<span class=\"Redcolor\"><strong>TODO has been deleted successfully</strong></span>').fadeIn('slow',function(){				
				  ajxpage('ajax/ajx_event_todo.php?page_no=1&oe_id='+event_id+'&show_per='+show_per,'event_block','fade','padding-left:20px;padding-top:20px;');				
				});
			  });
			});
			}
		}
	}  	
	
	// Faraday FInder functions starts from here 
	// Dated: 26/11/2012
	
	function toggleFgClass(active_id){
		var arr = new Array('first_1','second_2','third_3');
		for(i=0;i<arr.length;i++){
			if(active_id == arr[i])
			jQuery('#'+arr[i]).attr('class','active');
			else
			jQuery('#'+arr[i]).attr('class','');			
		}
	}
	
	function upload_pimage(){
		jQuery('#profile_image').dialog( 'open' );
	}
	
	
	function check_profile_pic(){

		jQuery("#loading")
		.ajaxStart(function(){
			jQuery(this).show();
		})
		.ajaxComplete(function(){
			jQuery(this).hide();
		});

		jQuery.ajaxFileUpload
		(
			{
				url:'ajax/ajx_image_upload.php',
				secureuri:false,
				fileElementId:'fileToUpload',
				dataType: 'json',
				data:{name:'logan', id:'id'},
				success: function (data, status)
				{
					if(typeof(data.error) != 'undefined'){
						if(data.error != ''){
							jQuery("#processing").html(data.error);
						}else{
							jQuery("#processing").html(data.msg);
							window.location.href="my-account/"; 
						}
					}
				},
				error: function (data, status, e){
					alert(e);
				}
			}
		)		
		return false;
	}
	
	function add_more_sketch(id){
		var current = parseInt(jQuery("#count_val").val());		
		jQuery("#"+id).append("<div class=\"from_action\" style=\"margin-right:60px;\" id=\"sk"+current+"\"><input name=\"sketch[]\" type=\"file\" \/>&nbsp;&nbsp;<a href=\"javascript:void(0);\" onclick=\"javascript:jQuery('#sk"+current+"').remove();\">[X] remove<\/a><\/div>");		
		jQuery("#count_val").val(current+1);
	}
	
	function add_more_file(id){
		var current = parseInt(jQuery("#count_val").val());		
		jQuery("#"+id).append("<div class=\"from_action\" style=\"margin-right:80px;\" id=\"sk"+current+"\"><input name=\"image[]\" type=\"file\" \/>&nbsp;&nbsp;<a href=\"javascript:void(0);\" onclick=\"javascript:jQuery('#sk"+current+"').remove();\">[X] remove<\/a><\/div>");		
		jQuery("#count_val").val(current+1);
	}	
	
	function del_sketch(file_id){
		var file_id = trim(file_id);
		if(file_id)
		{
			if(confirm('Are you sure,want to delete this file?')){
			jQuery.post('ajax/delete_sketch.php',{ file_id: file_id }, function(data) {	
			if(data == 1){
			jQuery('#psketch'+file_id).fadeOut('slow',function(){
				  jQuery('#psketch'+file_id).html('<span class=\"Redcolor\"><strong>File has been deleted successfully</strong></span>').fadeIn('slow',function(){
				  jQuery('#psketch'+file_id).remove();
				  });
			  });
			}
			});
			}
		}		
	}
	
	
function show_department(inst_id){
  jQuery.ajax({
    url  :'ajax/ajx_select_department.php',
    data :'inst_id='+inst_id+"&date="+ new Date(),
	type :'post',
	cache:false,
	success: function(data){
	  jQuery('#department_block').html(data);
	},
	error: function(){
		alert("AJAX REQUEST ERROR!");	
	}
  });
}


function delete_ss_image(oe_id,type,id)
{	 
	if(oe_id && type && id)
	{
		if(confirm("Do you really want to delete this Image!")){
			  jQuery.ajax({
			  type : 'POST',
			  url  : AJAX_PATH+"ajx_delss_image.php?id="+oe_id+"&type="+type+"&ss="+id,
			  cache: false,
			  data : "&rand="+ Date(),
			  success : function(res){
				//ajxpage('ajax/ajx_ss_image.php?type='+type+'&oe_id='+oe_id,'current_ss','fade','');
				jQuery('#block_'+id).hide('fade');
			  },
			  error: function(){
				 alert("Sorry! AJAX call is not responding");
			  }
			 });				
		}
	}
}



function delete_topo_info(type,type_id,topo,topo_id)
{
	var type,type_id,topo,topo_id;
	if(topo)
	{
		if(confirm('Are you sure,want to delete this '+topo+'?')){
		jQuery.post('ajax/delete_my_topo.php',{ type: type,type_id: type_id,topo: topo,topo_id: topo_id }, function() {	
		 
			  ajxpage('ajax/inner_'+type+'_topo.php?topo='+topo+'&'+type+'_id='+type_id,'show_common_'+type_id,'fade','');
		  
		});
		}
	}
}


//submit_common_info('publication','lab','<?=$lab_id?>','text','common_lab_page')
function submit_common_info(topo,type,type_id,id,block)
{
	var text = trim(jQuery('#'+id).val());
	if(text){
		jQuery('#Opendivblock').slideUp('slow');
		jQuery.post('ajax/submit_common_info.php',{ topo: topo,detail: text,type: type,type_id: type_id }, function() {	
		jQuery('#message').fadeOut('slow',function(){
			  jQuery('#message').html('<span class=\"Redcolor\"><strong>'+topo+' text has been submitted successfully</strong></span>').fadeIn('slow',function(){																																											
			  ajxpage('ajax/ajx_'+type+'_'+topo+'.php?'+type+'_id='+type_id,block,'fade','');
			});
		  });
	    });
	}else{ 
		alert ('Please enter your '+topo+' text !');
	}
 	return false;
}