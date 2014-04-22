import mandrill
import logging

def review_your_box(user):
    m = mandrill.Mandrill(settings.MANDRILL_API_KEY)
    URL = # URL to the ratings page
    try:
        template_content = [{'content': URL, 'name': 'FURL'}]
        message = {
            'merge': True,
            'merge_vars': [{'rcpt': user.email,
                            'vars': [{'content': user.fullname, 
                                      'name': 'FNAME'}]}],
            'to': [{
                    'email': user.email,
                    'name': user.fullname,
                    'type': 'to'}],
            'track_clicks': True,
            'track_opens': True,

        }
        m.messages.send_template(
            template_name = 'tnp-item-review', 
            template_content = template_content, 
            message = message
        )
        logging.info('Sent contact email: {0}'.format(form.cleaned_data))
    except mandrill.InvalidKeyError, e:
        logging.error('Cannot send contact email: {0}'.format(
            form.cleaned_data))
        logging.exception(e)
    except mandrill.Error, e:
        logging.error('Cannot send contact email: {0}'.format(
            form.cleaned_data))
        logging.exception(e)

def main():
    users = # SOME WAY TO GET USERS YOU JUST SHIPPED TO
    for user in users:
        review_your_box(user)

if __name__ == "__main__":
    main()
