# Create a user
resource "aws_iam_user" "user" {
  name = var.iam_user
}

# Create a group
resource "aws_iam_group" "group" {
  name = var.iam_group
}

# Assign permissions to the group
resource "aws_iam_group_policy_attachment" "group_policy" {
  group      = aws_iam_group.group.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3FullAccess"
}

# Add the user to the group
resource "aws_iam_user_group_membership" "group_membership" {
  user    = aws_iam_user.user.name
  groups  = [aws_iam_group.group.name]
}
