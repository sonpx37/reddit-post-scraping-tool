import praw
from praw.models import MoreComments

reddit = praw.Reddit(
    user_agent="Get Comments by /u/Legitimate_Grass9080",   #change 'name' to your username
    client_id="NeCb59uQ1rqDWJEZAhaH9A",                        #change 'XXX' to your id
    client_secret="23zZ6L44IPzfDtuxz74pf5Rtm7Xi0w",                    #change 'XXX' to your secret
)

comments = []

def iter_top_level(comments):
	for top_level_comment in comments:
		if isinstance(top_level_comment, MoreComments):
				yield from iter_top_level(top_level_comment.comments())
		else:
				yield top_level_comment

# use url keyword argument if you want to pass a link instead of id
# https://www.reddit.com/r/technology/comments/zla5lw/musk_shakes_up_twitters_legal_team_as_he_looks_to/
submission = reddit.submission(id='zl0lxa')
# print("-------------", len(submission.comments))

# only first comment output is shown here
for comment in iter_top_level(submission.comments):
	comments.append(comment.body)

print('--comments--', comments)
print('--comments size--', len(comments))
