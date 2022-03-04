import json
import praw

reddit = praw.Reddit(client_id = "S8uN7LL6R-RzspR1dt7YSQ",
		client_secret = "Vm_M7kue2Af0jcnJskaOsAr64YWUBQ",
		user_agent = "Browser:TestScrape v0.1 (by MAST)",
)

commenters = {}

subred = reddit.subreddit("climbing")
hot = subred.hot(limit = 3)
for i in hot:
	print(i.title)
	print(" ")
	id = i.id
	submission = reddit.submission(id=id)
	submission.comments.replace_more()
	comment_queue = submission.comments[:]
	j=0
	while comment_queue:
		print(j)
		j+=1
		comment = comment_queue.pop(0)
		try:
			if comment.author.name not in commenters:
				commenters[comment.author.name] = list()
			parent = reddit.comment(comment.parent_id).author.name
			if parent not in commenters[comment.author.name]:
				commenters[comment.author.name].extend([parent])
		except AttributeError:
			print("Null user detected")
		comment_queue.extend(comment.replies)

with open("graph.json", "w") as outfile:
	json.dump(commenters, outfile)

print(commenters)