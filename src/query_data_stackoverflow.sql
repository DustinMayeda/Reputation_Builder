SELECT TOP 10000
  Posts.CreationDate
, Posts.Id
, Posts.Title
, Posts.ViewCount
, Posts.Body
, Posts.OwnerUserId
, Posts.OwnerDisplayName
, Posts.Score
, Posts.Tags
, Posts.CommentCount
, Posts.FavoriteCount
, Users.Reputation
, Users.CreationDate
, Users.LastAccessDate
, Users.Location
, Users.WebsiteUrl
, Users.UpVotes
, Users.DownVotes
, Users.Age
FROM
  Posts JOIN Users on Posts.OwnerUserId = Users.Id
WHERE
  Posts.AnswerCount = 0
ORDER BY
  Posts.CreationDate DESC
