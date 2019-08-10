from core.base import CommonItem


def create_repo(github, name, org=None, description=None, homepage=None, private=False, has_issues=True,
                has_projects=True, has_wiki=True, auto_init=False):
    """
    创建一个repo。
    :param github: github 对象
    :param name: string, repo 名称
    :param org: string, 如果是要在一个organization下建repo，就在这里输入 org 名字；否则默认建在当前用户下。
    :param description: string, repo的描述
    :param homepage: string, repo的主页URL
    :param private: boolean, 值为 true的时候建立一个私有repo，为 false时建立公开repo，默认是false
    :param has_issues: boolean, true会建立有issues的repo， false 则没有，默认是true
    :param has_projects: boolean, true会建立有projects的repo， false 则没有，默认是true
    :param has_wiki: boolean, true会建立有wiki的repo，false则没有，默认是true
    :param auto_init: boolean, true会初始化创建的repo，false则没有，默认是false
    :return: common item
    """
    result = CommonItem()
    payload = {
        "name": name,
        "description": description,
        "homepage": homepage,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki,
        "auto_init": auto_init
    }
    result.success = False
    if org:
        response = github.repos.create_organization_repo(org=org, json=payload)
    else:
        response = github.repos.create_user_repo(json=payload)
    result.response = response
    if response.status_code == 201:
        result.success = True
    else:
        result.error = "create repo={} got {},should be 201".format(name, str(response.status_code))
    return result


def create_branch(github, owner, repo, new_branch_name, source_branch_name):
    """
    在现有repo上创建一个分支，从老分支上拉出一个新分支
    :param github: github 对象
    :param owner:  string, owner 名称，可以是github org 名称或当前用户的用户名
    :param repo:  string, repo 名称
    :param new_branch_name: 新分支的名称
    :param source_branch_name: 老分支的名称
    :return: common item
    """
    result = CommonItem()
    result.success = False
    result.error = None
    response = github.gitdata.refs.get_a_reference(owner, repo, source_branch_name)
    if response.status_code != 200:
        result.success = False
        result.error = "get source branch sha fails,repo={} got {},should be 200".format(repo,
                                                                                         str(response.status_code))
        result.response = response
        return result

    source_branch_sha = response.content["object"]["sha"]

    payload = {
        "ref": "refs/heads/{}".format(new_branch_name),
        "sha": source_branch_sha
    }
    response = github.gitdata.refs.create_a_reference(owner, repo, json=payload)
    if response.status_code != 201:
        result.success = False
        result.error = "create branch reference fails,repo={} got {},should be 201".format(repo,
                                                                                           str(response.status_code))
        result.response = response
        return result
    result.success = True
    result.response = response
    return result
