from github import Github

if __name__ == '__main__':
    github = Github(token="xxxx")
    username = "zhangting85"
    orgname = "TestUpCommunity"
    reponame ="111"

    from operations.repo import create_a_repo
    result = create_a_repo(github,"simpletest")
    assert result.success == True,result.error