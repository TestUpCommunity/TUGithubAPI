from core.base import CommonItem
def create_a_repo(github, name, org=None,description=None, homepage=None, private=None, has_issues=None,
                  has_projects=None, has_wiki=None):
    """

    :param github: github 对象
    :param name: repo 名称
    :param org: 如果是要在一个organization下建repo，就在这里输入org 名字
    :param description: repo的描述
    :param homepage: repo的主页
    :param private: 是privatepo
    :param has_issues:
    :param has_projects:
    :param has_wiki:
    :return:
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
    result = CommonItem()
    result.success=False
    if org:
        response=github.repos.create_organization_repo(org=org,json=payload)
    else:
        response=github.repos.create_user_repo(json=payload)
    result.response = response
    if response.status_code==201:
        result.success = True
    else:
        result.error = "create repo got {},should be 201".format(str(response.status_code))
    return result