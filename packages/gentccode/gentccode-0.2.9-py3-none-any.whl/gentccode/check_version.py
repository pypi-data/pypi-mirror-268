import xmlrpc.client
import importlib.metadata


def get_latest_version(package_name):
    try:
        client = xmlrpc.client.ServerProxy("https://pypi.org/pypi")
        package_info = client.package_releases(package_name)
        if package_info:
            latest_version = package_info[0]
            return latest_version
        else:
            return None
    except Exception as e:
        # print(f"Error fetching version information for '{package_name}': {str(e)}")
        return None


def check_package_version(package_name):
    latest_version = get_latest_version(package_name)

    if latest_version is None:
        pass
    else:
        # 获取当前版本号。

        current_version = importlib.metadata.version(package_name)
        if current_version < latest_version:
            print(
                f"'{package_name}' is outdated. latest version is {current_version} -> {latest_version}."
            )
            print(
                f"You should consider upgrading using 'pip install --upgrade {package_name}'."
            )


def get_current_version(package_name):
    current_version = importlib.metadata.version(package_name)
    return current_version
