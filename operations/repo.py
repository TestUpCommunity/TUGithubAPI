from core.base import CommonItem


def create_repo(github, name, org=None, description=None, homepage=None, private=False, has_issues=True,
                has_projects=True, has_wiki=True):
    """

    :param github: github 对象
    :param name: string, repo 名称
    :param org: string, 如果是要在一个organization下建repo，就在这里输入 org 名字；否则默认建在当前用户下。
    :param description: string, repo的描述
    :param homepage: string, repo的主页URL
    :param private: boolean, 值为 true的时候建立一个私有repo，为 false时建立公开repo，默认是false
    :param has_issues: boolean, true会建立有issues的repo， false 则没有，默认是true
    :param has_projects: boolean, true会建立有projects的repo， false 则没有，默认是true
    :param has_wiki: boolean, true会建立有wiki的repo，false则没有，默认是true
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
        "has_wiki": has_wiki
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
        result.error = "create repo got {},should be 201".format(str(response.status_code))
    return result


def delete_repo_from_user_by_name(github, owner, repo):
    """

    :param github: Github创建出来github对象
    :param owner: 当前登陆的用户
    :param repo: 要删除的repo关键字

    """
    import re
    delete_list = []
    result = CommonItem()
    result.success = False

    paylod = {'try': 'all'}
    # 列出当前用户的所有repos
    response = github.repos.list_user_repos(username=owner, json=paylod)
    if response.status_code == 200:

        r = response.json()

        for i in r:
            # 从该账户的所有repos中，匹配出所有带有"repo"关键字的repos
            restring = re.match('.*{}.*'.format(repo), i['name'])

            if restring == None:
                continue
            delete_list.append(restring.group())

        for delete_repo in delete_list:
            response = github.repos.delete_a_repo(owner=owner, repo=delete_repo)

            if response.status_code == 204:
                result.success = True
            else:
                result.error = "delete repo got {},should be 204".format(str(response.status_code))

        return result

    return ['list the repos fail','https://developer.github.com/v3/repos/#list-user-repositories']


def



