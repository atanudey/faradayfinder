// JavaScript Document
function validate_organization()
{
	var error =0;
	
	if(trim(jQuery('#name').val())=="")
	{
		jQuery('#err_name').html('Please enter Organization name');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	
	
	if(trim(jQuery('#url').val())=="")
	{
		jQuery('#err_url').html('Please enter Organization URL');
		error++;
	}
	else
	{
		jQuery('#err_url').html('');		
	}	
	
	
	if(trim(jQuery('#photo').val())=="")
	{
		jQuery('#err_photo').html('Please uploade Organization photo');
		error++;
	}
	else
	{
		jQuery('#err_photo').html('');		
	}
	
	if(trim(jQuery('#website').val())=="")
	{
		jQuery('#err_website').html('Please enter website');
		error++;
	}
	else
	{
		jQuery('#err_website').html('');		
	}
	
	
	if(trim(jQuery('#twitter').val())=="")
	{
		jQuery('#err_twitter').html('Please enter twitter account');
		error++;
	}
	else
	{
		jQuery('#err_twitter').html('');		
	}
	
	
	if(trim(jQuery('#address').val())=="")
	{
		jQuery('#err_address').html('Please enter address');
		error++;
	}
	else
	{
		jQuery('#err_address').html('');		
	}
	
	
	if(trim(jQuery('#city').val())=="")
	{
		jQuery('#err_city').html('Please enter city');
		error++;
	}
	else
	{
		jQuery('#err_city').html('');		
	}	
	
	
	if(trim(jQuery('#state').val())=="")
	{
		jQuery('#err_state').html('Please enter state');
		error++;
	}
	else
	{
		jQuery('#err_state').html('');		
	}	
	
	
	if(trim(jQuery('#country').val())=="")
	{
		jQuery('#err_country').html('Please enter country');
		error++;
	}
	else
	{
		jQuery('#err_country').html('');		
	}		
	
	
	if(trim(jQuery('#zipcode').val())=="")
	{
		jQuery('#err_zipcode').html('Please enter zipcode');
		error++;
	}
	else
	{
		jQuery('#err_zipcode').html('');		
	}	
	
	
	if(error > 0)	{ return false; }
	else		{ return true;  }
	//------------		
}


function validate_page()
{
	var error =0;
	
	if(trim(jQuery('#name').val())=="")
	{
		jQuery('#err_name').html('Please enter Page name');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	
	
	if(trim(jQuery('#title').val())=="")
	{
		jQuery('#err_title').html('Please enter Page title');
		error++;
	}
	else
	{
		jQuery('#err_title').html('');		
	}
	
	if(trim(jQuery('#url').val())=="")
	{
		jQuery('#err_url').html('Please enter page url');
		error++;
	}
	else
	{
		jQuery('#err_url').html('');		
	}
	
	
	if(trim(jQuery('#page_title').val())=="")
	{
		jQuery('#err_page_title').html('Please enter seo page title');
		error++;
	}
	else
	{
		jQuery('#err_page_title').html('');		
	}
	
	
	if(trim(jQuery('#page_keywords').val())=="")
	{
		jQuery('#err_page_keywords').html('Please enter page keywords');
		error++;
	}
	else
	{
		jQuery('#err_page_keywords').html('');		
	}
	
	
	if(trim(jQuery('#page_abstract').val())=="")
	{
		jQuery('#err_page_abstract').html('Please enter page abstract info');
		error++;
	}
	else
	{
		jQuery('#err_page_abstract').html('');		
	}	
	
	
	if(trim(jQuery('#page_description').val())=="")
	{
		jQuery('#err_page_description').html('Please enter meta description');
		error++;
	}
	else
	{
		jQuery('#err_page_description').html('');		
	}	
	
	
	if(trim(jQuery('#description').val())=="")
	{
		jQuery('#err_description').html('Please enter page description');
		error++;
	}
	else
	{
		jQuery('#err_description').html('');		
	}		
	
	
	if(error > 0)	{ return false; }
	else		{ return true;  }
	//------------		
}


function validate_user()
{
	var error =0;
	
	if(trim(jQuery('#name').val())=="")
	{
		jQuery('#err_name').html('Please enter name');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	
	
	if(trim(jQuery('#photo').val())=="")
	{
		jQuery('#err_photo').html('Please enter photo');
		error++;
	}
	else
	{
		jQuery('#err_photo').html('');		
	}
	
	if(trim(jQuery('#birthday').val())=="")
	{
		jQuery('#err_birthday').html('Please enter birthday');
		error++;
	}
	else
	{
		jQuery('#err_birthday').html('');		
	}
	
	
	if(trim(jQuery('#email').val())=="")
	{
		jQuery('#err_email').html('Please enter email');
		error++;
	}
	else
	{
		jQuery('#err_email').html('');		
	}
	
	
	if(trim(jQuery('#password').val())=="")
	{
		jQuery('#err_password').html('Please enter password');
		error++;
	}
	else
	{
		jQuery('#err_password').html('');		
	}
	
	
	if(trim(jQuery('#repassword').val())=="")
	{
		jQuery('#err_repassword').html('Please enter re-password');
		error++;
	}
	else
	{
		jQuery('#err_repassword').html('');		
	}	
	
	
	if(trim(jQuery('#from').val())=="")
	{
		jQuery('#err_from').html('Please enter from info');
		error++;
	}
	else
	{
		jQuery('#err_from').html('');		
	}	
	
	
	if(trim(jQuery('#city').val())=="")
	{
		jQuery('#err_city').html('Please enter city');
		error++;
	}
	else
	{
		jQuery('#err_city').html('');		
	}		
	
	
	if(trim(jQuery('#state').val())=="")
	{
		jQuery('#err_state').html('Please enter state');
		error++;
	}
	else
	{
		jQuery('#err_state').html('');		
	}	
	
	 
	
	if(trim(jQuery('#country').val())=="")
	{
		jQuery('#err_country').html('Please enter country');
		error++;
	}
	else
	{
		jQuery('#err_country').html('');		
	}
	
	if(trim(jQuery('#zipcode').val())=="")
	{
		jQuery('#err_zipcode').html('Please enter zipcode');
		error++;
	}
	else
	{
		jQuery('#err_zipcode').html('');		
	}
	

	if(error > 0)	{ return false; }
	else		    { return true;  }
	//------------		
}

function validate_faq_category()
{ 
	var error =0;	
	if(trim(jQuery('#name').val())=="")
	{
		jQuery('#err_name').html('Please enter Faq Category Title');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	 

	if(error > 0)	{ return false; }
	else		    { return true;  }
	//------------		
}

function validate_user_edit()
{
	var error =0;
	
	if(trim(jQuery('#name').val())=="")
	{
		jQuery('#err_name').html('Please enter name');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	
 
	
	if(trim(jQuery('#birthday').val())=="")
	{
		jQuery('#err_birthday').html('Please enter birthday');
		error++;
	}
	else
	{
		jQuery('#err_birthday').html('');		
	}
	
	
	if(trim(jQuery('#email').val())=="")
	{
		jQuery('#err_email').html('Please enter email');
		error++;
	}
	else
	{
		jQuery('#err_email').html('');		
	}
	
	 
	
	if(trim(jQuery('#from').val())=="")
	{
		jQuery('#err_from').html('Please enter from info');
		error++;
	}
	else
	{
		jQuery('#err_from').html('');		
	}	
	
	
	if(trim(jQuery('#city').val())=="")
	{
		jQuery('#err_city').html('Please enter city');
		error++;
	}
	else
	{
		jQuery('#err_city').html('');		
	}		
	
	
	if(trim(jQuery('#state').val())=="")
	{
		jQuery('#err_state').html('Please enter state');
		error++;
	}
	else
	{
		jQuery('#err_state').html('');		
	}	
	
	 
	
	if(trim(jQuery('#country').val())=="")
	{
		jQuery('#err_country').html('Please enter country');
		error++;
	}
	else
	{
		jQuery('#err_country').html('');		
	}
	
	if(trim(jQuery('#zipcode').val())=="")
	{
		jQuery('#err_zipcode').html('Please enter zipcode');
		error++;
	}
	else
	{
		jQuery('#err_zipcode').html('');		
	}
	

	if(error > 0)	{ return false; }
	else		    { return true;  }
	//------------		
}

function validate_faq_question()
{ 
	var error =0;	
	if(trim(jQuery('#question').val())=="")
	{
		jQuery('#err_question').html('Please enter Question');
		error++;
	}
	else
	{
		jQuery('#err_name').html('');		
	}	
	 
	if(trim(jQuery('#answer').val())=="")
	{
		jQuery('#err_answer').html('Please enter Answer');
		error++;
	}
	else
	{
		jQuery('#err_answer').html('');		
	}	
	

	if(error > 0)	{ return false; }
	else		    { return true;  }
	//------------		
}

function create_url($val)
{
	$val = $val.toLowerCase();
	var $str = "";
	for($i = 0; $i< $val.length; $i++)
	{
	 if ($val.charAt($i)  == " ")
	 {
		if ($str.substr(-1) != "-")
		 $str += "-";
		}	
		else if ( ($val.charCodeAt($i)	 > 47 && $val.charCodeAt($i) < 58) || ($val.charCodeAt($i) > 64 && $val.charCodeAt($i) < 91) ||  ($val.charCodeAt($i) > 96 && $val.charCodeAt($i) < 123))		$str += $val.charAt($i) ;
	}
	return $str;
}