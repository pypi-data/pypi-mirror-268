from cobra.utils.caches import ASSET_CACHE
from cobra.utils.configurations import COBRA_VERSION
from cobra.utils.urls import ASSET_URL
from cobra.utils.requests import session


def get_asset(name, version=COBRA_VERSION, force_download=False):
    """
    Returns asset from CoBRA if it exists.

    :param name: Name of asset to look for.
    :param version: Version of CoBRA to find this asset for.
    :param force_download: If True, asset will be downloaded even if it exists in cache.
    :return: Path to asset file.
    :raises FileNotFoundError: If asset does not exist in CoBRA of specific version.
    """
    asset_file = ASSET_CACHE.joinpath(version).joinpath(name)
    if not force_download and asset_file.exists():
        return asset_file
    asset_URI = f"{ASSET_URL}{name}?version={version}"
    r = session.get(asset_URI)
    if r.status_code == 200:
        asset_file.parent.mkdir(parents=True, exist_ok=True)
        with open(asset_file, 'wb') as f:
            f.write(r.content)
        return asset_file
    else:
        raise FileNotFoundError(f"Asset {name} (version {version}) does not exist in CoBRA.")
