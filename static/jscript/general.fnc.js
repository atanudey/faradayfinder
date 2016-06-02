// JavaScript Document

/**
 * DHTML resetting image button forms script. Courtesy of SmartWebby.com (http://www.smartwebby.com/dhtml/)
 */
var AJAX_PATH = 'ajax/';
function ResetForm(which){
	var pass=true
	var first=-1
	if (document.images){
	for (i=0;i<which.length;i++){
	var tempobj=which.elements[i]
	 if (tempobj.type=="text"){
	  eval(tempobj.value="")
	  if (first==-1) {first=i}
	 }
	 else if (tempobj.type=="checkbox") {
	  eval(tempobj.checked=0)
	  if (first==-1) {first=i}
	 }
	 else if (tempobj.col!="") {
	  eval(tempobj.value="")
	  if (first==-1) {first=i}
	 }
	}
	}
	which.elements[first].focus()
	return false
}


function selected_values(id)
{
	var items;
	var list = document.getElementById(id);
	var selected = new Array(); 
 
	for (i = 0; i < list.options.length; i++) {
		if (list.options[ i ].selected) {
			selected.push(list.options[ i ].value);
		}
	} 
	items = selected.join('*');
	return items; 
}


function getallselected(path,variable,idd,div_name,effect,hourglass,time) {
	var items;
	var list = z.getElementById(idd);
	var selected = new Array(); 
 
	for (i = 0; i < list.options.length; i++) {
		if (list.options[ i ].selected) {
			selected.push(list.options[ i ].value);
		}
	} 
	items = selected.join('*');
	ajxpage(path+'?'+variable+'='+items,div_name,effect,hourglass,time);
/*	item2 = str_replace('*',',',items);
	document.getElementById("mytext").value = items;*/
}


function str_replace (search, replace, subject)
{
	var result = "";
	var  oldi = 0;
	for (i = subject.indexOf (search); i > -1; i = subject.indexOf (search, i))
	{
	result += subject.substring (oldi, i);
	result += replace;
	i += search.length;
	oldi = i;
	}
	return result + subject.substring (oldi, subject.length);
}

function slideSwitch() {
    var jQueryactive = jQuery('#slideshow DIV.active');

    if ( jQueryactive.length == 0 ) jQueryactive = jQuery('#slideshow DIV:last');

    // use this to pull the divs in the order they appear in the markup
    var jQuerynext =  jQueryactive.next().length ? jQueryactive.next()
        : jQuery('#slideshow DIV:first');

    // uncomment below to pull the divs randomly
    // var jQuerysibs  = jQueryactive.siblings();
    // var rndNum = Math.floor(Math.random() * jQuerysibs.length );
    // var jQuerynext  = jQuery( jQuerysibs[ rndNum ] );


    jQueryactive.addClass('last-active');

    jQuerynext.css({opacity: 0.0})
        .addClass('active')
        .animate({opacity: 1.0}, 1000, function() {
            jQueryactive.removeClass('active last-active');
        });
}


function clear_form_elements(ele) { 
	    $(ele).find(':input').each(function() {
		switch(this.type) {
			case 'password':
			case 'select-multiple':
			case 'select-one':
			case 'text':
			case 'textarea':
				$(this).val('');
				break;
			case 'checkbox':
			case 'radio':
				this.checked = false;
		}
	}); 
}


function IsNumeric(strString)
   //  check for valid numeric strings	
   {
   var strValidChars = "0123456789.-";
   var strChar;
   var blnResult = true;

   if (strString.length == 0) return false;

   //  test strString consists of valid characters listed above
   for (i = 0; i < strString.length && blnResult == true; i++)
      {
      strChar = strString.charAt(i);
      if (strValidChars.indexOf(strChar) == -1)
         {
         blnResult = false;
         }
      }
   return blnResult;
   }


function redir_search_result()
{
	var lesson = jQuery('#search_lesson').val();
	if(lesson)
	 window.location = 	SITEURL+'browsebylesson/'+lesson+'/all/'; 
	else
	 window.location =  SITEURL;
}
 

function clearForm(oForm) {
    
   var elements = oForm.elements; 
    
  oForm.reset();

  for(i=0; i<elements.length; i++) {
      
	field_type = elements[i].type.toLowerCase();
	
	switch(field_type) {
	
		case "text": 
		case "password": 
		case "textarea":
	        case "hidden":	
			
			elements[i].value = ""; 
			break;
        
		case "radio":
		case "checkbox":
  			if (elements[i].checked) {
   				elements[i].checked = false; 
			}
			break;

		case "select-one":
		case "select-multi":
            		/*elements[i].selectedIndex = -1;*/
					elements[i].selectedIndex = 0;
			break;

		default: 
			break;
	}
    }
}


function email_validate(email) {
   var reg = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
   if(reg.test(email) == false) {
      return false;
   }
   else return true;
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


function show_cate(reg,count)
{	
	for(var j=0; j<count;j++)
	{
		var value = jQuery('#'+j+'cate').html();
		var one   = strip_tags(value);
		var two   = one.replace('&nbsp;','');	
		var patt1 = new RegExp(reg,"gi");
		
		if(two.match(patt1))
		{		jQuery('#'+j+'cate').show();		}
		else
		{		jQuery('#'+j+'cate').hide();		}
	}
}