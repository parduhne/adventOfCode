# helper function
def parsePolicy(policy):
  nums = policy.split(' ')[0].split('-')
  return [int(i) for i in nums] + [policy.split(' ')[1]]

# function used for part 1
def comparePasswordToPolicyPt1(policy, password):
  ch_count = password.count(policy[2])
  if (ch_count <= policy[1] and ch_count >= policy[0]):
    return 1
  else:
    return 0

# function used for part 2
def comparePasswordToPolicyPt2(policy, password):
  if ((password[policy[0] - 1] == policy[2] and password[policy[1] - 1] != policy[2]) or (password[policy[0] - 1] != policy[2] and password[policy[1] - 1] == policy[2])):
    return 1
  else:
    return 0

# this function can be used for both parts
def parsePasswordPolicySet(file):
  file_lines = file.readlines()
  val_count = 0
  for line in file_lines:
    parsed_line = line.split(': ')
    val_count += comparePasswordToPolicyPt2(parsePolicy(parsed_line[0]), parsed_line[1])
  print(val_count)

file = open("passwordSet.txt")
parsePasswordPolicySet(file)