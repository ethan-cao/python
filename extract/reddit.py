import praw


reddit = praw.Reddit(
    client_id="-pi3jNA_C04475hHvHWkJg",
    client_secret="nidUH4E5qiOJ2St_C5a3_X1iWY_htw",
    user_agent="my user agent",
)

print(reddit.read_only)
# Output: True


#  obtaining 10 “hot” submissions from r/UKPersonalFinance:
for submission in reddit.subreddit("UKPersonalFinance").hot(limit=10):
    print(submission.title)
