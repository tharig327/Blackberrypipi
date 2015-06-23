#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "I am PI"

# your twitter consumer and access information goes here
# note: these are garbage strings and won't work
apiKey = 'zTUJVRs8iM4d8qnDT58L6CxBA'
apiSecret = '5braWvGnyJaA2U8RElDVwtlYw7u8i9Ze4f4ihat0Q6h6BsPtgN'
accessToken = '213206695-qaYVILFlWjFxuyCk7LavTEUwoMdrZlUcK9zhfFTQ'
accessTokenSecret = '853OFByA8hdrY3zrqLqapraSTNmw7f827I8JOc7Tz8VOY'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
