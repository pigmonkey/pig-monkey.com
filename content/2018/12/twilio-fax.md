Title: Sending Documents Like It's 1988
Date: 2018-12-25
Tags: shell

Once every year or two I need to send a fax. Never receive, just send. Usually for something involving the finance industry. [Twilio](https://www.twilio.com/) makes this about as painless as it can be in the 21st century.

Unfortunately the [Twilio Fax API](https://www.twilio.com/docs/fax/send) doesn't allow you to post the document to it directly, so the first step is to get the PDF online somewhere. After that, it can be faxed via curl.

    $ curl https://fax.twilio.com/v1/Faxes \
        -X POST \
        -d 'To=%2B15408684391'  \
        -d 'From=%2B14158675309'  \
        -d 'MediaUrl=https://example.com/document.pdf' \
        -u $TWILIO_ACCOUNT_ID:$TWILIO_AUTH_TOKEN

This queues up the document to be sent, which usually takes a couple minutes. Somewhere in the response will be a URL that looks like `https://fax.twilio.com/v1/Faxes/$GIBBERISH`. After a few minutes, this URL can be used to check the status.

    $ curl https://fax.twilio.com/v1/Faxes/$GIBBERISH \
        -X GET \
        -u $TWILIO_ACCOUNT_ID:$TWILIO_AUTH_TOKEN | python -m json.tool

If the status is `queued`, `processing` or `sending`, check back in a few minutes. If it is `delivered`, you're all done and can delete the uploaded PDF. If the status is [something else](https://www.twilio.com/docs/fax/api/faxes#fax-status-values), you probably need to try again. Perhaps ask the recipient to sign out of AOL and hang-up their modem so that their fax machine can accept your call.
