""" Defines General Messages, Exceptions and information for application. """


class AppMessage(object):

    error = {
        'SIGNUP_AGREE_TNC': 'Please agree with Terms and Conditions of '
                            'FaradayFinder.com to complete your registration.',
        'DUPLICATE_EMAIL': 'A user with that email already exists.',
        'PASSWORD_REQUIRED': 'Password field is required.',
        'PASSWORD_MISMATCH': 'The two password fields did not match.',
        'PASSWORD_LENGTH_MIN':'Password length can not be less than 6 characters',
        'PASSWORD_LENGTH_MAX':'Password length can not greater than 30 characters',
        'ZIPCODE_NOT_INT': 'Only numeric value allowed for zipcode',
        'ZIPCODE_LENGTH_INCORRECT': 'Please enter correct length for zipcode.',
        'INVALID_REQUEST': 'Invalid request. Please try again.',
        'EMAIL_SENDING_FAIL': 'Unable to send email.',
        'INCORRECT_ACTIVATION_LINK': 'Incorrect link or Expired, please try again or contact to support team for help.',
        'EMAIL_REQUIRED': 'Email field is required.',
        'EMAIL_NOT_EXISTS': 'This email does not exist, please make sure you are entering correct email.',
        'SIGNUP_FAILS': 'Sorry, we are unable to create your account, please try again.',
        'LOGIN_FAILS': 'Sorry, you are unable to login, please check your credentials.',
        'FORGOT_PASSWORD_REQUEST_FAIL': 'Sorry, we are unable to process your request. Please contact to support team.',
        'PASSWORD_CHANGE_FAILED': 'We are unable to change you password, please make sure you are entering correct old password',
    }

    success = {
        'SIGNUP_SUCCESS': 'Thank you for your registration with FaradayFinder.com. '
                          'Please check your email inbox to activate your account.',
        'FORGOT_PASSWORD_REQUEST_SUCCESS': 'Please check your email inbox to reset your password.',
        'RESET_PASSWORD_SUCCESS': 'Your password has been reset successfully, please login with your new password.',
        'EDIT_PROFILE_SUCCESS': 'Your profile information updated successfully.',
        'EDIT_NETWORK_SUCCESS': 'Your Network information updated successfully.',
        'PASSWORD_CHANGED_SUCCESS': 'Password changed successfully.',
    }

    info = {
        'SIGNUP_EMAIL_SUBJECT': 'FaradayFinder- Signup email',
        'FORGOT_PASSWORD_EMAIL_SUBJECT': 'FaradayFiner- Forgot password email'
    }
