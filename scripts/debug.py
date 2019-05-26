from github import Github
from operations.repo import create_repo

if __name__ == '__main__':
    github = Github(token="xxxx")

    # # test 1: 在当前用户下创建一个repo，除了repo名字以外全部用默认值
    result = create_repo(github, "simpletest")
    assert result.success == True, result.error

    # test 2: 在当前用户下创建一个repo，使用一些输入值
    result = create_repo(github, "simpletest03", has_issues=False)
    assert result.success == True, result.error
