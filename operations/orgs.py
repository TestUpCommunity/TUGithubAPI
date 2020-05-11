from core.base import CommonItem


def create_org_and_repo(github, org, name, description=None, private=None, has_issues=None, has_projects=None, has_wiki=None):
    """

       :param github: github 对象
       :param name: string, repo 名称
       :param org: string, 如果是要在一个organization下建repo，就在这里输入 org 名字；否则默认建在当前用户下。
       :param description: string, repo的描述
       :param private: boolean, 值为 true的时候建立一个私有repo，为 false时建立公开repo，默认是false
       :param has_issues: boolean, true会建立有issues的repo， false 则没有，默认是true
       :param has_projects: boolean, true会建立有projects的repo， false 则没有，默认是true
       :param has_wiki: boolean, true会建立有wiki的repo，false则没有，默认是true
       :return: common item
       """
    result = CommonItem()
    result.success = False
    response = github.orgs.get_on_organization(org=org)

    payload = {
        "name": name,
        "description": description,
        "private": private,
        "has_issues": has_issues,
        "has_projects": has_projects,
        "has_wiki": has_wiki
    }

    if response.status_code == 200:
        response = github.repos.create_organization_repo(org=org,json=payload )
        if response.status_code == 201:
            result.success = True
        else:
            result.error = "create repo got {},should be 201".format(str(response.status_code))

        return result

    return "failed to create org"